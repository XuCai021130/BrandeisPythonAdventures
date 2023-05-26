# Xu Cai (Charles)
# COSI-10A-2, Fall 2021
# Programming Assignment #3 Problem1
#
# Description: This program can calculate and print the value of zero power of
# two up to the power user input. 

def task1():
        exponent=int(input("Enter a number for exponent:"))
        for i in range(0,exponent+1): # Use for loop to get each value
                print(2**i)

def main():
        task1()

main()


	
