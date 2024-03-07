# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #4 Problem 1
#
# Description: This program calculate and print the first 12 entries of
# Fibonacci numbers

def task1():
    n1=1
    n2=1
    print("The first 12 Fibonacci numbers are:",n1,n2,end=" ")
    for i in range(1,11):
        n3=n1+n2
        print(n3,end=" ")
        n1=n2 # Pass the value to the preceding one
        n2=n3

def main():
    task1()

main()
