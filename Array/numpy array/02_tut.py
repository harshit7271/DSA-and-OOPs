from numpy import *

val = linspace(10, 20, 5)

for i in val:
    print(i, end=" ")
# it will divide 10 - 20 in 5 parts

print('\n')

val2 = arange(10, 20, 2)

for x in val2:
    print(x, end=" ")
# output : 10 12 14 16 18

print('\n')

val3 = zeros(10)

for y in val3:
    print(y, end=" ")
# output : 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
