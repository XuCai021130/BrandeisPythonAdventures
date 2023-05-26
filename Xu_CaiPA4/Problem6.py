# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #4 Problem 6
#
# Description: This program is similiar to problem 5, but this time the height
# of the figure is only 4.

def task6():
    for height in range(1,5):
        print("\\\\"*(height-1),end="") 
        print("!"*(14-(height-1)*4),end="")
        print("//"*(height-1))

def main():
    task6()

main()
    
