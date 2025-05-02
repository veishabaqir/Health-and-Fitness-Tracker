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
        total_calories = 0
        for workout in self.workouts:
            calories = workout.total_calories_burned()
            total_calories += calories
            print(f"- {workout.name} ({workout.date}): {len(workout.exercises)} exercises, {calories} kcal burned")
        print(f"Total Workouts: {len(self.workouts)}")
        print(f"Total Calories Burned: {total_calories} kcal")


class Meal:
    def __init__(self, name, calories, protein, carbs, fats):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fats = fats

    def __str__(self):
        return (f"Meal: {self.name}, Calories: {self.calories}, Protein: {self.protein}g, "
                f"Carbs: {self.carbs}g, Fats: {self.fats}g")


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
    meal1=Meal(name="Breakfast ", Calories=1000, protein=400, carbs=70, fats=20) 
    meal1=Meal(name="Lunch ", Calories=2000, protein=300, carbs=75, fats=25) 
