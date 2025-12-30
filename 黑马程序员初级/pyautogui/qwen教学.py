import pyautogui
import pyperclip  # 需要安装: pip install pyperclip
import time

print("3 秒后开始，请准备好！")
time.sleep(3)

# 打开记事本（用 Win+R 更稳定）
pyautogui.hotkey('win', 'r')
time.sleep(0.3)
pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(1.5)

# 准备混合文本
text = "Hello, PyAutoGUI! 我学会自动化啦！"

# 复制到剪贴板
pyperclip.copy(text)

# 粘贴（无论当前输入法是什么，都能正确显示）
pyautogui.hotkey('ctrl', 'v')

# 按回车
pyautogui.press('enter')