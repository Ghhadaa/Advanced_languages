import re
import database


# -----------------------------------
# Validate Player ID
# -----------------------------------
def validate_player_id(player_id):

    # Must contain 4 digits only
    if not re.fullmatch(r"\d{4}", player_id):

        return False, (
            "Player ID must contain "
            "exactly 4 digits."
        )

    # Check duplicate ID
    if database.search_player(player_id):

        return False, "Player ID already exists."

    return True, ""


# -----------------------------------
# Validate Name
# -----------------------------------
def validate_name(name):

    if len(name.strip()) == 0:

        return False, "Name cannot be empty."

    if not re.fullmatch(r"[A-Za-z ]+", name):

        return False, (
            "Name must contain letters only."
        )

    return True, ""


# -----------------------------------
# Validate Age
# -----------------------------------
def validate_age(age):

    try:

        age = int(age)

        if age < 10 or age > 100:

            return False, (
                "Age must be between 10 and 100."
            )

        return True, ""

    except:

        return False, "Age must be numeric."


# -----------------------------------
# Validate Time
# -----------------------------------
def validate_time(min_time):

    try:

        min_time = float(min_time)

        if min_time <= 0:

            return False, (
                "Time must be greater than 0."
            )

        if min_time > 100:

            return False, (
                "Time value is unrealistic."
            )

        return True, ""

    except:

        return False, "Time must be numeric."


# -----------------------------------
# Validate Rounds
# -----------------------------------
def validate_rounds(rounds):

    try:

        rounds = int(rounds)

        if rounds < 0:

            return False, (
                "Rounds cannot be negative."
            )

        return True, ""

    except:

        return False, "Rounds must be numeric."


# -----------------------------------
# Validate Wins
# -----------------------------------
def validate_wins(wins, rounds):

    try:

        wins = int(wins)
        rounds = int(rounds)

        if wins < 0:

            return False, (
                "Wins cannot be negative."
            )

        if wins > rounds:

            return False, (
                "Wins cannot exceed rounds."
            )

        return True, ""

    except:

        return False, "Wins must be numeric."