import sys

# 快速读入
input = lambda: sys.stdin.readline().strip()
input = sys.stdin.readline

# 示例1：单行多个整数
a,b,c = map(int,input().split())
print(a,b,c)

# 示例2：多行多个整数
n = int(input())
lst = [int(input()) for _ in range(n)]
print(lst)

# 示例3：矩阵输入
n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
print(matrix)

# 示例4：标准矩阵
matrix1 = [[0] * 5 for _ in range(5)]
matrix2 = [[0 for _ in range(5)] for _ in range(5)]

# 示例5.1：二维列表变一维
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
flatten = [x for row in matrix for x in row]

# 队列
from collections import deque
x = 1145
q = deque([1,2,3])
q.append(x)
print(q)
x = q.popleft()

stk = []
stk.append(x)
tmp1 = stk[-1]
tmp2 = stk.pop()

