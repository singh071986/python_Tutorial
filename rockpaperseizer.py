import random as ran

from pandas.core.dtypes.inference import is_decimal


def rps_game():
    #choies = ['rock', 'paper', 'scissors']
    user_input=input("enter your choice (rock as 1, paper as 2, scissors as 3): ")
    # rock --scissors.
    # paper --rock
    # scissors --paper
    my_choice=ran.randint(1,3)
    if  (user_input not in ['1','2','3']):
        print("User selection is invalid! Please enter rock as 1, paper as 2, scissors as 3.")
    elif (int(user_input)==my_choice):
        print("It's a tie! Please try again.")
    elif (int(user_input)==1 and my_choice==3) or (int(user_input)==2 and my_choice==1) or (int(user_input)==3 and my_choice==2):
        print(f"User is winner .{user_input}")
    else:
        print(f"User lost this game:{my_choice} , Please try again!")

rps_game()



