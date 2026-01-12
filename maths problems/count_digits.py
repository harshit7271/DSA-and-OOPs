def CountDigit(num):
    return len(str(num))


num = 788756764353
print(CountDigit(num))
# output : 12

# Another way


def CountNum(num1):
    count = 0
    while num1 > 0:
        num1 = num1//10
        count += 1
    return count
# Output : 5


num1 = 21653
print(CountNum(num1))
