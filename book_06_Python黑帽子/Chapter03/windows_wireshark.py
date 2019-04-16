# !/usr/bin/env python2
# -*- coding: utf-8 -*-

import socket
import os
import struct
import threading
import time
import sys
from netaddr import IPNetwork, IPAddress
from ctypes import *


# 监听的主机
host = [a for a in os.popen('route print').readlines() if ' 0.0.0.0 ' in a][0].split()[
    -2]  # Windows 下获取正在使用的网卡地址(内网 ip)
print("Your Host IP Address is {}".format(host))

# 网络协议分析开关
try:
    switch = raw_input("Enable Network Protocol Analyzer?(yes/no): ")
    if not switch.strip().lower().startswith("n"):
        switch = True
    else:
        switch = False
except:
    switch = input("开启网络协议分析?(yes/no): ")
    if not switch.strip().lower().startswith("n"):
        switch = True
    else:
        print("网络嗅探暂时仅支持 Python2.")
        sys.exit(0)

# 扫描的目标子网
temp = host.split('.')
temp[-1] = '0/24'
subnet = ".".join(temp)  # 意思是 subnet = "192.168.1.0/24"s

# 自定义的字符串， 我们将在 ICMP 响应中进行核对
magic_message = "PYTHONRULES!"

# 内网存活的主机数量
hosts_count = 0


# 批量发送 UDP 数据包
def udp_sender(subnet, magic_message):
    time.sleep(5)
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for ip in IPNetwork(subnet):
        try:
            sender.sendto(magic_message, ("{}".format(ip), 65212))
        except:
            pass


# ip 头定义
class IP(Structure):
    _fields_ = [
        ("ihl", c_ubyte, 4),
        ("version", c_ubyte, 4),
        ("tos", c_ubyte),
        ("len", c_ushort),
        ("id", c_ushort),
        ("offset", c_ushort),
        ("ttl", c_ubyte),
        ("protocol_num", c_ubyte),
        ("sum", c_ushort),
        # ("src", c_ulong),
        ("src", c_uint32),
        # ("dst", c_ulong)
        ("dst", c_uint32)
    ]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        # 协议字段与协议名称对应
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}

        # 可读性更强的 ip 地址
        # self.src_address = socket.inet_ntoa(struct.pack("<L", self.src))
        self.src_address = socket.inet_ntoa(struct.pack("@I", self.src))
        # self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst))
        self.dst_address = socket.inet_ntoa(struct.pack("@I", self.dst))

        # 协议类型
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)


class ICMP(Structure):
    _fields_ = [
        ("type", c_ubyte),
        ("code", c_ubyte),
        ("checksum", c_ushort),
        ("unused", c_ushort),
        ("next_hop_mtu", c_ushort)
    ]

    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        pass


# 创建原始套接字， 然后绑定在公开接口上
if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

try:
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
except:
    print("Error, must be run with admin privileges.")
    sys.exit(0)

sniffer.bind((host, 0))

# 设置在捕获的数据包中包含 ip 头
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# 在 Windows 平台上， 我们需要设置 IOCTL 以启动混杂模式
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# 开始发送数据包
t = threading.Thread(target=udp_sender, args=(subnet, magic_message))
t.start()

try:
    while True:
        # 读取数据包
        raw_buffer = sniffer.recvfrom(65565)[0]

        # 将缓冲区的前 20 个字节按 ip 头进行解析
        ip_header = IP(raw_buffer[0:20])

        # TODO: You can open it.
        # 输出协议和通信双方 ip 地址
        if switch:
            print("Protocol: {} {} -> {}".format(ip_header.protocol, ip_header.src_address, ip_header.dst_address))

        # 如果为 ICMP， 进行处理
        if ip_header.protocol == "ICMP":
            # 计算 ICMP 包的起始位置
            offset = ip_header.ihl * 4
            buf = raw_buffer[offset:offset + sizeof(ICMP)]

            # 解析 ICMP 数据
            icmp_header = ICMP(buf)
            # print "ICMP -> Type: {} Code: {}".format(icmp_header.type, icmp_header.code)

            # 检查类型和代码值是否为 3
            if icmp_header.code == 3 and icmp_header.type == 3:

                # 确认响应的主机在我们的目标子网之内
                if IPAddress(ip_header.src_address) in IPNetwork(subnet):

                    if not switch:
                        # 确认 ICMP 数据中包含我们发送的自定义的字符串
                        if raw_buffer[len(raw_buffer) - len(magic_message):] == magic_message:
                            hosts_count += 1
                            print("[*] Host Up: {} Count: {}".format(ip_header.src_address, hosts_count))


# 处理 CTRL-C
except KeyboardInterrupt:
    # 如果运行在 Windows 上， 关闭混杂模式
    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
