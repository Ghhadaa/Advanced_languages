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

    print("\n========== ADD PLAYER ==========")

    player = {}

    # -----------------------------------
    # Player ID
    # -----------------------------------
    while True:

        player_id = input("Player ID: ")

        valid, message = validations.validate_player_id(
            player_id
        )

        if valid:

            player["id"] = player_id
            break

        else:
            print("Error:", message)

    # -----------------------------------
    # Name
    # -----------------------------------
    while True:

        name = input("Player Name: ")

        valid, message = validations.validate_name(
            name
        )

        if valid:

            player["name"] = name
            break

        else:
            print("Error:", message)

    # -----------------------------------
    # Age
    # -----------------------------------
    while True:

        age = input("Age: ")

        valid, message = validations.validate_age(
            age
        )

        if valid:

            player["age"] = int(age)
            break

        else:
            print("Error:", message)

    # -----------------------------------
    # Best Time
    # -----------------------------------
    while True:

        min_time = input("Best Time: ")

        valid, message = validations.validate_time(
            min_time
        )

        if valid:

            player["min_time"] = float(min_time)
            break

        else:
            print("Error:", message)

    # -----------------------------------
    # Rounds
    # -----------------------------------
    while True:

        rounds = input("Rounds Played: ")

        valid, message = validations.validate_rounds(
            rounds
        )

        if valid:

            player["rounds"] = int(rounds)
            break

        else:
            print("Error:", message)

    # -----------------------------------
    # Wins
    # -----------------------------------
    while True:

        wins = input("Wins: ")

        valid, message = validations.validate_wins(
            wins,
            player["rounds"]
        )

        if valid:

            player["wins"] = int(wins)
            break

        else:
            print("Error:", message)

    # -----------------------------------
    # Save Player
    # -----------------------------------
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