#demonstrate the use of recursion

from itertools import count


def recursion(n):
    print(n)
    if n == 0:
        print("Done")
    else:
        recursion(n-1)
        
    
def main():
    #initialize variables
    count = 10
    #print a message
    print("This program demonstrates recursion")
    #call the function
    recursion(count)
    
if __name__ == "__main__":
    main()
    