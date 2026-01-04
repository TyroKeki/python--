
# words = ["apple", "banana", "kiwi", "cherry"]
# words.sort(key=len)
# print(words)

# li = [[1*5]*5]*5
# li[0][0] = 1
# print(li)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
# flatten = [x for row in matrix for x in row]
# print(flatten)

from collections import deque
q = deque()
q.append(1)
print(q)
x = q.popleft()

stk = []
stk.append(x)
x = stk[-1]
x = stk.pop()

