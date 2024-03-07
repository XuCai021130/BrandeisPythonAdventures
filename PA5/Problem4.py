# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #5 Problem 4
#
# Description: This program can find how many days until user1 and user2's birthday
# and tell you who's birthday is sooner compared to today.

def days_in_month(a): # This function tells you the date in a month
    days=0
    if (a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12):
        days+=31
    elif (a==4 or a==6 or a==9 or a==11):
        days+=30
    elif a==2:
        days+=28
    return days

def day_in_a_year(month,day): # This function tells you the order of days in a year
    for i in range(1,month):
        day+=days_in_month(i)
    return day

def task4():
    m1=int(input("Enter birth month for user1:"))
    day1=int(input("Enter birth day for user1:"))
    m2=int(input("Enter birth month for user2:"))
    day2=int(input("Enter birth day for user2:"))
    today_month=int(input("Enter today's month"))
    today_days=int(input("Enter today's date"))
    day_in_a_year1=day_in_a_year(m1,day1)
    day_in_a_year2=day_in_a_year(m2,day2)
    day_in_a_year3=day_in_a_year(today_month,today_days)

    remain1=day_in_a_year1-day_in_a_year3 
    if remain1<0:  # Smaller than 0 means user has had her birthday,
        remain1+=365  # so we need to add another year otherwise it is negative
    if remain1==0:
        print("Today is uer1's birthday")
    print("User1's birthday is",remain1,"days later")
    
    remain2=day_in_a_year2-day_in_a_year3 # Same way for comparing user2
    if remain2<0:
        remain2+=365
    if remain2==0:
        print("Today is uer2's birthday")
    print("User2's birthday is",remain2,"days later")

    if remain1>remain2:     # Larger remaining days means birthday will come later
        print("User2's birthday is sooner")
    elif remain1<remain2:
        print("User1's birthday is sooner")
    else:
        print("They have the same birthday")

def main():
    task4()

main()
    
