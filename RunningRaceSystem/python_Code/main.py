import database
import auth
import validations
import analysis
import leaderboard


# -----------------------------------
# Welcome
# -----------------------------------
def welcome():

    print("\n==========================================")
    print(" Smart Running Race Management System")
    print("==========================================")


# -----------------------------------
# Menu
# -----------------------------------
def menu():

    print("\n1 - Add Player")
    print("2 - Search Player")
    print("3 - Update Player")
    print("4 - Delete Player")
    print("5 - Display All Players")
    print("6 - Show Leaderboard")
    print("7 - Exit")


# -----------------------------------
# Add Player
# -----------------------------------
def add_player():

    player = {}

    player["id"] = input("Player ID: ")
    player["name"] = input("Player Name: ")

    age = int(input("Age: "))

    if not validations.valid_age(age):

        print("Invalid age.")
        return

    player["age"] = age

    min_time = float(input("Best Time: "))

    if not validations.valid_time(min_time):

        print("Invalid time.")
        return

    player["min_time"] = min_time

    rounds = int(input("Rounds Played: "))
    wins = int(input("Wins: "))

    if not validations.valid_wins(wins, rounds):

        print("Wins cannot exceed rounds.")
        return

    player["rounds"] = rounds
    player["wins"] = wins

    success = database.add_player(player)

    if success:

        print("\nPlayer added successfully.")

    else:

        print("\nPlayer ID already exists.")


# -----------------------------------
# Search Player
# -----------------------------------
def search_player():

    player_id = input("Enter Player ID: ")

    player = database.search_player(player_id)

    if player:

        category = analysis.player_category(
            player[3],
            player[5]
        )

        score = analysis.performance_score(
            player[3],
            player[5]
        )

        print(f"""
========== PLAYER INFO ==========

ID: {player[0]}
Name: {player[1]}
Age: {player[2]}
Best Time: {player[3]}
Rounds: {player[4]}
Wins: {player[5]}

Category: {category}
Performance Score: {score}
        """)

    else:

        print("\nPlayer not found.")


# -----------------------------------
# Display Players
# -----------------------------------
def display_players():

    players = database.get_all_players()

    if players:

        for player in players:

            print(f"""
-----------------------------
ID: {player[0]}
Name: {player[1]}
Age: {player[2]}
Best Time: {player[3]}
Rounds: {player[4]}
Wins: {player[5]}
-----------------------------
            """)

    else:

        print("\nNo players found.")


# -----------------------------------
# Update Player
# -----------------------------------
def update_player():

    player_id = input("Enter Player ID: ")

    min_time = float(input("New Best Time: "))
    rounds = int(input("New Rounds: "))
    wins = int(input("New Wins: "))

    success = database.update_player(
        player_id,
        min_time,
        rounds,
        wins
    )

    if success:

        print("\nPlayer updated successfully.")

    else:

        print("\nPlayer not found.")


# -----------------------------------
# Delete Player
# -----------------------------------
def delete_player():

    player_id = input("Enter Player ID: ")

    success = database.delete_player(player_id)

    if success:

        print("\nPlayer deleted successfully.")

    else:

        print("\nPlayer not found.")


# -----------------------------------
# Main Program
# -----------------------------------
def main():

    database.create_tables()

    welcome()

    if not auth.admin_login():
        return

    while True:

        menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_player()

        elif choice == "2":
            search_player()

        elif choice == "3":
            update_player()

        elif choice == "4":
            delete_player()

        elif choice == "5":
            display_players()

        elif choice == "6":
            leaderboard.show_leaderboard()

        elif choice == "7":

            print("\nGood Luck.")
            break

        else:

            print("\nInvalid choice.")


main()