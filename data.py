import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, jsonify, request, render_template
import videogamessales as video

video_games = pd.read_csv("video_Games_sales_as_at_22_Dec_2016.csv", header=0)


df = pd.DataFrame(video_games)


#print(df[['Name', 'Platform', 'Publisher', 'NA_Sales']].head(5))

#maximum for NA_sales
def max_NA_Sales(df)-> float:
    p1 = df['NA_Sales'].max()
    return print(p1)



#maximum for EU_sales
def max_EU_Sales(df)-> float:
    p1 = df['EU_Sales'].max()
    return print(p1)

#maximum for JP_sales
def max_JP_Sales(df)-> float:
    p1 = df['JP_Sales'].max()
    return print(p1)

#maximum for Other_sales
def max_other_Sales(df)-> float:
    p1 = df['Other_Sales'].max()
    return print(p1)

#maximum for Global_sales
def max_Global_Sales(df)-> float:
    p1 = df['Global_Sales'].max()
    return print(p1)

#min for NA_sales
def min_NA_Sales(df)-> float:
    p1 = df['NA_Sales'].min()
    return print(p1)
    
#min for EU_sales
def min_EU_Sales(df)-> float:
    p1 = df['EU_Sales'].min()
    return print(p1)

#min for JP_sales
def min_JP_Sales(df)-> float:
    p1 = df['JP_Sales'].min()
    return print(p1)

#min for Other_sales
def min_other_Sales(df)-> float:
    p1 = df['Other_Sales'].min()
    return print(p1)

#min for Global_sales
def min_Global_Sales(df)-> float:
    p1 = df['Global_Sales'].min()
    return print(p1)

#counting how titles are in each Ratings
def count_Ratings (): 
    x1 = df.groupby('Rating')['Rating'].count().sort_values(ascending=False)
    print(x1)


#top 5 oldest release based on Released year
def top_5_old_release ():
    
    print(df[['Name', 'Platform','Year_of_Release']].sort_values(by= 'Year_of_Release', ascending= True).head(5).drop_duplicates())


#Total slaes by genre and region sale.
def Genre_total():
    Genre_request = input('What types of genera sales do you want to look at in NA: (Sports, Platform, Racing, Role-Playing, Puzzle, Misc, Shooter, Simulation, Action, Fighting, Adventure, Strategy)')
    sales_request = input('What region do you want to see this generas total sales from:(NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales)')
    G = df.loc[(df['Genre'] == Genre_request ) & (df[sales_request])]
    total_sales = G.groupby('Genre')[sales_request].sum()
    print(total_sales)




#Gives you games based on Genre
def type_Genre() ->str:
    Genre_request = input('What types of games do you want to look at: (Sports, Platform, Racing, Role-Playing, Puzzle, Misc, Shooter, Simulation, Action, Fighting, Adventure, Strategy)')
    G = df[(df['Genre'] == Genre_request)]
    return print(G)




#counts on how many times the number of platforms are in the data. 
def count_platforms():
    x1 = df.groupby('Platform')['Platform'].count().sort_values(ascending=False)
    print(x1)


#Graph
def graph():
    graph_something = df.groupby('Genre')['NA_Sales'].sum().sort_values(ascending=False).head(5)

    plt.title("Genre V.S North Amercias sales")
    #p1 = graph_something.groupby('Genre')['NA_Sales'].mean().sort_values()
    graph_something.plot.bar(x='Genre', y='NA_Sales')
    plt.show()



#CRUD OPERATIONS

data = Flask(__name__)

@data.route("/")
def hello():
    return "Welcome to Video Games Sales data"


@data.route("/videogamessales", methods=["GET", "POST"])
def handle_create_read():
    if request.method == "GET":
        return jsonify(video.read_video_games())
    if request.method == "POST":
        p1 = request.get_json()
        video.add_video_games(p1)
        return "Added!"

@data.route("/videogamessales/<id>", methods=["GET", "PUT", "DELETE"])
def handle_update_delete(id):
    try:
        int_id = int(id)
    except ValueError:
        return "Id must be an int"
    if request.method == "GET":
        return jsonify(video.get_video_games_sales_by_id(int_id))
    if request.method == "PUT":
        p1 = request.get_json()
        video.update_video_games(int_id, p1)
        return "Video game updated"
    if request.method == "DELETE":
        video.delete_video_games(int_id)
        return "Video games sale Deleted"

if __name__ == "__main__":
    data.run(port=8080)