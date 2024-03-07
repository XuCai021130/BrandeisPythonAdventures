#  Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #6 Problem 2
#
# Description: This program can print a string that have same characters as user
# input but each character repeated the same number of times as the multiplier
# user entered

def task2(a,times):
    print("I got: ",end="")
    for s in a:                # I user nested for loop here. The first for loop
        for i in range(times): # is used to separate each character in the string
            print(s,end="")    # and second for loop is to print each character
                               # with number of times user entered

def main():
    a=str(input("Please enter a String: "))
    times=int(input("Please enter a multiplier for each character to repeat: "))
    task2(a,times)

main()
