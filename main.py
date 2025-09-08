
from player import player
from round import round

def intialize_players():

    print("Welcome to  Bank!!!")


    while True:
        user_input = input("Enter how many players you want: ")
        try:
            player_numbers = int(user_input)
            break  # valid integer, exit loop
        except ValueError:
            print("That’s not a valid integer. Try again.")
    
    players = []

    for i in range(player_numbers):

        user_input = input("Player name: ")
        while True:
            try:
                name = str(user_input)

                player_obj = player(name)
                players.append(player_obj)
                break
            except ValueError:
                print("That’s not a valid integer. Try again.")

    return players


# def play_round(players):
#     for p in players:
#         if p.banked == False:
            


def main():
    players = intialize_players()
    
    while True:
        user_input = input("How many rounds do you want? ")
        try:
            number_rounds = int(user_input)
            break  # valid integer, exit loop
        except ValueError:
            print("That’s not a valid integer. Try again.")
    
        
    player_index = 0

    for i in range(number_rounds):
        print("ROUND " + str(i +1) + "\n \n")
        
        round_obj = round()


        playing = True

        while playing == True:

            current_player = players[player_index]
            
                
            if current_player.get_banked == True:
                player_index = (player_index +1) % len(players)

                ### TODO build a cyler here to check if everyone is banked

                continue # this skips to the next player

            print("It is " + current_player.get_name() + "'s turn!")
                
            valid_roll = False

            while valid_roll == False:
                if round_obj.get_roll_num() <3:
                    roll = input("What did they roll?")
                    if isinstance(roll, int):
                        if 1 < roll<  13:
                            valid_roll = True

                else:
                    roll = input("What did they roll, or is someone banking?")

                    if isinstance(roll, int):
       
                        if 2 < roll<  12:
                            valid_roll = True

                    elif isinstance(roll, str):
                        roll = roll.lower()

                        possible = ["d", "doubles", "double"]

                        banking_list = ["bank", "banking", "b"]

                        if roll in banking_list:
                            #TODO fix this
                            print("This is broken")
                            continue


                        if roll in possible:
                            valid_roll = True

                        
                            round_obj.add_score(roll)


                            if round_obj.get_game_over() == True:
                                playing = False

                            print("Score is ", round_obj.get_score())

                            player_index = (player_index +1) % len(players) 


                    else:
                        print("Please enter a valid value")


                





main()