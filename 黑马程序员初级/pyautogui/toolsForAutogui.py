import pyautogui, time, os

def imageIdentify(icon_template, confidence=0.8, timeout=10):
    """图像识别搜索"""

    if not os.path.exists(icon_template):
        print(f"❌ 错误：找不到模板文件 '{icon_template}'")
        print("👉 请将图标截图保存为该文件名，并放在脚本同目录下。")
        exit()

    print("🔎 正在搜索图标...")
    start_time = time.time()
    icon_center = None

    while time.time() - start_time < timeout:
        try:
            # 使用 OpenCV 进行模板匹配（需 opencv-python）
            icon_center = pyautogui.locateCenterOnScreen(
                icon_template,
                confidence=confidence,
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
    print(f"✔成功！图片坐标是：{icon_center}")
    return icon_center

def imageJudge(icon_template, confidence=0.88, timeout=4):
    """图像识别判断"""
    if not os.path.exists(icon_template):
        print(f"❌ 错误：找不到模板文件 '{icon_template}'")
        print("👉 请将图标截图保存为该文件名，并放在脚本同目录下。")
        exit()

    print("🔎 正在搜索图标...")
    start_time = time.time()
    icon_center = None

    while time.time() - start_time < timeout:
        try:
            # 使用 OpenCV 进行模板匹配（需 opencv-python）
            icon_center = pyautogui.locateCenterOnScreen(
                icon_template,
                confidence=confidence,
                grayscale=False  # 设为 True 可提速，但可能降低准确率
            )
            if icon_center is not None:
                break
        except Exception as e:
            print(f"⚠️ 识别出错: {e}")
        time.sleep(0.5)  # 避免 CPU 占用过高

    # 判断是否找到
    if icon_center is None:
        print(f"不存在图片！执行逻辑")
        return None
    print(f"✔存在图片！图片坐标是：{icon_center}")
    return icon_center
