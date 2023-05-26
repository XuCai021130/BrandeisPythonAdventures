#  Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #6 Problem 6
#
# Description: This program is a simple Rock Paper Scissor game. User can play this game with computer.
# It contains two different strategies for user to choose. And user can stop the game whenever they want

import random
import time

def strategy1(): # Strategy is simple. The computer will randomly make choice between rock paper and scissor
    user_choice=0
    tie=0 #Count how many times user win, lose or tie
    win=0
    lose=0
    while user_choice!= -1:
        user_choice=int(input('Make a decision(0 for Rock, 1 for Paper, 2 for Scissor):'))
        computer_choice=random.randint(0,2)

        if user_choice==0:
            user="Rock"
        elif user_choice==1:
            user="Paper"
        elif user_choice==2:
            user="Scissor"
        elif (user_choice>2 or user_choice<0) and user_choice!=-1: # If user enters invalid value, remind user and reenter proper value
            user_choice=int(input("Please enter a integer between 0-2 or enter -1 to quit the game:"))
        else:                           # Quit this game when user enters -1
            print("You played total",tie+win+lose,"games.\nYou wins",win,"times,\nlose",lose,"times\nand tie",tie,"times")
            print("\nYour winning rate is",win/(tie+win+lose)*100,"%")
            print("See you next time!")
            return             
        
        if computer_choice==0:           # Assign rock, paper, scissor to different numerical values
            computer="Rock"
        elif computer_choice==1:
            computer="Paper"
        else:
            computer="Scissor"
            
        time.sleep(0.5)                  # Slow down the process of game, making this program more like a real game

        print("Your choose",user,"and computer choose",computer,end=" ") # determines who wins by the rule of rock paper scissor game
        if user_choice==computer_choice:
            print("\nIt's a tie!")
            tie+=1
        elif (user_choice==0 and computer_choice==2) or (user_choice==1 and computer_choice==0) or (user_choice==2 and computer_choice==1):
            print("\nYou win!")
            win+=1

        elif (user_choice==0 and computer_choice==1) or (user_choice==1 and computer_choice==2) or (user_choice==2 and computer_choice==0):
            print("\nComputer win!")
            lose+=1

def strategy2():   # Strategy2 is bit more better.
    user_choice=0
    computer_choice=random.randint(0,2)
    tie=0
    win=0
    lose=0
    total=tie+win+lose
    while user_choice!= -1:
        user_choice=int(input('Make a decision(0 for Rock, 1 for Paper, 2 for Scissor):'))

        if user_choice==0:
            user="Rock"
        elif user_choice==1:
            user="Paper"
        elif user_choice==2:
            user="Scissor"
        elif (user_choice>2 or user_choice<0) and user_choice!=-1: # If user enters invalid value, remind user and reenter proper value
            user_choice=int(input("Please enter a integer between 0-2 or enter -1 to quit the game:"))
        else:                           # Quit this game when user enters -1
            print("You played total",tie+win+lose,"games.\nYou wins",win,"times,\nlose",lose,"times\nand tie",tie,"times")
            print("\nYour winning rate is",win/(tie+win+lose)*100,"%")
            print("See you next time!")
            return             
        
        if computer_choice==0:           # Assign rock, paper, scissor to different numerical values
            computer="Rock"
        elif computer_choice==1:
            computer="Paper"
        else:
            computer="Scissor"
            
        time.sleep(0.8)        # Slow down the process of game, making this program more like a real game

        print("Your choose",user,"and computer choose",computer,end=" ")
        
        if user_choice==computer_choice: # determines who wins by the rule of rock paper scissor game
            print("\nIt's a tie!")
            computer_choice=random.randint(0,2)
            tie+=1

        elif user_choice==0 and computer_choice==2:  # These three elif statement happened when computer loses the game
            print("\nYou win!")                      # In order to icnrease the chance to win, computer will choose the 
            computer_choice=1                        # one that can defeat user's choice
            win+=1
        elif user_choice==1 and computer_choice==0:
            print("\nYou win!")
            computer_choice=2
            win+=1
        elif user_choice==2 and computer_choice==1:
            print("\nYou win!")
            computer_choice=0
            win+=1

        elif user_choice==0 and computer_choice==1:  
            print("\nComputer win!")                     
            computer_choice=random.randrange(0,3,2)
            lose+=1
        elif user_choice==1 and computer_choice==2:
            print("\nComputer win!")
            computer_choice=random.randint(0,1)
            lose+=1
        elif user_choice==2 and computer_choice==0:
            print("\nComputer win!")
            computer_choice=random.randint(1,2)
            lose+=1
    
   
def main():
        print("Wlecome to Rock, Paper, Scissor game!")
        choosing_strategy=int(input("Please choose the difficulty of this game\nEnter 1 for easier level and 2 for harder level:")) # Give user two level to choose
        if choosing_strategy==1: 
            strategy1()
        elif choosing_strategy==2:
            strategy2()
        else:
            return 
            
    

main()

            
            
    
