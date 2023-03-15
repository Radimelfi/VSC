# Dictionary Comprehension
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key,Value) in dict.items()}
# new_dict = {new_key: new_value for (key,Value) in dict.items() if test}
import random
# ex 1
names = ["Ana Maria", "Radimelfi Maria", "Randy Jose", "Francisca", "Silvestre", "Maria Rachel", "Ramona"]
student_score = {student:random.randint(1,100)  for student  in names}
print(student_score)

new_student_score = {student:score   for (student, score) in student_score.items() if score >= 70}
print(new_student_score)


# ex 2
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {sentences:len(sentences) for sentences in sentence.split()}
print (result)

# ex 3
"""You are going to use Dictionary Comprehension to create a dictionary called weather_f 
that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit."""

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,    
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {Day:(temp * 9/5) + 32 for (Day, temp) in weather_c.items()}
print(weather_f)