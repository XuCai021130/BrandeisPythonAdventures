# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #4 Problem 7
#
# Description: This program requiires the user enters a positive integer n. Then
# the program will print number from 1 to n with square brackets.

def task7():
    n=int(input("Please enter a positive integer:"))
    for i in range(1,n+1):
        print("[",i,"]",end=" ") # Adding square brackets to integer i and print

def main():
    task7()

main()

