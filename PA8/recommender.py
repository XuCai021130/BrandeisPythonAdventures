# Xu Cai (Charles)
# COSI 10a, Fall 2021
# Programming Assignment #8
#
# Description: This program will be used to sort a text containing people's
# rating on books. 

def get_data(): # Sort the data and return two list, one is list of books and the other is  people's name and ratings for books
    book=set()
    lines = open("ratings.txt").readlines() # Read the given text
    for i in range(1,len(lines),3):         # Get name of books            
                book.add(lines[i].rstrip())
    book=list(book)
    rating_data={}

    for i in range(0,len(lines),3):
        if lines[i].rstrip() not in rating_data.keys(): # Test whether username is already exist
            rating_data[lines[i].rstrip()]=[0]*len(book)# adding values to key, which is username
        rating_data[lines[i].rstrip()][book.index(lines[i+1].rstrip())]=lines[i+2].rstrip()
    
    return book,rating_data # Return two lists

def averages(): # compute the rating for each book and rank from the highest to lowest
    book=get_data()[0]
    rating_data=list(get_data()[1].values())
    ratings=[]
    for i in range(len(book)): # loop the book 
        total = 0
        count = 0
        for j in range(len(rating_data)):
            if rating_data[j][i]!=0: # Test if the rating is nonzero
                total += int(rating_data[j][i]) # add them together
                count += 1
        if count!=0:
            temp = (total/count,book[len(ratings)]) # calculate the average and store in tuples 
            ratings.append(temp)
    ratings.sort()
    ratings.reverse() # sort and reverse so that ratings will rank from highest to lowest
    for (score,book_name) in ratings: # Print book and its ratings
        print(book_name,score)
    return

def recommendations(): # When typing a username, the system will generate recommended books fore that user
    user_name=input("User?")
    book,rating_data = get_data()
    similarities = []
    if user_name in rating_data.keys():
        
        for user in rating_data.keys():
            similarity=0
            if user != user_name: # If the input user is user itself, we don't need to calculate the similarity score
                for i in range(0,len(book)):
                    similarity += int(rating_data[user_name][i])*int(rating_data[user][i]) # calculate the degree of similarity by using what instrction taught
                similarities.append((similarity,user)) # store the pair of score and username by tuples
    else: # if user types a wrong answer, call averages function
        averages()
        return
    similarities.sort()
    similarities.reverse() # sort and reverse so that ratings will rank from highest to lowest
    person1,person2,person3 = similarities.pop(0),similarities.pop(0),similarities.pop(0)
    rating1,rating2,rating3 = rating_data[person1[1]],rating_data[person2[1]],rating_data[person3[1]] # extract the name and ratings for books for the first three person
    books_ratings=[0]*len(book) # creating a list of zero 
    
    for i in range(len(books_ratings)): # this loop adds the  rating for each book of three user togethre and calculate average
        n=0
        if rating1[i]!=0: # Test if the user rating is zero 
            books_ratings[i]+=int(rating1[i])
            n+=1
        else:
            n=n
        if rating2[i]!=0:
            books_ratings[i]+=int(rating2[i])
            n+=1
        else:
            n=n
        if rating3[i]!=0:
            books_ratings[i]+=int(rating3[i])
            n+=1
        else:
            n=n
        if n != 0:
            books_ratings[i]=books_ratings[i]/n
    recommendations=[]
    for i in range (len(books_ratings)): # loop the ratings for books
        if books_ratings[i] != 0:
            recommendations.append((books_ratings[i],book[i]))
    recommendations.sort()
    recommendations.reverse()
    for (rating,book_title) in recommendations: # print the pairs together 
        if rating > 0:
            print(book_title,rating)
        
def decision(): # Build a starting page and ask what user wants to do 
    print("Welcome to the Book Recommender. Type the word in the")
    print("left column to do the action on the right.")
    print("recommend : recommend books for a particular user")
    print('averages : output the average ratings of all books in the system')
    print("quit : exit the program")
    decision=input("next task?")
    while True: # loop until user wants to quit
        if decision=="recommend":
            recommendations()
        if decision=="averages":
            averages()
        if decision=="quit": # quit the program if user wants to
            return
        decision=input("\nnext task?")

def main():
    decision()
             

main()
        


