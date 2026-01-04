# LETS REVERSE ALL THE ELEMENTS

from array import *

val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
reversedArray = val[::-1]
for i in range(0, len(reversedArray)):
    print(reversedArray[i], end=" ")
