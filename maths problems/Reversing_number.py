def reverseNum(num):
    ans = 0
    while num > 0:
        ans = ans*10 + num % 10    # remainder = num % 10
        num = num//10
    return ans


print(reverseNum(1234))
