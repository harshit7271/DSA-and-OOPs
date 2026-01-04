from array import *

val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

newArray = val[2: 6]

for i in range(0, len(newArray)):
    # slicing 3,4,5,6 from val arary and storing it in newArrray
    print(newArray[i], end=" ")


# LETS REVERSE ALL THE ELEMENTS

reversedArray = val[::-1]
for i in range(0, len(reversedArray)):
    print(reversedArray[i], end=" ")
