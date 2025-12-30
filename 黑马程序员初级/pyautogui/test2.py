import pyautogui
import pyperclip
import time
import os
from toolsForAutogui import imageIdentify


# 配置
PLAY_BTN = "./bili/playbutton.png"
CONFIDENCE = 0.8


def get_sorted_buttons():
    """获取所有播放按钮，并按「从上到下、从左到右」排序"""
    buttons = list(pyautogui.locateAllOnScreen(
        PLAY_BTN,
        confidence=CONFIDENCE,
    ))

    # 转为 (x, y, box) 列表，按 y（行）为主，x（列）为辅排序
    button_centers = []
    for box in buttons:
        x, y = pyautogui.center(box)
        button_centers.append((x, y, box))

    # 先按 y（垂直位置）排序，再按 x（水平位置）排序
    button_centers.sort(key=lambda p: (p[1], p[0]))

    return button_centers


# 主流程
print("🔍 正在查找播放按钮...")
buttons = get_sorted_buttons()

if not buttons:
    print("❌ 未找到任何播放按钮，请检查截图和区域")
    exit()

print(f"✅ 找到 {len(buttons)} 个视频，开始按顺序播放...")

for i, (x, y, box) in enumerate(buttons):
    print(f"\n--- 第 {i + 1} 个视频 (位置: x={x}, y={y}) ---")

    # 点击该视频
    pyautogui.click(x, y)
    time.sleep(3)  # 等待视频页加载

    # 👇 在这里执行你的操作（如三连）
    # do_triple_action()

    # 返回搜索结果页
    pyautogui.hotkey('alt', 'left')
    time.sleep(2)

print("🔚 所有视频处理完毕！")