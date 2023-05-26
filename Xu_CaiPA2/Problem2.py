# Xu Cai (Charles)
# COSI-10A-2, Fall 2021
# Programming Assignment #2 Problem2
miles=float(input("Please enter a length in miles"))
#Utilize integer devision to get rid of digits after two decimal places
kilometers=miles*1.609344*100//1/100
print(miles,"miles equals to",kilometers,"kilometers")
