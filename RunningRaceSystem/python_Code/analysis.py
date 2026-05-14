def player_category(min_time, wins):

    if min_time < 10 and wins >= 15:
        return "Elite Runner"

    elif min_time < 15 and wins >= 10:
        return "Professional Runner"

    elif min_time < 20:
        return "Intermediate Runner"

    else:
        return " Runner"


def performance_score(min_time, wins):

    score = (wins * 10) - min_time

    return round(score, 2)