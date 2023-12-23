

import constants
import copy
import sys # To allow the user to quit the application

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

        try:
            if selection == "a":
                # If selection is A, choose a team
                choice_menu_2()
            elif selection == "b":
                # If selection is B, quit the app
                quit()
            else:
                print("This is not a valid selection. Your choices are A or B. Please try again. ")
                choice_menu_1()
        except ValueError:
            print("You must enter either A, B, or C")

        
    def choice_menu_2():
        # When the menu or stats display to the console, it should display in a nice readable format. 
        choices_2 = "A) Panthers \n"
        choices_2 += "B) Bandits \n"
        choices_2 += "C) Warriors \n"

        # Print the team options
        print(choices_2)

        # Get user selection and set it to lowercase
        team_selection = input("Enter an option: ").lower()
        
        try:
            # Retrieve details from selected team based on user input
            if team_selection == "a":
                selected_team('Panthers')
            elif team_selection == "b":
                selected_team('Bandits')
            elif team_selection =="c":
                selected_team('Warriors')
            else:
                print("This is not a valid selection. Your choices are A or B. Please try again")
                choice_menu_2()
        except ValueError:
            print("You must enter either A, B, or C")

    def clean_height(player):
        ## FYI: This function runs inside of clean_data() as part of a loop
        # Split height string into parts
        height_int = player['height'].split()
        # Grab the number
        height_int = height_int[0]
        # Convert to integer and put back into dictionary
        player['height'] = int(height_int)

    def clean_experience(player):
        ## FYI: This function runs inside of clean_data() as part of a loop
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
        ## FYI: This function runs inside of clean_data() as part of a loop
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
            
        # Put cleaned guardian names back into dictionary, BUT append their player's experience level to the end of the list
        player['guardians'] = guardians_list + [player['experience']]
        

    def clean_data():
        # Clean the player data using copy.deepcopy().
        # Save the cleaned data to a new collection
        cleaned_player_data = copy.deepcopy(raw_player_data)
        cleaned_team_data = copy.deepcopy(raw_team_data)      

        # Loop through player data to clean it
        for player in cleaned_player_data:
            
            # HEIGHT
            clean_height(player)

            ## EXPERIENCE
            clean_experience(player)

            ## GUARDIANS
            clean_guardians(player)

        # Take the unbalanced list of players and pass it into a function to be broken up into teams
        return balance_teams(cleaned_player_data, cleaned_team_data)



    def balance_players(player_info, total_teams, team_size):
         
        # Variables for lists to separate players into experienced and inexperienced categories
        experienced_players = []
        inexperienced_players = []

        # Grab all experienced players
        experienced_players = [ x for x in player_info if x['experience'] == True ]
        
        #Grab all inexperienced players
        inexperienced_players = [ x for x in player_info if x['experience'] == False ]
           
        # Evenly divide experienced players over total number of teams. 
        experienced_players = [ experienced_players[i:i+int(team_size/2)] for i in range(0, len(experienced_players), int(team_size/2))]
       
        # Evenly divide in experienced players over total number of teams
        inexperienced_players = [ inexperienced_players[i:i+int(team_size/2)] for i in range(0, len(inexperienced_players), int(team_size/2))]
       
        # Variable that creates a list of 3 teams, each with equal experienced and inexperienced players
        split_players = []
       
        for num in range(total_teams):      
            split_players.append(experienced_players[int(num)] + inexperienced_players[int(num)])

        # returns list of lists for each divided team
        return split_players
    

    def balance_guardians(player_info, total_teams, team_size):
        
        # Grab all guardians, so you can split them up based on child's experience
        all_guardians = [ x['guardians'] for x in player_info]
        
        
        #loop through guardians, and put them into either an experienced list or an inexperienced list
        experienced_guardians = [x for x in all_guardians if x[-1] == True]
        inexperienced_guardians = [x for x in all_guardians if x[-1] == False]
        
        # Evenly divide guardians with experienced kids over total number of teams
        experienced_guardians = [ experienced_guardians[i:i+int(team_size/2)] for i in range(0, len(experienced_guardians), int(team_size/2))]
       
        # Evenly divide in guardians with inexperienced kids over total number of teams
        inexperienced_guardians = [ inexperienced_guardians[i:i+int(team_size/2)] for i in range(0, len(inexperienced_guardians), int(team_size/2))]
       
        #Set up list to hold one group of correctly divided guardians per team
        split_guardians = []
        
        # concantenate experienced and inexperienced players 
        for num in range(total_teams):
            split_guardians.append(experienced_guardians[int(num)] + inexperienced_guardians[int(num)])
        
        return split_guardians


    def balance_teams(player_info, team_info):
        # Create a balance_teams function to balance the players across the three teams
        
        balanced_teams = []

        # count total number of players
        total_players = len(player_info)
        # count total number of teams
        total_teams = len(team_info)

        # calculate how many players each team should have
        team_size = int(total_players/total_teams)

        # Split players and guardians into experienced/inexperienced groups
        player_results = balance_players(player_info, total_teams, team_size)
        guardian_results = balance_guardians(player_info, total_teams, team_size)

        # Set and iterate a counter to allow for looping between 3 teams
        counter = 0

        # for each team, grab the name, the size and a share of the players, the corresponding parents, and their experience counts
        for team in team_info:
            balanced_teams.append({
                "team_name": team,
                "team_size": team_size,
                "team_players": player_results[counter],
                "team_guardians": guardian_results[counter],
                "team_inexperienced": player_results[1],
                "team_experienced": player_results[2]
                })
            counter+= 1

        return balanced_teams


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

    
    # Pass selected team name into dictionary of teams, in order to retrieve the requested one.
    def selected_team(team_name):
        # Get list of cleaned data
        divided_teams = clean_data()
        
        # Use user input to grab details for selected team
        selected_team = [x for x in divided_teams if x['team_name'] == team_name]
       
        # Drill into the resulting list to grab the dictionary
        selected_team = selected_team[0]

        # Assign desired values for easier printing
        selected_team_name = selected_team['team_name']
        selected_team_count = selected_team['team_size']
        selected_team_roster = selected_team['team_players'] # this is breaking because it loads up all 3 teams
        formatted_team_roster = []
        experienced_team_count = len([x for x in selected_team_roster if x['experience'] == True])
        inexperienced_team_count = len([x for x in selected_team_roster if x['experience'] == False])
        team_guardians = selected_team['team_guardians']

        # loop through the roster and push all player names into list that we can convert to a string
        for x in selected_team_roster:
            formatted_team_roster.append(x['name'])
      
        # loop through players and push all heights into a list that we can convert to a string
        average_height = [] 
        for y in selected_team['team_players']:
            average_height.append(y['height'])

        # loop through all guardians and push them into a list that we can convert to a string
        formatted_guardians = []
        flattened_guardians = []
        for l in team_guardians:
            formatted_guardians.append(l[:-1])
        for row in formatted_guardians:
            flattened_guardians += row
        
        final_guardians = [''.join(x) for x in flattened_guardians]

        # Set up selected team details for printing in the app
        team_details = "Team: " + selected_team_name + " Stats \n"
        team_details += "Total players: " + str(selected_team_count)+" \n"
        # Concantenate player names into string
        team_details += "Players on Team: " +", ".join(formatted_team_roster) + " \n"
        team_details += "Guardians: " +", ".join(final_guardians) + " \n"
        team_details += "Total experienced players: " + str(experienced_team_count) + "\n"
        team_details += "Total inexperienced player: " + str(inexperienced_team_count) + "\n"
        team_details += "Average player height: " + str(calculate_avg_height(average_height)) + "\n"
        
        # print team's details to console
        print(team_details)
        
        # After viewing results, have user choose their next option
        next_selection = input("Press ENTER to continue")
        if next_selection == "":
            choice_menu_1()
        
    # Call starting function to run application
    start_app()