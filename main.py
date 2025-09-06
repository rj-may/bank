
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

    for i in number_rounds:
        print("ROUND " + str(i +1) + "\n \n")
        
        round_obj = round()


        playing = True

        while playing == True:

            current_player = players[player_index]
            
                
            if current_player.banked == True:
                player_index = (player_index +1) % len(players)

                continue # this skips to the next player

            print("It is " + current_player.get_name() + "'s turn!")
                
            valid_roll = False

            while valid_roll == False:
                if round_obj.get_roll_num() <3:
                    roll = input("What did they roll?")
                else:
                    roll = input("Is someone banking?")

                if isinstance(roll, int):
                    if round_obj.get_roll_num() <3:
                        if 1 < roll<  13:
                            valid_roll = True
                    else:
                        if 2 < roll<  12:
                            valid_roll = True

                elif isinstance(roll, str):
                    roll = roll.lower()

                    possible = ["d", "doubles", "double"]
                    if roll in possible:
                        valid_roll = True

                else:
                    print("Please enter a valid value")

            round_obj.add_score(roll)

                
            if round_obj.get_game_over() == True:
                playing = False

            print("Score is ", round_obj.get_score())

            player_index = (player_index +1) % len(players) 




main()