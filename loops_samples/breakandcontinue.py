#program demonstrates break and continue

def main():
    #initialize variables
    count = 0
    #print a message
    print("This program counts from 0 to 9 using a for loop but eliminates numbers using break and continue")
    #for loop
    for count in range(10):
        #print the count
        print(count)
        #check if the count is even
        if count % 2 == 0:
            #skip the rest of the loop
            continue
        #check if the count is greater than 5
        if count > 5:
            #break out of the loop
            break
    #print a message
    print("Done")
    
if __name__ == "__main__":
    main()