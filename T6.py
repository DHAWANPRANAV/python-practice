#A dataset records customer feedback ratings as strings: "5", "4", "3". Convert these 
#into integers and calculate the total rating score.

ratings =[] #Created a list

for i in range(5): #Number of rating input to be taken 
    rating = input("Please enter your rating (1-5): ")#rating entry prompt 
    ratings.append(int(rating))#entering ratings into the list 

average_rating = sum(ratings) / len(ratings)#calculating average 
print("Average rating:", average_rating)#printing average

