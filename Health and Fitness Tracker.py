class User:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.workouts = []

    def log_workout(self, workout):
        self.workouts.append(workout)
        print(f"Workout '{workout.name}' logged for {self.name}.")

    def generate_report(self):
        print(f"Fitness Report for {self.name}:")
        for workout in self.workouts:
            print(f"- {workout.name}: {len(workout.exercises)} exercises")
        print(f"Total Workouts: {len(self.workouts)}")


class Workout:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)
        print(f"Exercise '{exercise.name}' added to workout '{self.name}'.")

    def total_calories_burned(self):
        return sum(exercise.calories_burned for exercise in self.exercises)


class Exercise:
    def __init__(self, name, sets, reps, weight, calories_burned):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.calories_burned = calories_burned


# Example usage:
if __name__ == "__main__":
    # Create a user
    user = User(name="John Doe", age=30, weight=75, height=175)

    # Create a workout
    workout1 = Workout(name="Morning Workout", date="2023-10-01")

    # Add exercises to the workout
    exercise1 = Exercise(name="Bench Press", sets=3, reps=10, weight=50, calories_burned=100)
    exercise2 = Exercise(name="Squats", sets=3, reps=15, weight=0, calories_burned=150)

    workout1.add_exercise(exercise1)
    workout1.add_exercise(exercise2)

    # Log the workout for the user
    user.log_workout(workout1)

    # Generate a fitness report
    user.generate_report()