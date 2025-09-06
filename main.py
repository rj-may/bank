
from player import player

def start():

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



def main():
    start()

    


main()