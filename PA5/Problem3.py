# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #5 Problem 3
#
# Description: This program can generate the roman numeral of a positive integer
# that user input range fromm 1 to 4999

def Roman_Numerals():
    a=int(input("Enter a positive integer number (not bigger than 4999):"))
    b=a//1000  # Split the number of digits
    c=a//100%10
    d=a%100//10
    e=a%10
    if b==1:   # Assign roman numerals for digits
        print("M",end="")
    elif b==2:
        print("MM",end="")
    elif b==3:
        print("MMM",end="")
    elif b==4:
        print("MMMM",end="")

    if c==1:                
        print("c",end="")
    elif c==2:
        print("CC",end="")
    elif c==3:
        print("CCC",end="")
    elif c==4:
        print("CD",end="")
    elif c==5:
        print("D",end="")
    elif c==6:
        print("DC",end="")
    elif c==7:
        print("DCC",end="")
    elif c==8:
        print("DCCC",end="")
    elif c==9:
        print("CM",end="")

    if d==1:
        print("X",end="")
    elif d==2:
        print("XX",end="")
    elif d==3:
        print("XXX",end="")
    elif d==4:
        print("XL",end="")
    elif d==5:
        print("L",end="")
    elif d==6:
        print("lX",end="")
    elif d==7:
        print("LXX",end="")
    elif d==8:
        print("LXXX",end="")
    elif d==9:
        print("XC",end="")

    if e==1:
        print("I")
    elif e==2:
        print("II")
    elif e==3:
        print("III")
    elif e==4:
        print("IV")
    elif e==5:
        print("V")
    elif e==6:
        print("VI")
    elif e==7:
        print("VII")
    elif e==8:
        print("VIII")
    elif e==9:
        print("IX")

    


def main():
    Roman_Numerals()

main()
    
    
        
