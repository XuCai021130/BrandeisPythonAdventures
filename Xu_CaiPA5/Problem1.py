# Name Student
# COSI 10a, Fall 2021
# Programming Assignment #5 Problem1
#
# Description: This program can find the maximum and minimum value of
# the integers user input. 

def task1():
    number_of_numbers=int(input("How many numbers do you want to enter?"))
    a=1
    max=min=0
    for i in range(1,number_of_numbers+1):
        print("Number",i,end="")
        number=int(input(": "))

        if a==1:
            max=min=number # When there is only one number input, assume this 
                           # is both maximum and minimun value.
        else:
            if number<min: # if the next value is larger than maximum or
                min=number # smaller than minimun value, replace it
            elif number>max:
                max=number
        a+=1
    print("Smallest =",min)
    print("Largest =",max)

def main():
    task1()

main()
            
        
