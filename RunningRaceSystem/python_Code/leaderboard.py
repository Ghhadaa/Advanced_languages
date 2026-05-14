import database
import analysis


# -----------------------------------
# Show Leaderboard
# -----------------------------------
def show_leaderboard():

    players = database.get_all_players()

    if not players:

        print("\nNo players found.")
        return

    print("\n========== TOP PLAYERS ==========")

    ranked_players = []

    for player in players:

        score = analysis.performance_score(
            player[3],
            player[5],
            player[4]
        )

        ranked_players.append(
            (player, score)
        )

    ranked_players.sort(
        key=lambda x: x[1],
        reverse=True
    )

    rank = 1

    for item in ranked_players[:5]:

        player = item[0]
        score = item[1]

        print(f"""
Rank: {rank}
Name: {player[1]}
Best Time: {player[3]}
Wins: {player[5]}
Score: {score}
-----------------------------
        """)

        rank += 1