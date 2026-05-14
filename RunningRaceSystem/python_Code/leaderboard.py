import database


def show_leaderboard():

    players = database.get_all_players()

    print("\n========== TOP PLAYERS ==========")

    rank = 1

    for player in players[:5]:

        print(
            f"{rank}. {player[1]} "
            f"- {player[3]} sec"
        )

        rank += 1