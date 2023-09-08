# Part A
weeks = 16
classes = 5
tuition = 6000
classes_per_week = 3
cost_per_week = (tuition / classes) / weeks
cost_per_class = (cost_per_week/classes_per_week)
print("Your cost per week is:", cost_per_week)
print("Your cost per class is", cost_per_class)
print(weeks, type(weeks)) 
print(classes, type(classes))
print(tuition, type(tuition))
print(classes_per_week, type(classes_per_week))
print(cost_per_class, type(cost_per_class))

# Part B
import random 
print(random.randint(0,10))

var = [10,15,23,24,56,67,54,98]
print(random.choice(var))