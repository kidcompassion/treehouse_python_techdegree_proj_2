import constants

if __name__ =="__main__":
    
    raw_player_data = constants.PLAYERS
    raw_team_data = constants.TEAMS

    def clean_data():
        pass


#pt 1 - clean data

# Create a clean_data function. This function should perform the following actions:
# 
#     [X] Read the existing player data from the PLAYERS constants provided in constants.py
#     Clean the player data using copy.deepcopy().
#     Save the cleaned data to a new collection.
# 
# Data to be cleaned:
# 
#     Height: This should be saved as an integer
#     Experience: This should be saved as a boolean value (True or False)
# 
# HINT: Think Lists with nested Dictionaries might be one way.



#pt 2 - create teams

#Now that the player data has been cleaned, create a balance_teams function to balance the players across the three teams: Panthers, Bandits, and Warriors. Make sure the teams have the same number of total players on them when your team balancing function has finished.
#
#HINT: To find out how many players should be on each team, divide the length of players by the number of teams:
#
#num_players_team = len(PLAYERS) / len(TEAMS)
#


#pt 3 - show stats

#When displaying the selected teams' stats to the screen, you will want to include:
#
#    Team's name as a string
#    Total players on that team as an integer
#    The player names as strings separated by commas
#