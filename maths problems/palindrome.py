def reverseNumber(num):
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = reversed_num*10 + remainder
        num = num//10
    return reversed_num


def is_palindrome(pal):
    return pal == reverseNumber(num)


num = 121
reversed_num = is_palindrome(num)
print(reversed_num)
