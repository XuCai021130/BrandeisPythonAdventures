#  Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #6 Problem 1
#
# Description: This program requires user to input a positive number, then  the
# number will be processed by a rule that if the number is odd and not 1, multiply by 3
# and add 1, if the number is even, halve it, if the number is 1. stop the program
# and print how many times performed

def task1(value):
    count=0
    if value<1: # Remind if user enters a number less than 1
        print("Error")
        return

    while value!=1:
        if (value%2==0):
            value//=2
        elif (value%2==1): 
            value=value*3+1
        count+=1 # After each calculation, count will increase 1 to record one
                 # calculation is finished
        if value==1:           # When the value is 1, we don't need to print what is the next value
            print("Final value 1,",end="")
        else:
            print("Next value is:",value)
    print(" number of operations performed", count)

def main():
    value=int(input("Initial value is: "))
    task1(value)


main()
        
