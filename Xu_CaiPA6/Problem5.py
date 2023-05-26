#  Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #6 Problem 5
#
# Description: This program can encode the string entered by rotating the string
# by a given amount to Caesar cipher

def Caesar_cipher(message,amount_to_rotate):
    for s in message:
        num=ord(s)
        if num>=ord("A") and num<=ord("Z"): # Set the range for all uppercase letters
            num+=amount_to_rotate
            if num>ord("Z"):               # Prevent the number exceeds or lower than
                num-=26                    # range of uppercase letters
            elif num<ord("A"):
                num+=26

        elif num>=ord("a") and num<=ord("z"): # Set the range for all lowercase letters
            num+=amount_to_rotate
            if num>ord("z"):                  # Same purpose 
                num-=26
            elif num<ord("a"):
                num+=26

        print(chr(num),end="")

def main():
    message=str(input("Enter message needed to be encoded:"))
    amount_to_rotate=int(input("Enter an amount by which to rotate each letter:"))
    Caesar_cipher(message,amount_to_rotate) # Use of parameter

main()
    
        
    
