"""贪心算法"""
def group_by_first_letter(words: list) -> dict:
    """
    构造26个字母桶，分别装入
    :param words: 输入一个字母列表
    :return: 字典，键是首字母，值是包含相同首字母单词的列表
    """
    groups = {}
    for word in words:
        first_char = word[0]
        if first_char not in groups:
            groups[first_char] = []
        groups[first_char].append(word)
    return groups

n = int(input())
i = 1
raw_list = []
while i <= n:
    raw_list.extend(input().split())
    i+=1
# print(raw_list)

i = 1
sec_list = []
while i < len(raw_list):
    sec_list.append(raw_list[i])
    i += 2
# print(sec_list)

"""输入处理完成"""
count = len(sec_list)


for word in sec_list:
    correct = False

    if len(word) != count:
        continue

    correct = True
    match_list = sec_list.copy()
    match_list.remove(word)

    dic = group_by_first_letter(match_list)
    # print(dic)

    final_list = [word]
    i = 1

    while i < count:
        if word[i] in dic and dic[word[i]]:
            final_list.append(dic[word[i]][0])
            dic[word[i]].pop(0)
            i += 1
        else:
            correct = False
            break

    if correct:
        break


chars = " ".join(final_list)
print(chars)



"""
4
2 IS
4 WINE
8 EMULATOR
3 NOT
"""

"""
7
5 CLONECC
5 CLOSECC
5 CCCPCCC
5 CCCCCCC
5 CDEFGCC
5 CLLLECC
5 CCCCCCC
"""

"""
3
3 GNU
3 NOT
4 UNIX
"""