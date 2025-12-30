def main():
    while True:
        try:
            user_input = input("请输入一个十进制或十六进制码点 Unicode 码点（输入 'q' 退出）: ").strip()
            if user_input.lower() == 'q':
                print("退出程序。")
                break

            """改进：添加十六进制，自动去掉 U+"""
            set16 = set("ABCDEF")
            set10 = set("0123456789")
            user_input = user_input.lstrip("uU+")
            user_input = user_input.rstrip() # 空格也去了
            if set(user_input.upper()) & set16:
                code_point = int(user_input,16)
            elif "X" in user_input.upper():
                user_input = user_input.strip("Xx")
                code_point = int(user_input,16)
            else:
                code_point = int(user_input)
            # print("这是多少：",code_point)


            # 检查是否在合法 Unicode 范围内
            if not (0 <= code_point <= 0x10FFFF):
                print("错误：Unicode 码点必须在 0 到 1,114,111 (0x10FFFF) 之间。")
                continue

            # 转换为字符
            char = chr(code_point)
            # print("让我看看字符：",char)

            # 获取 UTF-8 编码（字节）
            utf8_bytes = char.encode('utf-8')
            # print("让我看看编码：",utf8_bytes,type(utf8_bytes))

            utf8_hex = ' '.join(f'{b:02X}' for b in utf8_bytes)
            utf8_dec = ' '.join(str(b) for b in utf8_bytes)

            print(f"十进制码点: {code_point}")
            print(f"十六进制码点: U+{code_point:04X}")
            print(f"对应字符: '{char}'")
            print(f"UTF-8 字节（十六进制）: {utf8_hex}")
            print(f"UTF-8 字节（十进制）: {utf8_dec}")
            print("-" * 50)

        except ValueError:
            print("错误：请输入一个有效的整数。")



if __name__ == "__main__":
    main()