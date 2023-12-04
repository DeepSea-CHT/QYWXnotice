import pyautogui
import win32api
import win32con
import win32gui
import win32clipboard as clipboard
import requests
import schedule
import time

from IsvServiceLog import IsvServiceLog

pyautogui.FAILSAFE=False

def FindWindow(chatroom):
    win = win32gui.FindWindow(None, chatroom)
    print("找到窗口句柄")
    if win != 0:
        win32gui.ShowWindow(win, win32con.SW_SHOWMINIMIZED)
        win32gui.ShowWindow(win, win32con.SW_SHOWNORMAL)
        win32gui.ShowWindow(win, win32con.SW_SHOW)
        win32gui.SetWindowPos(win, win32con.HWND_TOPMOST, 0, 0, 300, 500, win32con.SWP_SHOWWINDOW)
        win32gui.SetForegroundWindow(win)  # 获取控制
        time.sleep(1)
        tit = win32gui.GetWindowText(win)
        print("已启动【" + str(tit) + "】窗口")
    else:
        print("找不到企业微信窗口")
        exit()


# 粘贴复制回车
def ClipboardTextEnter(ClipboardText):
    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardData(win32con.CF_UNICODETEXT, ClipboardText)
    clipboard.CloseClipboard()
    time.sleep(0.8)
    win32api.keybd_event(17, 0, 0, 0)  # 按下ctrl键
    win32api.keybd_event(86, 0, 0, 0)  # 按下v键
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放v键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放ctrl键
    time.sleep(0.8)
    win32api.keybd_event(13, 0, 0, 0)  # 按下回车键
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放回车键


# 定位到搜索框
def SelectSearchBox():
    pyautogui.moveTo(143, 39)
    pyautogui.click()


def make_request():
    try:
        # 发送请求的代码 获取推送信息
        response = requests.post('')
        if response.status_code == 200:
            data_list = response.json()  # 将响应转换为JSON格式的列表
            id_list_error = []
            id_list_notice = []
            for key, value in data_list.items():
                SelectSearchBox()
                ClipboardTextEnter(key)
                for data in value:
                    log = IsvServiceLog(data)
                    if log.type == 1:
                        #报警
                        ClipboardTextEnter(log.__error__())
                        id_list_error.append(log.id)
                    elif log.type == 2:
                        #通知
                        ClipboardTextEnter(log.__notice__())
                        id_list_notice.append(log.id)
            #ack 响应
            requests.post("", json=id_list_error)
            #ack 响应
            requests.post("", json=id_list_notice)
    except Exception as e:
        # 处理其他类型的异常的代码块
        print("发生了一个异常:", str(e))

# schedule.every(11).seconds.do(make_request)

# 示例用法
if __name__ == '__main__':
    # 先启动企业微信窗口
    make_request()
    # FindWindow("企业微信")
    time.sleep(1)
    print("开始")
    # 循环执行定时任务
    while True:
        print("执行")
        # schedule.run_pending()
        time.sleep(10)
