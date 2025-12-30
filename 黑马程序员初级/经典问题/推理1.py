

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


def digit_to_letter(digits: list[int]) -> list[str]:
    relation = {0: 'A',
                1: 'B',
                2: 'C',
                3: 'D'}

    answer = []
    for digit in digits:
        answer.append(relation[digit])
    return answer

s = [0,0,0,0,0,0,0,0,0,0]
while len(s) <= 10:
    s[9] += 1
    s = quaternary_converter(s)
    right = [0] * 10

    #Q2
    if   s[1] == 0 and s[4] == 2:
        right[1] = 1
    elif s[1] == 1 and s[4] == 3:
        right[1] = 1
    elif s[1] == 2 and s[4] == 0:
        right[1] = 1
    elif s[1] == 3 and s[4] == 1:
        right[1] = 1
    else:
        continue

    #Q3
    if   s[2] == 0 and s[2] != s[5] == s[1] == s[3]:
        right[2] = 1
    elif s[2] == 1 and s[5] != s[2] == s[1] == s[3]:
        right[2] = 1
    elif s[2] == 2 and s[1] != s[5] == s[2] == s[3]:
        right[2] = 1
    elif s[2] == 3 and s[3] != s[5] == s[1] == s[2]:
        right[2] = 1
    else:
        continue

    #Q4
    if   s[3] == 0 and s[0] == s[4]:
        right[3] = 1
    elif s[3] == 1 and s[1] == s[6]:
        right[3] = 1
    elif s[3] == 2 and s[0] == s[8]:
        right[3] = 1
    elif s[3] == 3 and s[5] == s[9]:
        right[3] = 1
    else:
        continue

    #Q5
    if   s[4] == 0 and s[4] == s[7]:
        right[4] = 1
    elif s[4] == 1 and s[4] == s[3]:
        right[4] = 1
    elif s[4] == 2 and s[4] == s[8]:
        right[4] = 1
    elif s[4] == 3 and s[4] == s[6]:
        right[4] = 1
    else:
        continue

    #Q6
    if   s[5] == 0 and s[7] == s[1] == s[3]:
        right[5] = 1
    elif s[5] == 1 and s[7] == s[0] == s[5]:
        right[5] = 1
    elif s[5] == 2 and s[7] == s[2] == s[9]:
        right[5] = 1
    elif s[5] == 3 and s[7] == s[4] == s[8]:
        right[5] = 1
    else:
        continue

    #Q7
    CA = s.count(0)
    CB = s.count(1)
    CC = s.count(2)
    CD = s.count(3)
    mini = min(CA, CB, CC, CD)
    if   s[6] == 0 and CA == mini:
        right[6] = 1
    elif s[6] == 1 and CB == mini:
        right[6] = 1
    elif s[6] == 2 and CC == mini:
        right[6] = 1
    elif s[6] == 3 and CD == mini:
        right[6] = 1
    else:
        continue

    #Q8
    if   s[7] == 0 and s[0] != s[6]:
        right[7] = 1
    elif s[7] == 1 and s[0] != s[4]:
        right[7] = 1
    elif s[7] == 2 and s[0] != s[1]:
        right[7] = 1
    elif s[7] == 3 and s[0] != s[9]:
        right[7] = 1
    else:
        continue

    #Q9
    if   s[8] == 0 and ((s[0]==s[5] and not s[5]==s[4]) or (not s[0]==s[5] and s[5]==s[4])):
        right[8] = 1
    elif s[8] == 1 and ((s[0]==s[5] and not s[9]==s[4]) or (not s[0]==s[5] and s[9]==s[4])):
        right[8] = 1
    elif s[8] == 2 and ((s[0]==s[5] and not s[1]==s[4]) or (not s[0]==s[5] and s[1]==s[4])):
        right[8] = 1
    elif s[8] == 3 and ((s[0]==s[5] and not s[8]==s[4]) or (not s[0]==s[5] and s[8]==s[4])):
        right[8] = 1
    else:
        continue

    #Q10 final
    D_value = max(CA, CB, CC, CD) - min(CA, CB, CC, CD)
    if   s[9] == 0 and D_value == 3:
        right[9] = 1
    elif s[9] == 1 and D_value == 2:
        right[9] = 1
    elif s[9] == 2 and D_value == 4:
        right[9] = 1
    elif s[9] == 3 and D_value == 1:
        right[9] = 1
    else:
        continue
    break

answer = digit_to_letter(s)
for i,ans in enumerate(answer,1):
    print(f"{ans}, ",end="")

