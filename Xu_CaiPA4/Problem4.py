# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #4 Problem 4
#
# Description: This program utilize nested for loop to print *


def task4():
    for line in range(1,6): # This for loop determines how many lines needed
        for empty_space in range(0,5-line): # This for loop determines how many
            print(" ",end=" ")               # empty space needed
        for character in range(0,line): # This for loop determines how many *
            print("*",end=" ")           # needed
        print()

def main():
    task4()

main()



