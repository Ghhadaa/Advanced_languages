import sqlite3

DB_NAME = "players.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():

    conn = connect()
    cursor = conn.cursor()

    # Players Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (

        id TEXT PRIMARY KEY,
        name TEXT,
        age INTEGER,
        min_time REAL,
        rounds INTEGER,
        wins INTEGER

    )
    """)

    # Admin Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admins (

        username TEXT PRIMARY KEY,
        password TEXT

    )
    """)

    # Default Admin
    cursor.execute("""
    INSERT OR IGNORE INTO admins
    VALUES ('admin', '1234')
    """)

    conn.commit()
    conn.close()


# -----------------------------------
# Add Player
# -----------------------------------
def add_player(player):

    conn = connect()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        INSERT INTO players
        VALUES (?, ?, ?, ?, ?, ?)
        """, (

            player["id"],
            player["name"],
            player["age"],
            player["min_time"],
            player["rounds"],
            player["wins"]

        ))

        conn.commit()

        return True

    except:
        return False

    finally:
        conn.close()


# -----------------------------------
# Search Player
# -----------------------------------
def search_player(player_id):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM players
    WHERE id = ?
    """, (player_id,))

    player = cursor.fetchone()

    conn.close()

    return player


# -----------------------------------
# Display Players
# -----------------------------------
def get_all_players():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM players
    ORDER BY min_time ASC
    """)

    players = cursor.fetchall()

    conn.close()

    return players


# -----------------------------------
# Update Player
# -----------------------------------
def update_player(player_id, min_time, rounds, wins):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE players

    SET
        min_time = ?,
        rounds = ?,
        wins = ?

    WHERE id = ?
    """, (

        min_time,
        rounds,
        wins,
        player_id

    ))

    conn.commit()

    success = cursor.rowcount > 0

    conn.close()

    return success


# -----------------------------------
# Delete Player
# -----------------------------------
def delete_player(player_id):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM players
    WHERE id = ?
    """, (player_id,))

    conn.commit()

    success = cursor.rowcount > 0

    conn.close()

    return success


# -----------------------------------
# Admin Login
# -----------------------------------
def login(username, password):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM admins
    WHERE username = ?
    AND password = ?
    """, (

        username,
        password

    ))

    admin = cursor.fetchone()

    conn.close()

    return admin is not None