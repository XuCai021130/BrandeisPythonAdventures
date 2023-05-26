# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #5 Problem 2
#
# Description: In this program,user will enter a positive number. This number will
# be processed in a rule that If the value is even, halve it.
# If it's odd, multiply by 3 and add 1.
# Repeat this process until the value is 1, printing out each value.  finally
# print how many times of calculations performed. 

def task2():
    value=int(input("Initial value is: "))
    if value<1:
        print("Error")
        return 0
    count=0
    for i in range(200):
        if (value%2==0):
            value//=2
            print("Next value is:",value)
            count+=1
        elif (value%2==1 and value!=1): #Since 1 is also a odd number, we need 
            value=value*3+1             # to exclude it from other odd number
            print("Next value is:",value)
            count+=1

        elif (value==1):
            print("Final value 1, number of operations performed", count)
            return 0  # when value is 1, stop the for loop by return

def main():
    task2()

main()
            
        
        
        
        
            
            
