n = 1
save1 = set()
for n in range(1,101):
    num1 = 3 * pow(n,6) + 26 * pow(n,4) + 33 * pow(n,2) + 1
    for k in range(1,101):
        if num1 % k == 0:
            save1.add(k)
print(save1)

"""{1, 3, 7, 9, 13, 19, 21, 27, 29, 31, 39, 49, 57, 59, 63, 71, 81, 83, 87, 91, 93}"""