"""
import sys

input = lambda : sys.stdin.readline().strip()
chars = input()
n = int(input())
lst = [input() for _ in range(n)]
# print(lst)
for word in lst:
    cnt = chars.count(word)
    print(cnt)
# 错误示范
"""


"""
bluemooninthedarkmoon
3
moon
blue
dark
"""

s = input()
n = int(input())
while n>0:
    p = input()
    cnt = 0
    for i in range(len(s) - len(p) + 1):
        if p == s[i:i+len(p)]:
            cnt += 1
    print(cnt)
    n-=1