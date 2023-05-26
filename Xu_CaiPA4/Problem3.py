# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #4 Problem 3
#
# Description: This program will print given output

def task3():
    for line in range(5,0,-1): # Since the first line contain most and last line
        for i in range(line,0,-1):  # contains least number of *, I choose start
            print("*",end=" ") # the for loop with maximun
        print()

def main():
    task3()

main()
        
    
