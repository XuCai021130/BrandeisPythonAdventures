# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #4 Problem 8
#
# Description: This program requires the user to enter two integers for base and
# exponent. Then the programm will print from base 0 to base exponent. 

def task8(): 
    base=int(input("Please enter an integer indicating the base:"))
    exponent=int(input("Please enter a positive integer indicating the exponent:"))
    for i in range(0,exponent+1):
        print(base**i,end=" ") # Calculate the result and print it

def main():
    task8()

main()
