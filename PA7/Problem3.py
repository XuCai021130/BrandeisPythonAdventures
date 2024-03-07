# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #7 Problem 3
#
# Description: This program requires the user to enter a list with integers. Then the computer
# can return a new list with replacing each pair of integers with their sum.


def collapse(list):
    collapsed_list=[]
    for i in range(0,len(list)-1,2):
        new_integer=list[i]+list[i+1] # Add the adjacent pairs together and form a new integer stored in the new list
        collapsed_list.append(new_integer)
    if len(list)%2==1: # If there are odd number of entries in the list, add the last one to the new list
        collapsed_list.append(list[-1])
    print(collapsed_list)



def main():
    list1=[]
    for i in input("Please enter the first list and separated each integer by space: ").split(" "):
        list1.append(int(i))
    collapse(list1)
main()
