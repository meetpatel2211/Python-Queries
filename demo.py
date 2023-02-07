#import videogamessales
import data
import pandas as pd


video_games = pd.read_csv("video_Games_sales_as_at_22_Dec_2016.csv", header=0)


df = pd.DataFrame(video_games)


#Maximum of NA_Sales
print('This is the Maximum of the NA_Sales')
data.max_NA_Sales(df)
print('\n')

#Minimum of NA_Sales
print('This is the Minimum of NA_Sales')
data.min_NA_Sales(df)
print('\n')

#counting how many video games are in each Ratings
print("Counting the number of video games in each Rating")
data.count_Ratings()
print('\n')

#top 5 oldest release based on Released year
print("Top 5 oldest release based")
data.top_5_old_release()
print("\n")

#Total slaes by genre and region sale.
print("Total sales for a specific genre and a specific region")
data.Genre_total()
print("\n")

#Gives you games based on Genre
print("This Method gives you all the Video Game Sales based on user selection Genre")
data.type_Genre()
print("\n")

#counts on how many times the number of platforms are in the data. 
print("This Method gives you the count on how many video games are in each platforms")
data.count_platforms()
print("\n")

#This Graph method shows the correlation between NA_Sales on Top 5 Genre
print("This Graph shows the correlation between NA_Sales on Top 5 Genre")
data.graph()
print("\n")