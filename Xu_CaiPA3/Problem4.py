# Xu Cai (Charles)
# COSI-10A-2, Fall 2021
# Programming Assignment #3 Problem4
#
# Description: This program requires the user enter row number and column number
# Then the program will print a grid of integers from 1 to (rows*columns)

def task4():
    rows=int(input("Please enter a number:")) # Nested for loop is needed
    columns=int(input("Please enter second number:"))
    for a in range(1,rows+1):
        for b in range(1,columns+1):
            print(a+rows*(b-1),end="\t")
        print()

def main():
    task4()

main()
