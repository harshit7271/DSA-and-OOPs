from array import *
arr = array('i', [])

n = int(input('Enter the length of array'))

for i in range(0, n):
    arr.append(int(input('Enter next number')))

for x in arr:
    print(x, end=" ")

# Output -
"""
Enter the length of array5
Enter next number1
Enter next number2
Enter next number3
Enter next number4
Enter next number5
1 2 3 4 5
"""
