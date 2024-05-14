import sqlite3
import parse_workout


def setup_database():
    conn = sqlite3.connect('workouts_data.db')

    c = conn.cursor()

    c.execute("""
              CREATE TABLE IF NOT EXISTS workouts(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT,
                  date TEXT,
                 )
              """)

    c.execute("""
              CREATE TABLE IF NOT EXISTS exercises(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    workout_id INTEGER,
                    exercise TEXT,
                    set_number INTEGER,
                    weight REAL,
                    reps INTEGER,
                    FOREIGN KEY(workout_id) REFERENCES workouts(id)
                 )
              """)

    conn.commit()
    conn.close()


def create_db():
    setup_database()
    with open('workout.txt') as f:
        workout = f.read()

    conn = sqlite3.connect('workouts_data.db')
    c = conn.cursor()
    parse_workout.parse_workout(workout, conn, c)
    conn.close()
