import json

class WorkoutDayManager:
    def __init__(self, json_file, exercise_library):
        self.json_file = json_file
        self.exercise_library = exercise_library
        self.workouts = self.load_workouts()

    def load_workouts(self):
        with open(self.json_file, 'r') as f:
            return json.load(f)

    def save_workouts(self):
        with open(self.json_file, 'w') as f:
            json.dump(self.workouts, f, indent=4)

    def add_workout(self, workout_data):
        self.workouts.append(workout_data)
        self.save_workouts()

    def get_workout(self, date):
        for workout in self.workouts:
            if workout['date'] == date:
                return workout
        return None

    def record_workout(self, date, day, workout, exercise_name, sets, reps):
        exercise_details = self.exercise_library.get_exercise(exercise_name)
        if exercise_details:
            workout_data = {
                'date': date,
                'day': day,
                'workout': workout,
                'set': {
                    'set1': [{
                        'exercise_name': exercise_name,
                        'exercise_details': exercise_details,
                        'sets': sets,
                        'reps': reps
                    }]
                }
            }
            self.add_workout(workout_data)
        else:
            print(f"Exercise '{exercise_name}' not found in the library.")
