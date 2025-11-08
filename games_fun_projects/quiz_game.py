import sqlite3

def create_db_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def save_score(conn, name, score):
    sql = """INSERT INTO scores(name, score)
              VALUES(?,?)"""
    cur = conn.cursor()
    cur.execute(sql, (name, score))
    conn.commit()
    return cur.lastrowid

def get_all_scores(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM scores ORDER BY score DESC")

    rows = cur.fetchall()
    return rows

print("Welcome to AskPython Quiz")
answer = input("Are you ready to play the quiz? (yes/no) : ")

score = 0
total_questions = 3

if answer.lower() == "yes":
    answer = input("Question 1: What is your Favorite programming language? ")
    if answer.lower() == "python":
        score += 1
        print("Correct")
    else:
        print("Wrong Answer: :(")

    answer = input("Question 2: Do you follow any author on AskPython? ")
    if answer.lower() == "yes":
        score += 1
        print("Correct")
    else:
        print("Wrong Answer :(")

    answer = input(
        "Question 3: What is the name of your favorite website for learning Python?"
    )
    if answer.lower() == "askpython":
        score += 1
        print("Correct")
    else:
        print("Wrong Answer :(")

    print(
        "Thank you for Playing this small quiz game, you attempted",
        score,
        "questions correctly!",
    )
    mark = int((score / total_questions) * 100)
    print(f"Marks obtained: {mark}%")

    player_name = input("Enter your name: ")
    player_score = score

    database = "quiz_game.db"

    conn = create_db_connection(database)

    if conn is not None:
        save_score(conn, player_name, player_score)

        print("Previous scores: ")
        scores = get_all_scores(conn)

        for row in scores:
            print(f"Name: {row[1]}, Score: {row[2]}, Date: {row[3]}")
        conn.close()
    else:
        print("Error! Cannot create the database connection.")
else:
    print(" Please, when you're ready, enter the game again.")

print("BYE!!!")
