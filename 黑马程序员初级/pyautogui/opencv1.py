import pyautogui
import time
import os

# === 配置区 ===
ICON_TEMPLATE = './img/bdfy.png'  # 替换为你自己的图标文件名
CONFIDENCE = 0.85                   # 匹配阈值：0.7~0.95（越高越严格）
TIMEOUT = 10                        # 最长等待时间（秒）

print("🚀 开始自动化任务...")
print(f"🔍 将在桌面查找图标: {ICON_TEMPLATE}")
print("⏳ 请确保桌面可见，且图标未被窗口遮挡！")
time.sleep(3)

# 检查模板文件是否存在
if not os.path.exists(ICON_TEMPLATE):
    print(f"❌ 错误：找不到模板文件 '{ICON_TEMPLATE}'")
    print("👉 请将图标截图保存为该文件名，并放在脚本同目录下。")
    exit()


# 尝试定位图标（带超时重试）
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

# 【关键修改】更可靠的双击方式
print(f"图标坐标是：{icon_center}")
pyautogui.moveTo(icon_center)
time.sleep(0.3)

# 先单击选中（避免焦点问题）
pyautogui.click()
time.sleep(0.2)

# 再执行双击，控制间隔（Windows 默认双击间隔 ~0.5 秒，这里用 0.2~0.3 更安全）


# 可选：等待并执行后续操作
time.sleep(3)
print("🎉 任务完成！")