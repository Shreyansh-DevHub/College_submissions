# Write a function that returns two values swapped.
def swapped(a, b):
    return b, a


num = input("Input any 2 character long value: ")

a, b = swapped(num[0], num[1])
print("swapped values", a, b)
