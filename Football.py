class Football:

    def __init__(selfs):
        pass

    def football(self):
        #return "This is the Football module."
        import pandas as pd
        from datetime import datetime
        #step2
        df=pd.read_csv('/Users/Yuvaan/Downloads/results.csv')
        print(f"count before  dropping missing value ::\n{df.shape[0]}")
        if df.isna().sum().sum()>0:
           print(f"Missing value count row wise::\n{df.isna().sum().sum()}")
           print(f"Drop if any missing value::\n{df.dropna()}")
        print(f"count after drop missing value ::\n{df.shape[0]}")
        #step3
        print(f"No of tuples/rows ::{df.shape[0]}")
        print(f"Number of tournaments in dataset::\n {df['tournament'].nunique()}")
        #step4
        #convert date column  in to timestamp format
        df['date']=pd.to_datetime(df['date'],errors='coerce')
        #read year 2018 matches using timestamp
        print(f"Number of matches played in 2018 using timestamp::\n {df[df['date'].dt.year==2018].shape[0]}")

        #convert date column back to string format #read year 2018 matches using string
        df['date']=pd.to_datetime(df['date'],errors='coerce').dt.strftime('%Y-%m-%d')
        print(f"Number of matches played in 2018 using string ::\n {df[df['date'].str.contains('2018')].shape[0]}")

        #step5 Calculate how many times the home team won, lost, or had a draw.
        home_wins=df[df['home_score']>df['away_score']].shape[0] # or (id
        #home_wins=(df['home_score'] > df['away_score']).sum()
        away_wins= df[df['home_score']<df['away_score']].shape[0]
        draws=df[df['home_score']==df['away_score']].shape[0]
        print(f"Home team wins: {home_wins}")
        print(f"Away team wins: {away_wins}")
        print(f"Draws: {draws}")


        # import numpy as np
        # cond = df['home_score'].to_numpy() > df['away_score'].to_numpy()
        # print(cond)
        # positions = np.flatnonzero(cond)        # integer row positions where home_score > away_score
        # print("positons:::\n",positions)
        # home_wins = df.iloc[positions].shape[0] # count using .iloc
        # print(home_wins)

    #step 6

fb=Football()
fb.football()


