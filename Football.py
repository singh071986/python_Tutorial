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
        print(df.isna().sum().sum())
        if df.isna().sum().sum()>0:
           print(f"Missing value count row wise::\n{df.isna().sum().sum()}")
           print(f"Drop if any missing value::\n{df.dropna()}")
        print(f"count after drop missing value ::\n{df.shape[0]}")
        #step3
        print(f"No of tuples/rows ::{df.shape[0]}")
        print(f"Number of unique tournaments in dataset::\n {df['tournament'].nunique()}")
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


        import matplotlib.pyplot as plt
        # labels = ['Home Wins', 'Away Wins', 'Draws']
        # sizes = [home_wins, away_wins, draws]
        # colors = ['lightblue', 'lightcoral', 'lightgreen']
        # plt.pie(sizes,  labels=labels, colors=colors, autopct='%1.1f%%')
        # plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        # plt.title("Football Match Outcomes")
        # plt.show()
        #step 6
        import pandas as pd
        matchoutcomes=pd.Series({"Home Winds":home_wins,"Away Wins":away_wins,"Draws":draws})
        matchoutcomes.plot(kind='pie',autopct='%1.1f%%',title='Football Match Outcomes')
        plt.show()


        # Debug:
        print("unique values:", df['neutral'].unique())
        print(df['neutral'].value_counts(dropna=False))
        # If you meant to drop rows with missing data, assign the result:
        df = df.dropna(subset=['neutral'])
        df['neutral'] = df['neutral'].astype(str).str.upper()
        neutral_matches=df[df['neutral']=='TRUE'].shape[0]
        non_neutral_matches=df[df['neutral']=='FALSE'].shape[0]
        print(f"Neutral matches: {neutral_matches}")
        print(f"Non-neutral matches: {non_neutral_matches}")
        # #print(df['neutral'])
        neautral_data=pd.Series({"Neutral Matches":neutral_matches,"Non-Neutral Matches":non_neutral_matches})
        neautral_data.plot(kind='pie',color=['orange','purple'],title='Neutral vs Non-Neutral Matches',autopct='%1.1f%%')
        plt.show()




fb=Football()
fb.football()


