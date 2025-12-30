import pyautogui
import pyperclip
import time
import os

url = "https://www.bilibili.com/"
text = f'msedge {url}'
searching_text = "怕上火暴王老菊"
upName = "wanglaoju.png"

"""打开相关网址"""
pyautogui.hotkey('win', 'r')
pyautogui.press('backspace')
pyperclip.copy(text)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.3)
pyautogui.press('enter')


"""图像识别搜索框"""
ICON_TEMPLATE = './bili/magnifier.png'  # 替换为你自己的图标文件名
CONFIDENCE = 0.8                  # 匹配阈值：0.7~0.95（越高越严格）
TIMEOUT = 10                        # 最长等待时间（秒）

if not os.path.exists(ICON_TEMPLATE):
    print(f"❌ 错误：找不到模板文件 '{ICON_TEMPLATE}'")
    print("👉 请将图标截图保存为该文件名，并放在脚本同目录下。")
    exit()

print("🔎 正在搜索图标...")
start_time = time.time()
icon_center = None

while time.time() - start_time < TIMEOUT:
    try:
        # 使用 OpenCV 进行模板匹配（需 opencv-python）
        icon_center = pyautogui.locateCenterOnScreen(
            ICON_TEMPLATE,
            confidence=CONFIDENCE,
            grayscale=False  # 设为 True 可提速，但可能降低准确率
        )
        if icon_center is not None:
            break
    except Exception as e:
        print(f"⚠️ 识别出错: {e}")
    time.sleep(0.5)  # 避免 CPU 占用过高

# 判断是否找到
if icon_center is None:
    print("❌ 失败：在屏幕上未找到匹配的图标！")
    print("\n🔧 排查建议：")
    print("1. 检查截图是否清晰、无文字、无背景干扰")
    print("2. Windows 显示缩放是否为 100%？（设置 > 系统 > 显示 > 缩放）")
    print("3. 尝试降低 CONFIDENCE（如 0.7）")
    print("4. 确保图标当前显示在屏幕上（未被其他窗口覆盖）")
    exit()

print(f"搜索框最右侧的坐标是：{icon_center}")
x,y = icon_center
x = x - 100
time.sleep(0.5)
pyautogui.moveTo(x,y)
pyautogui.click()
pyperclip.copy(searching_text)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

from toolsForAutogui import *
icon_center = imageIdentify(f"./bili/{upName}")
pyautogui.moveTo(icon_center)
pyautogui.click()

icon_center = imageIdentify(f"./bili/Allvideos.png")
x,y = icon_center
x = x + 50
pyautogui.moveTo(x,y)
pyautogui.click()

# icon_center = imageIdentify(f"./bili/newest.png")
# x,y = icon_center
# y = y + 120
# pyautogui.moveTo(x,y)
# pyautogui.click()


if not imageJudge(f"./bili/afterThumbUp.png"):
    icon_center = imageIdentify(f"./bili/thumbup.png")
pyautogui.moveTo(icon_center)
pyautogui.mouseDown()
time.sleep(3)
pyautogui.mouseUp()
pyautogui.hotkey('ctrl', 'w')