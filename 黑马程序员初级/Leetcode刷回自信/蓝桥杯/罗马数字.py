import sys
# """
# 3
# IV
# VII
# XL
#
# """
# n = int(input())
# dic = {
#     'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
# }
# for i in range(n):
#     chars = input()
#     lst1 = [dic[char] for char in chars]
#     # print(lst1)
#     p = 0
#     rst = 0
#     while p < len(lst1) - 1: # XCIII len=5
#         if lst1[p] < lst1[p+1]:
#             rst -= lst1[p]
#         else:
#             rst += lst1[p]
#         p += 1
#     rst += lst1[p]
#
#     print(rst)


# 'you   and    me     what    cpp2005program'
# lst = list(input().split())
# lst2 = []
# for char in lst:
#     char = list(char)
#     char[0] = char[0].upper()
#     char = ''.join(char)
#     lst2.append(char)
# chars = ' '.join(lst2)
# lst3 =list(chars)
# # print(lst3)
#
# p = 1
# while p < len(lst3):
#     # 加下划线
#     if lst3[p-1].isalpha() and lst3[p].isdigit():
#         lst3.insert(p,'_')
#     elif lst3[p-1].isdigit() and lst3[p].isalpha():
#         lst3.insert(p,'_')
#
#     p+=1
#
# chars = ''.join(lst3)
# print(chars)


# mag = list(input())
# let = list(input())
# dic = {}
# for char in mag:
#     if char not in dic:
#         dic[char] = 0
#     dic[char] += 1
#
# dic2 = {}
# for char in let:
#     if char not in dic2:
#         dic2[char] = 0
#     dic2[char] += 1
#
# try:
#     needchar = list(dic2.keys())
#     for char in needchar:
#         if dic[char] - dic2[char] < 0:
#             print('NO')
#             exit()
# except KeyError as e:
#     print('NO')
# else:
#     print('YES')

"you know"
lst = input().split()
chars = ''.join(lst)
print(len(chars))
