# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #4 Problem 10
#
# Description: Thhis program helps you to annual balance with the given interest
# of 0.65%

def task10():
    years=int(input("For how many years do you want to save?"))
    print("Year","Curr Balance","Interest","New Deposit","New Balance",sep="\t")
    current_balance=1000
    new_deposit=100.0
    for i in range(0,years):
        interest=current_balance*0.0065*100//1/100 # Ensure only two decimal places
        new_balance=(current_balance + new_deposit + interest)*100//1/100
        print(i,current_balance,interest,new_deposit,new_balance,sep="      ")
        current_balance=new_balance
       


def main():
    task10()

main()

