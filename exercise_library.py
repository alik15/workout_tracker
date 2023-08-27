import json

class ExerciseLibrary:
    def __init__(self, json_file):
        self.json_file = json_file
        self.exercise_library = self.load_library()

    def load_library(self):
        with open(self.json_file, 'r') as f:
            return json.load(f)

    def save_library(self):
        with open(self.json_file, 'w') as f:
            json.dump(self.exercise_library, f, indent=4)

    def add_exercise(self, category, level, exercise_name, weight=None):
        if category not in self.exercise_library:
            self.exercise_library[category] = {}
        if level not in self.exercise_library[category]:
            self.exercise_library[category][level] = []
        exercise = {'name': exercise_name, 'weight': weight}
        self.exercise_library[category][level].append(exercise)
        self.save_library()

    def get_exercise(self, category, level, index):
        if category in self.exercise_library and level in self.exercise_library[category]:
            exercises = self.exercise_library[category][level]
            if 0 <= index < len(exercises):
                return exercises[index]
        return None

    def get_categories(self):
        return list(self.exercise_library.keys())

    def get_levels(self, category):
        return list(self.exercise_library.get(category, {}).keys())
    
    def get_exercises(self, category, level):
        return self.exercise_library.get(category, {}).get(level, [])
