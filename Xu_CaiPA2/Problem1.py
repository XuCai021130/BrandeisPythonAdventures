# Xu Cai (Charles)
# COSI-10A-2, Fall 2021
# Programming Assignment #2 Problem1
price=int(input("Please enter the price of item\n(from 25 cents to a dollar, in 5-cent increments):"))
change=100-price
#Utilize integer devision to get how many quarter to be dispensed.
quarter=change//25
#If necessary, calculate amount of dime   
dime=(change-(quarter*25))//10
#If necessary, calculate amount of nickel 
nickel=(change-(quarter*25)-(dime*10))//5
print("Your item costs",price,"and you paid a dollar")
print("Below is your change:")
print("quarter:",quarter)
print("dime：",dime)
print("nickel：",nickel)
