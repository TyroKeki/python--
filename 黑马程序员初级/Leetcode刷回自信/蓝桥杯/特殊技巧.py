input_data = [int(x) for x in input().split()]
"""
等价于input_data = list(map(int,input().split()))
"""

# 示例5：快速生成斐波那契数列（不要使用）
n = 10
fib = [0,1]
[fib.append(fib[-1]+fib[-2]) for _ in range(n - 2)]

# 生成循环索引
n = 5
for i in range(n * 2):
    idx = i % n
    print(idx,end=" ")

# 生成二维坐标
rows, cols = 2,3
grid = [[(i,j) for i in range(cols)] for j in range(rows)]