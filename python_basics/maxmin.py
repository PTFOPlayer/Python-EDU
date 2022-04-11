#program to demonstrate how max and min works

a = int(input("Enter a number (a): "))
b = int(input("Enter a number (b): "))
c = int(input("Enter a number (c): "))
d = int(input("Enter a number (d): "))

if ((type(a) == int and type(b) == int and type(c) == int and type(d) == int) or
    (type(a) == float and type(b) == float and type(c) == float and type(d) == float)):

    list = [a, b, c, d]

    print('highest number is:', max(list))
    print('lowest number is:', min(list))
    
else :
    print('a, b, c and d must be integers or floats')