#  Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #6 Problem 3
#
# Description: This program can test whether the string  entered by user
# is palindrome. 

def test_palindrome(a):
    length=len(a)
    temp=length//2
    a=a.lower()
    first_half=a[0:temp] # Extract first half of the string
    second_half=""      # The second half of the string is not same as first part
                        # even the string is palindrome because they are in reverse
                        # oeder.
                        
    for i in range(-1,-temp-1,-1): # Use a for loop to entract the reverse of 
        second_half+= a[i]         # second half of the string
        
    if first_half==second_half:
        print("The string is palindrome")
        return True
    else:
        print("The string is not palindrome")
        return False

def main():
    a=str(input("Please enter a string: "))
    test_palindrome(a)

main()
    
    
