# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #4 Problem 5
#
# Description: This program can print given structure by using for loop and
# string multiplication. 

def task5():
    for height in range(1,7): # Set how many lines needed
        print("\\\\"*(height-1),end="")     
        print("!"*(22-(height-1)*4),end="")
        print("//"*(height-1))

def main():
    task5()

main()
    
