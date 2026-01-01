import re
import os

class 课程处理类:
    # count = 0
    #
    # def __init__(self,count=0):
    #     self.count = count

    def 自动课时统计器(self,addr):
        '''
        黑马程序员-163课时+1 17已完成
        目前课时-163+1 50已完成
        这个鲁棒性高
        :return:
        '''
        finished = 0
        unfinished = 0
        with open(addr, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if len(line) > 5 and re.search(r'\d', line):
                    if line.startswith('V'):
                        finished += 1
                    else:
                        unfinished += 1
                        # print(line)
            print(f"已完成的课时有：{finished}\n"
                  f"未完成的课时有：{unfinished}\n")

    def 视频时间去除(self):
        last_digit = 0
        count = 0
        max_str_length = 0
        with open(r'C:\Users\13726\Desktop\课程计划草稿.txt', 'r', encoding='utf-8') as fread:
            with open(r'C:\Users\13726\Desktop\中间1.txt', 'w', encoding='utf-8') as fwrite:
                for line in fread:
                    line = line.strip()
                    if len(line) > 5 and re.search(r'\d', line):
                        '''侦测最大一行字符数'''
                        str_length = len(line)
                        if max_str_length < str_length:
                            max_str_length = str_length


                        # Bug1 要在任务处理完换行
                        # fwrite.write(line + '\n')

                        # Optimization1 不用复杂正则
                        # it = re.search(r'-(?P<digit>\d*?)-', line)
                        # digit = int(it.group('digit'))

                        # Bug2 后面的视频标题格式不匹配
                        # parts = line.split('-')
                        # digit_str = parts[2]
                        # digit = int(digit_str)

                        digit = None
                        for part in line.split('-'):
                            p = part.strip()
                            if p.isdigit():
                                digit = int(p)

                        # 检测的工作做完再写入
                        if digit < last_digit:
                            fwrite.write('\n')
                        fwrite.write(line + '\n')
                        count += 1
                        last_digit = digit
        print('第一次计入条数：',count)
        print('最大字符数：',max_str_length)
        self.更改V的位置添加F()


    def 更改V的位置添加F(self):
        count = 0
        with open(r'C:\Users\13726\Desktop\中间1.txt', 'r', encoding='utf-8') as fread:
            with open(r'C:\Users\13726\Desktop\黑马程序员python入门.txt', 'w', encoding='utf-8') as fwrite:
                for line in fread:
                    if line != '\n':
                        line = line.strip()
                        # Warning1 容易将标题替换成空格，一定不能出现空格（已修复）
                        if line.endswith('V'):
                            line = line[:-1:1].strip()
                            fwrite.write('V\t')
                            fwrite.write(line + '\n')
                            count += 1

                        else:
                            fwrite.write('F\t')
                            fwrite.write(line + '\n')
                            count += 1
                    else:
                        fwrite.write('\n')

        os.remove(r'C:\Users\13726\Desktop\中间1.txt')
        print('第二次计入条数：',count)


addr_to_count1 = r'C:\Users\13726\Desktop\黑马程序员python入门.txt'
addr_to_count2 = r'C:\Users\13726\Desktop\课程计划草稿.txt'

开始 = 课程处理类()
# 开始.视频时间去除()
开始.自动课时统计器(addr_to_count1)