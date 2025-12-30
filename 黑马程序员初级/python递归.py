#累乘递归
def multiply(n:int) -> int:
    if n == 1 or n == 0:
        return 1
    return n * multiply(n-1)

# n = int(input())
# result = multiply(n)
# print(result)


# 斐波那契第n项的值 递归 1 1 2 3 5 8 13 21 34 55 89 144
def fei(An):
    if An == 1 or An == 2:
        return 1
    elif An >= 3:
        return fei(An-1)+fei(An-2)

# n = int(input())
# result = fei(n)
# print(result)


#所有二进制数
def binary(n,s=''):
    if len(s) == n:
        print(s)
        return
    binary(n,s + '1')
    binary(n,s + '0')

# binary(n=4)


#所有排序
def char_sort(chars,after_char_sort = ''):
    if not chars:
        print(f"这是结果：{after_char_sort}")

    for char in chars:
        new_after_char_sort = after_char_sort + char
        new_chars = chars.replace(char,'')
        # print(f"这是还未排序的：{new_chars},这是排序完成的：{new_after_char_sort}")
        char_sort(new_chars,new_after_char_sort)

# char_sort("abcde")


#递归大神
'''复杂度爆炸'''
# import copy
#
# def easy_full_permutation(waiting_list,after_permutation=[],result = []):
#     if not waiting_list:
#         # print(f"{after_permutation}")
#         status = checker(after_permutation)
#         if status:
#             output =  ' '.join(after_permutation)
#             print(output)
#
#
#     for word in waiting_list:
#         new_after_permutation = after_permutation + [word]
#
#         new_waiting_list = copy.copy(waiting_list)
#         new_waiting_list.remove(word) #只删除一次，不保证正确
#
#         easy_full_permutation(new_waiting_list,new_after_permutation)
#
# def checker(waiting_list):
#     first_word = list(waiting_list[0])
#     # print(first_word)
#
#     #判断首字母能否组成第一个单词
#     i = 0
#     for char in first_word:
#         if char != waiting_list[i][0]:
#             return False
#         i += 1
#     return True
#
#
#
# num1 = int(input())
# chars_list = []
# for i in range(num1):
#     chars_list.extend(map(str,input().split()))
# # print(num1,chars)
#
# i = 1
# new_chars_list = []
# while i <= num1*2:
#     new_chars_list.append(chars_list[i])
#     i += 2
# # print(new_chars_list)
# easy_full_permutation(new_chars_list)
#
#
# # # print(need_to_process)
# #
# # for element in need_to_process:
# #     stats = checker(element)
# #     if stats:
# #         output =  ' '.join(element)
# #         print(output)
#
# def list_to_str(waiting_list):
#     return ' '.join(waiting_list)

