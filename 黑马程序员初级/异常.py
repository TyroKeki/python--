try:
    print(e)
except Exception as e:
    print(f"异常是：{e}")
else:
    print("好高兴，没有出现异常")
finally:
    print("无论如何都要执行")