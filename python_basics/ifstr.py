#program to demonstrate how if works (with strings)

a = str(input("Enter a str (a): "))
b = str(input("Enter a str (b): "))

if type(a) == str and type(b) == str:
    if a == b:
        print('strings are equal')
    elif a != b:
        print('strings are not equal')
else:
    print('a and b must be strings')