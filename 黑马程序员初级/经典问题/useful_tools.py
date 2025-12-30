def quaternary_converter(nums:list[int]) -> list[int]:
    nums.reverse()
    after_sort_nums = []
    carry = 0
    for num in nums:
        num += carry
        carry = 0
        if num >= 4:
            num -= 4
            carry += 1
            after_sort_nums.append(num)
        else:
            after_sort_nums.append(num)
    if carry >= 1:
        after_sort_nums.append(carry)
    after_sort_nums.reverse()
    return after_sort_nums


def decimal_converter(nums:list[int]) -> list[int]:
    nums.reverse()
    after_sort_nums = []
    carry = 0
    for num in nums:
        num += carry
        carry = 0
        if num >= 10:
            num -= 10
            carry += 1
            after_sort_nums.append(num)
        else:
            after_sort_nums.append(num)
    if carry >= 1:
        after_sort_nums.append(carry)
    after_sort_nums.reverse()
    return after_sort_nums


def strtoint_list(listt:list[str]) -> list[int]:
    new_list = []
    for char in listt:
        char = int(char)
        new_list.append(char)
    return new_list

if __name__ == '__main__':
    li = ["1","2","3"]
    print(strtoint_list(li))