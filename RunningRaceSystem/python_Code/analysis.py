# -----------------------------------
# Player Category
# -----------------------------------
def player_category(min_time, wins):

    if min_time < 10 and wins >= 15:
        return "Elite Runner"

    elif min_time < 15 and wins >= 10:
        return "Professional Runner"

    elif min_time < 20:
        return "Intermediate Runner"

    else:
        return "Beginner Runner"


# -----------------------------------
# Performance Score
# -----------------------------------
def performance_score(min_time, wins, rounds):

    if rounds == 0:
        return 0

    win_rate = wins / rounds

    score = (win_rate * 100) - min_time

    return round(score, 2)


# -----------------------------------
# Win Rate
# -----------------------------------
def calculate_win_rate(wins, rounds):

    if rounds == 0:
        return 0

    return round((wins / rounds) * 100, 2)


# -----------------------------------
# Performance Recommendation
# -----------------------------------
def performance_recommendation(score):

    if score >= 70:
        return "Outstanding Performance"

    elif score >= 50:
        return "Very Strong Player"

    elif score >= 30:
        return "Needs Minor Improvement"

    else:
        return "Needs Intensive Training"
    
    # -----------------------------------
# Recommendation System
# -----------------------------------
def player_recommendation(
    min_time,
    wins,
    rounds
):

    recommendations = []

    # -----------------------------------
    # Win Rate Analysis
    # -----------------------------------
    if rounds > 0:

        win_rate = (
            wins / rounds
        ) * 100

    else:

        win_rate = 0

    # -----------------------------------
    # Speed Recommendation
    # -----------------------------------
    if min_time > 20:

        recommendations.append(
            "Improve running speed "
            "through sprint training."
        )

    elif min_time > 15:

        recommendations.append(
            "Focus on endurance "
            "and speed balance."
        )

    # -----------------------------------
    # Win Rate Recommendation
    # -----------------------------------
    if win_rate < 40:

        recommendations.append(
            "Increase match practice "
            "to improve win rate."
        )

    elif win_rate < 60:

        recommendations.append(
            "Needs more strategic "
            "race preparation."
        )

    # -----------------------------------
    # Experience Recommendation
    # -----------------------------------
    if rounds < 5:

        recommendations.append(
            "Participate in more races "
            "to gain experience."
        )

    # -----------------------------------
    # Final Recommendation
    # -----------------------------------
    if len(recommendations) == 0:

        recommendations.append(
            "Excellent performance. "
            "Maintain current training."
        )

    return recommendations