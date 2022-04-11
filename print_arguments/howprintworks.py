#program to demonstrate how print works

#normal print
print("Hello World")
print("Hello", "World")

#print with a new line
print("Hello", "World", sep="\n")

#print with a new line and a tab
print("Hello", "World", sep="\t", end="\n")

#print with a '-' as a separator
print("Hello", "World", sep="-")

#cancel the new line
print("Hello", sep = " ", end="")
print("World", end="\n")