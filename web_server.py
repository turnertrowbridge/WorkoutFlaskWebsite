from flask import Flask, render_template, request
import sqlite3
import create_db
import parse_workout

# Create a Flask app
app = Flask(__name__)

# Define a function to get the workout data from the database


def get_workout_data():
    conn = sqlite3.connect('workouts_data.db')
    c = conn.cursor()
    c.execute("""
                SELECT w.title, w.date, e.exercise, e.set_number, e.weight, e.reps
                FROM workouts w
                JOIN exercises e ON w.id = e.workout_id
              """)
    rows = c.fetchall()
    conn.close()

    # Organize the workouts into dictionary
    workouts = {}
    for row in rows:
        title, date, exercise, set_number, weight, reps = row
        if (title, date) not in workouts:
            workouts[(title, date)] = []
        workouts[(title, date)].append((exercise, set_number, weight, reps))

    return workouts


# Define a route for the root URL
@app.route('/')
def index():
    workout_data = get_workout_data()
    return render_template('index.html', workout_data=workout_data)


# Form to add a workout
@app.route('/add_workout', methods=['POST'])
def add_workout():
    conn = sqlite3.connect('workouts_data.db')
    c = conn.cursor()
    workout_data = request.form['workout_data']
    parse_workout.parse_workout(workout_data, conn, c)
    conn.commit()
    conn.close()
    return 'Workout added successfully!'


# Run the app
if __name__ == '__main__':
    create_db.create_db()
    app.run(debug=True)
