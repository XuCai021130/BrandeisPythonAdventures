# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #7 Problem 1
#
# Description: This program is a guessing number game. After user enters a answer,
# computer will tell you whether the actual answer is higher or lower your answer
# After each game, you can choose whether or not play it again. When you exit the
# game, computer will give you a report about the overall results.

import random

def guess_number_game():
    max = 200
    answer = random.randint(1,max)
    print("\nI'm thinking of a mumber between 1 and",max,"...")
    total_game = 1
    guesses = 0
    
    while True:
        user_answer=int(input("Your guess? "))

        if user_answer > answer:  # Give user hint if the answer is not correct
            print("it's lower")
            guesses+=1
            
        elif user_answer < answer:
            print("It's higher")
            guesses+=1
        else:
            guesses+=1 # Address special case when user got right answer in one attempt
            if guesses!=1:
                print("You got it right in",guesses,"guesses")
                return guesses
            else:
                print("You got it right in 1 guesses")
                return 1                             

def Overall_results(total_game,total_guesses,best_game): # This function can print the results of the game
    print("\nOverall results:")
    print("Total games   = ",total_game)
    print("Total guesses = ",total_guesses)
    print("Guesses/Game  = ",round(total_guesses/total_game,1))
    print("Best game     = ",best_game)

def main():
    print("Welcome come to the fantastic guessing number game!")
    total_game = 0 # count number of games, number of guesses, and best game
    total_guesses = 0
    best_game = guess_number_game()
    total_game += 1
    total_guesses += best_game

    while True:
        decision = str(input("Do you want to play again?"))
        decision = decision.lower()
        if decision.startswith("y"):  
            count=guess_number_game()
            total_game += 1
            total_guesses += count
            if count < best_game:
                best_game = count
        else:
            Overall_results(total_game,total_guesses,best_game) # If user decide not to play the game, print the overall statistics
            return
        
main()
            
