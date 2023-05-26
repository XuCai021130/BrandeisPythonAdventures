# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #4 Problem 9
#
# Description: After the user inter two positive integers, the program will print
# a square with first line fro minimum to maximum and second line start with
# next-higher number

def task9():
    min=int(input("Please enter a minimum integer:"))
    max=int(input("Please enter a maximum integer:"))
    for i in range(min, max+1):
        for j in range(i, max+1): # Print number from i to 7
            print(j,end="")
        for k in range(min,i): # Print number after 7
            print(k,end="")
        print()

def main():
    task9()

main()
        
