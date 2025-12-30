import pyautogui
import time

x, y = 114, 423


# 右键点击图标
pyautogui.rightClick(x, y)
time.sleep(0.3)

# 按下方向键选择“打开”（通常是第一个）
pyautogui.press('up')    # 有些系统“打开”在顶部，需按 up；有些在底部，按 down
time.sleep(0.1)
pyautogui.press('enter')