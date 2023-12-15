

import constants
import copy

if __name__ =="__main__":
    # Read the existing player data from the PLAYERS constants provided in constants.py
    raw_player_data = constants.PLAYERS
    raw_team_data = constants.TEAMS


    # generate menu

    def intro_screen():
        print(f'BASKETBALL TEAM STATS TOOL\n')
        print(f'-----------MENU------------')
        choice_menu_1()

    def quit():
        pass

    def choice_menu_1():
        # When the menu or stats display to the console, it should display in a nice readable format. 
        choices_1 = "Here are your choices \n"
        choices_1 += "A) Display Team Stats \n"
        choices_1 += "B) Quit \n"

        print(choices_1)
        
        # Get user selection and convert to INT for easier comparisons
        selection = input("Enter an option: ").lower()

        if selection == "a":
            choice_menu_2()
        elif selection == "b":
            print("quit")
        
    def choice_menu_2():
        # When the menu or stats display to the console, it should display in a nice readable format. 
        choices_2 = "A) Panthers \n"
        choices_2 += "B) Bandits \n"
        choices_2 += "C) Warriors \n"

        print(choices_2)

        team_selection = input("Enter an option: ").lower()

        # Pass in name of selected team
        if team_selection == "a":
            selected_team('Panthers')
        elif team_selection == "b":
            selected_team('Bandits')
        elif team_selection =="c":
            selected_team('Warriors')
        


    def selected_team(team_name):
        # Get list of cleaned data
        divided_teams = clean_data()

        # Find the team list that matches the selected team
        selected_team = [x for x in divided_teams if x['team_name'] == team_name]
        
        # Drill into the list to grab the dictionary
        selected_team = selected_team[0]
        #print(selected_team)

        #print(selected_team['team_players'])
        # Assign desired values for easier printing
        selected_team_name = selected_team['team_name']
        selected_team_count = selected_team['team_size']
        selected_team_roster = selected_team['team_players']
        formatted_team_roster = []
        total_inexperienced = str(selected_team['team_inexperienced'])
        total_experienced = str(selected_team['team_experienced'])
        team_guardians = selected_team['team_guardians']

       # print(selected_team)

       # print(selected_team['team_guardians'])
        # loop through the roster and push all player names into list
        for x in selected_team_roster:
            formatted_team_roster.append(x['name'])

      
        average_height = [] 
        for y in selected_team['team_players']:
            average_height.append(y['height'])
        

        #format guardian list for rendering

        formatted_guardians = []
        flattened_guardians = []
        for l in team_guardians:
            formatted_guardians.append(l[:-1])
        for row in formatted_guardians:
            flattened_guardians += row
        
        final_guardians = [''.join(x) for x in flattened_guardians]


        team_details = "Team: " + selected_team_name + " Stats \n"
        team_details += "Total players: " + str(selected_team_count)+" \n"
        # Concantenate player names into string
        team_details += "Players on Team: " +", ".join(formatted_team_roster) + " \n"
        team_details += "Guardians: " +", ".join(final_guardians) + " \n"
        team_details += "Total experienced players: " + total_experienced + "\n"
        team_details += "Total inexperienced player: " + total_inexperienced + "\n"
        team_details += "Average player height: " + str(calculate_avg_height(average_height)) + "\n"
        
        # print team's details to console
        print(team_details)
        
        # have user choose their next option
        next_selection = input("Press ENTER to continue")
        if next_selection == "":
            choice_menu_1()
        


    def generate_guardian_list(args):
        pass


    def clean_height():
        pass

    def clean_experience():
        pass

    def clean_guardians(player):
        ## Function runs in a loop and is applied to each player
        
        # Break up the guardians string so it can be turned into a list
        guardians_list = player['guardians'].split(" ")
        
        # Filter out the "and" from the guardians string
        guardians_list = [name for name in guardians_list if 'and' not in name]
        
        # If there are two words in the list, that means one guardian, so concatenate with a space
        if len(guardians_list) == 2 :
            guardians_list = [" ".join(guardians_list)]
        # if there are four words in the list, that means two guardians, so add comma separation
        elif len(guardians_list) == 4:
            guardians_list = [ " ".join(guardians_list[:2])," ".join(guardians_list[2:]) ]
        else:
            guardians_list = ["No guardian on file"]
            
        # Put cleaned guardian names back into dictionary, and concantenate whether their child has experience at the end of the list
        player['guardians'] = guardians_list + [player['experience']]
        



    def calculate_avg_height(args):
        avg_height = args
        print(avg_height)
        sum_height = 0
        total_players = len(avg_height)
        for x in args:
            sum_height+=x

        return sum_height/total_players

    def clean_data():
        # Clean the player data using copy.deepcopy().
        # Save the cleaned data to a new collection
        cleaned_player_data = copy.deepcopy(raw_player_data)
        cleaned_team_data = copy.deepcopy(raw_team_data)
        
        for player in cleaned_player_data:
            
            ## HEIGHT
            # Split height string into parts
            height_int = player['height'].split()
            # Grab the number
            height_int = height_int[0]
            # Convert to integer and put back into dictionary
            player['height'] = int(height_int)

            ## EXPERIENCE
            # Grab Experience info
            experience_bool = player['experience']
            # If it's YES, set to True. If it's NO, set to False.
            if player['experience']== "YES":
                experience_bool = True
            elif player['experience'] == "NO":
                experience_bool = False
            # Put boolean value back into dictionary
            player['experience'] = experience_bool

            ## GUARDIANS
            clean_guardians(player)

        

        return balance_teams(cleaned_player_data, cleaned_team_data)

  

    

    def balance_teams(player_info, team_info):
        # Create a balance_teams function to balance the players across the three teams
        
       # print(player_info)
        balanced_teams = []

        guardian_list = []
        # count total number of players
        total_players = len(player_info)
        # count total number of teams
        total_teams = len(team_info)

        # calculate how many players each team should have
        team_size = int(total_players/total_teams)

        # Create lists for experienced and inexperienced players
        experienced_players = []
        inexperienced_players = []
        experienced_guardians = []
        # Grab all experienced players
        experienced_players = [ x for x in player_info if x['experience'] == True ]

        
        
        #Grab all inexperienced players
        inexperienced_players = [ x for x in player_info if x['experience'] == False ]
        

        #print(experienced_guardians)
        split_players = []
        
        
        # Evenly divide experienced players over total number of teams
        experienced_players = [ experienced_players[i:i+int(team_size/2)] for i in range(0, len(experienced_players), int(team_size/2))]
       
       

        # Evenly divide in experienced players over total number of teams
        inexperienced_players = [ inexperienced_players[i:i+int(team_size/2)] for i in range(0, len(inexperienced_players), int(team_size/2))]
       

        
        team_experience_total = len(experienced_players)
        team_inexperience_total = len(inexperienced_players)
        
        

        split_guardians = []
        experienced_guardians = [ x['guardians'] for x in player_info]
        formatted_experienced_guardians = []
        for y in experienced_guardians:
            parent_experience = len(y) -1
            if y[parent_experience] == True:
                formatted_experienced_guardians.append(y)



        inexperienced_guardians = [ x['guardians'] for x in player_info]
        formatted_inexperienced_guardians = []
        for y in inexperienced_guardians:
            parent_inexperience = len(y) -1
            if y[parent_inexperience] == False:
                formatted_inexperienced_guardians.append(y)

        

         # Evenly divide experienced players over total number of teams
        formatted_experienced_guardians = [ formatted_experienced_guardians[i:i+int(team_size/2)] for i in range(0, len(formatted_experienced_guardians), int(team_size/2))]
       
       

        # Evenly divide in experienced players over total number of teams
        formatted_inexperienced_guardians = [ formatted_inexperienced_guardians[i:i+int(team_size/2)] for i in range(0, len(formatted_inexperienced_guardians), int(team_size/2))]
       

        
        # concantenate experienced and inexperienced players 
        for num in range(total_teams):
            split_players.append(experienced_players[int(num)] + inexperienced_players[int(num)])
            split_guardians.append(formatted_experienced_guardians[int(num)] + formatted_inexperienced_guardians[int(num)])
        
        

       
        counter = 0
        # for each team, grab the name, the size and a share of the players
        for team in team_info:
            balanced_teams.append({
                "team_name": team,
                "team_size": team_size,
                "team_players": split_players[counter],
                "team_guardians": split_guardians[counter],
                "team_inexperienced": team_inexperience_total,
                "team_experienced": team_experience_total
                })
            counter+= 1
        
       # print(balanced_teams)
        return balanced_teams

       

 

            


        

        #get selected team data
        #generate list of player guardians

        




    intro_screen()









    
#pt 1 - clean data

# Create a clean_data function. This function should perform the following actions:
# 
#     [X] Read the existing player data from the PLAYERS constants provided in constants.py
#     [X] Clean the player data using copy.deepcopy().
#     [X] Save the cleaned data to a new collection.
# 
# Data to be cleaned:
# 
#     [X] Height: This should be saved as an integer
#     [X] Experience: This should be saved as a boolean value (True or False)
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