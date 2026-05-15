import database
import analysis


# -----------------------------------
# Show Statistics
# -----------------------------------
def show_statistics():

    players = database.get_all_players()

    if not players:

        print("\nNo players available.")
        return

    total_players = len(players)

    fastest_player = min(
        players,
        key=lambda p: p[3]
    )

    highest_wins = max(
        players,
        key=lambda p: p[5]
    )

    best_score_player = None
    best_score = -999

    total_time = 0

    for player in players:

        total_time += player[3]

        score = analysis.performance_score(
            player[3],
            player[5],
            player[4]
        )

        if score > best_score:

            best_score = score
            best_score_player = player

    average_time = (
        total_time / total_players
    )

    print("\n===================================")
    print("        SYSTEM STATISTICS")
    print("===================================")

    print(f"""
Total Players: {total_players}

Fastest Player:
{fastest_player[1]}
Time: {fastest_player[3]}

Highest Wins:
{highest_wins[1]}
Wins: {highest_wins[5]}

Best Performance:
{best_score_player[1]}
Score: {best_score}

Average Best Time:
{round(average_time, 2)}
    """)