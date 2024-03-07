# Xu Cai (Charles)
# COSI-10A-2, Fall 2021
# Programming Assignment #3 Problem3
#
# Description: This program can print the given output. I divide this output
# into five different parts. Each part has its own pattern. 

def task3():
        for i in range(5,-1,-1):
            print("*"*i,end="")
            print(" "*(5-i),end="")
            print("//"*i,end="")
            print("\\\\"*(5-i),end="")
            print(" "*(5-i),end="")
            print("*"*i)

def main():
        task3()

main()

    
