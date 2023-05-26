# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #7 Problem 2
#
# Description: This program can test whether the list user entered is sorted.

def is_sorted(list):

    for i in range(1,len(list)):
        if list[i] < list[i-1]: # Test whether the latter is smaller than the former, as long as one pair of integers satisfy, this list cannot be sorted
            print("The list is not sorted")
            return False
        
    print("The list is sorted")
    return True

def main():
    list1=[]
    for i in input("Please enter the list and separated each integer by space: ").split(" "):
        list1.append(float(i))
    is_sorted(list1)
    
    
    

main()
    
    
