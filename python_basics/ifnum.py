#program to demonstrate how if works (with numbers)
print('compare two numbers')
a = input("Enter a number (a): ")
b = input("Enter a number (b): ")

print('a =', a)
print('b =', b)
print('\n')
if ((type(a) == int and type(b) == int) or
    (type(a) == float and type(b) == float)):
    if a > b:
        print('a is greater than b')
    elif a < b:
        print('a is less than b')
    else:
        print('a is equal to b')
else:
    print('a and b must be integers(numerical)')
