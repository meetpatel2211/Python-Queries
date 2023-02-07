import pandas as pd

df = pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")

df['id'] = df.index + 1

def read_video_games():
    global df
    return df.to_dict(orient='records')

def get_video_games_sales_by_id(id):
    global df
    return df.loc[df['id'] == int(id)].to_dict(orient="records")

def add_video_games(video_games):
    global df
    df = pd.concat([df, pd.DataFrame(video_games, [len(df)])])

def update_video_games(id, video_games):
    global df
    df.at[id] = video_games 

def delete_video_games(id):
    global df
    df.drop(index=int(id), inplace=True)
    

if __name__ == "__main__":
    print(read_video_games())