

import constants
import copy
import sys

if __name__ =="__main__":
    # Read the existing player data from the PLAYERS constants provided in constants.py
    raw_player_data = constants.PLAYERS
    raw_team_data = constants.TEAMS


    # start app and generate intro
    def start_app():
        print(f'BASKETBALL TEAM STATS TOOL\n')
        print(f'-----------MENU------------')
        choice_menu_1()

    # Allow users to exit
    def quit():
        # https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program
        print("Goodbye!")
        sys.exit(0)


    def choice_menu_1():
        # When the menu or stats display to the console, it should display in a nice readable format. 
        choices_1 = "Here are your choices \n"
        choices_1 += "A) Display Team Stats \n"
        choices_1 += "B) Quit \n"

        print(choices_1)
        
        # Get user selection and convert to INT for easier comparisons
        selection = input("Enter an option: ").lower()

        if selection == "a":
            # If selection is A, choose a team
            choice_menu_2()
        elif selection == "b":
            # If selection is B, quit the app
            quit()
        
    def choice_menu_2():
        # When the menu or stats display to the console, it should display in a nice readable format. 
        choices_2 = "A) Panthers \n"
        choices_2 += "B) Bandits \n"
        choices_2 += "C) Warriors \n"

        # Print the team options
        print(choices_2)

        # Get user selection and set it to lowercase
        team_selection = input("Enter an option: ").lower()

        # Retrieve info for selected team based on user input
        if team_selection == "a":
            selected_team('Panthers')
        elif team_selection == "b":
            selected_team('Bandits')
        elif team_selection =="c":
            selected_team('Warriors')


    # FUNC: 
    # 
    # Pass selected team name into dictionary of teams, in order to retrieve the requested one.
    def selected_team(team_name):
        # Get list of cleaned data
        divided_teams = clean_data()

        # Find the team list that matches the selected team
        selected_team = [x for x in divided_teams if x['team_name'] == team_name]
        
        # Drill into the list to grab the dictionary
        selected_team = selected_team[0]

        # Assign desired values for easier printing
        selected_team_name = selected_team['team_name']
        selected_team_count = selected_team['team_size']
        selected_team_roster = selected_team['team_players']
        formatted_team_roster = []
        total_inexperienced = str(selected_team['team_inexperienced'])
        total_experienced = str(selected_team['team_experienced'])
        team_guardians = selected_team['team_guardians']

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


    def clean_height(player):
        ## Function runs inside of a loop and is applied to each player
        # Split height string into parts
        height_int = player['height'].split()
        # Grab the number
        height_int = height_int[0]
        # Convert to integer and put back into dictionary
        player['height'] = int(height_int)

    def clean_experience(player):
        # Grab Experience info
        experience_bool = player['experience']
        # If it's YES, set to True. If it's NO, set to False.
        if player['experience']== "YES":
            experience_bool = True
        elif player['experience'] == "NO":
            experience_bool = False
        # Put boolean value back into dictionary
        player['experience'] = experience_bool

    def clean_guardians(player):
        ## Function runs inside of a loop and is applied to each player
        
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
            
        # Put cleaned guardian names back into dictionary, and append their player's experience level to the end of the list
        player['guardians'] = guardians_list + [player['experience']]
        



    def calculate_avg_height(args):
        # Get all student heights
        avg_height = args
        sum_height = 0
        
        # calculate total number of players
        total_players = len(avg_height)
        
        # sum all heights
        for x in args:
            sum_height+=x

        # calculate average
        return sum_height/total_players

    def clean_data():
        # Clean the player data using copy.deepcopy().
        # Save the cleaned data to a new collection
        cleaned_player_data = copy.deepcopy(raw_player_data)
        cleaned_team_data = copy.deepcopy(raw_team_data)
        
        for player in cleaned_player_data:
            
            # HEIGHT
            clean_height(player)

            ## EXPERIENCE
            clean_experience(player)

            ## GUARDIANS
            clean_guardians(player)

        

        return balance_teams(cleaned_player_data, cleaned_team_data)

  

    def balance_guardians():
        pass

    def balance_players():
        pass
    

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
        
        split_players = []
        
        
        # Evenly divide experienced players over total number of teams. 
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
        # for each team, grab the name, the size and a share of the players, the corresponding parents, and their experience counts
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
        
        return balanced_teams


    start_app()