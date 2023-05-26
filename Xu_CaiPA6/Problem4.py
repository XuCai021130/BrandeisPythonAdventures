#  Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #6 Problem 4
#
# Description: This program requires user to enter one people's first and last
# name, then the two strings will be converted according to pig latin rule

def pig_latin(first_name,last_name):
    first_name=first_name.lower() # Firstly converts two strings to all lowercase
    last_name=last_name.lower()
    first_name=first_name[1:]+first_name[0]+'ay' # Manipulate the strings according
    last_name=last_name[1:]+last_name[0]+'ay'    # to pig latin rule
    first_name=first_name.capitalize()      # Make the first character capitalized
    last_name=last_name.capitalize()        # for both strings
    print("Under the pig latin rule, your new name is", first_name,last_name)

def main():
    first_name=str(input("Please enter your first name: "))
    last_name=str(input("Please enter your last name: "))
    pig_latin(first_name,last_name)

main()
    
    
