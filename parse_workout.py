import re


def parse_workout(workout, conn, c):
    lines = workout.split('\n')
    title = lines[0]
    date = lines[1]

    # Add the workout to the database
    c.execute("INSERT INTO workouts (title, date) VALUES (?, ?)", (title, date))
    workout_id = c.lastrowid

    exercise = None
    for line in lines[2:]:
        if not line.startswith('Set'):
            exercise = line.strip()
            continue

        # Extract the set number, weight, and reps from the line
        match = re.match(r'Set (\d+): (\d+(?:\.\d+)?) lb × (\d+)', line)
        if match:
            set_number = int(match.group(1))
            weight = float(match.group(2))
            reps = int(match.group(3))

            # Insert the workout data into the database
            c.execute("INSERT INTO exercises (workout_id, exercise, set_number, weight, reps) VALUES (?, ?, ?, ?, ?)",
                      (workout_id, exercise, set_number, weight, reps))
            conn.commit()
