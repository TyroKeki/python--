from functools import reduce

def test_func(compute):
    result = compute(1,2)
    print(result)

# def compute(x,y):
#     return x+y
#
# test_func(compute)

# test_func(lambda a,b: a+b)

# n = int(input())
# total = reduce(lambda x,y:x*y,range(1,n+1,1))
# print(total)

# def docu(a,b):
#     '''
#     这个函数用来测试python文本功能
#     :param a: 这个是参数a
#     :param b: 这个是参数b
#     :return: 返回None
#     '''
#     print(a,b)
# docu

