from array import *

val = array('i', [1, 2, 3, 4, 5, 6])
for i in range(0, len(val)):
    print(val[i], end=" ")

print('\n')

for x in val:
    print(x, end=' , ')

print("\n")

print(val.typecode)

print("\n")

val.reverse()
for i in range(0, len(val)):
    print(val[i], end=" ")

print("\n")

val.insert(1, 50)
val.append(100)
val[3] = 150        # overwrite at 4th place digit
for i in range(len(val)):
    print(val[i], end=" ")


print('\n')

# Copying Array
copyArray = array(val.typecode, (x for x in val))
print(f"copied array = {copyArray}")

print('\n')

# another way
array2 = array(val.typecode, (x for x in val))
for i in range(len(val)):
    print(array2[i], end=" ")
