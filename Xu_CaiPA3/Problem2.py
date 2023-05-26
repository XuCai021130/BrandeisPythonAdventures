# Xu Cai (Charles)
# COSI-10A-2, Fall 2021
# Programming Assignment #3 Problem2
#
# Description: This program can calculate factorial of a positive integer
# that user input. For loop is a good choice.

def task2():
        number=int(input("Enter a number:"))
        result=1
        for a in range(1,number+1):
                result*=a
        print(number,end="")
        print("! =",result)

# Since this task asks for three integers, I call task2 function three times
def main():                     
        task2()
        task2()
        task2()

main()



	
