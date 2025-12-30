class Phone:
    __current_voltage = 0.2

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5G通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5G通话，并设置单核模式进行省电")

phone = Phone()
phone.call_by_5g()


class Phone2019:
    IMEI = None
    producer = "HM"

    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone2019):
    face_id = "10001" # 面部识别

    def call_by_5g(self):
        print("2022年新功能：5g通话")

phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")

class MyPhone(Phone2019,NFCReader,RemoteControl):
    pass

print("武装到牙齿的手机")
phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

class MyPPhone(Phone2019):
    producer = "ITHEIMA"

    def call_by_5g(self):
        print(f"父类的厂商是:{super().producer}")
        super().call_by_4g()
        print("已被覆写")

mypphone = MyPPhone()
mypphone.call_by_5g()

