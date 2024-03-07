# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #4 Problem 2
#
# Description: This program utilize nested for loop to print * with slope.


def task2():
    for line in range(1,6): # This for loop determines how many lines needed
        for i in range(1,line+1): # This for loop determines how many "*" will                             
            print("*",end=" ")     # be printed in one line
        print()

def main():
    task2()

main()



