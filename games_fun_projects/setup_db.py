import sqlite3

def create_database():
    conn = sqlite3.connect("quiz_game.db")

    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
    )

    conn.commit()
    conn.close()

    print("Database and table created successfully!")

if __name__ == "__main__":
    create_database()