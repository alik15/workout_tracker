from exercise_library import ExerciseLibrary
from WorkoutDayManager import WorkoutDayManager

exercise_library = ExerciseLibrary("workout_library.json")
workout_manager = WorkoutDayManager("workouts.json", exercise_library)



E1 = ExerciseLibrary()

while(True):
    
  
  print("[0] Display previous workouts")
  print("[1] Record new workout")
  print("[2] Exit")

  term_input  = input()
  if (term_input == 1):
    print("pls enter the following data ")
    print("date, day, workout, exercise_name, sets, reps")
    date = input("date")
    day = input("day")
    workout = input("workout")
    exercise_name= input("exercise_name")
    sets = input("sets")
    reps = input("reps")
    WorkoutDayManager.record_workout(date,day,workout,exercise_name,sets,reps)

