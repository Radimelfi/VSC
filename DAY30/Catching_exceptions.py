""" catching exceptions: 
try: something that might cause an exception
except: do this if there was an exception
else: do this if there were no exceptions
finally: Do this np matter what happens """

#ex 1
x = "hello"

try:
  x > 3
except NameError:
  print("You have a variable that is not defined.")
except TypeError:
  print("You are comparing values of different type")
#ex 2
x = 1

try:
  x > 10
except NameError:
  print("You have a variable that is not defined.")
except TypeError:
  print("You are comparing values of different type")
else:
  print("The 'Try' code was executed without raising any errors!")
#ex 3
try:
  x > 3
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The try...except block is finished")

# Raising your own exceptions 
height = float(input ("height: "))
weight= int(input("weight: "))
bmi= weight/height**2
print(bmi)
if height > 3:
  raise ValueError ("Human Height should not be over 3 meters.")

ex 4 

fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.

fruits = ["Apple", "Pear", "Orange"]
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Invalid index. Please provide an index between 0 and " + str(len(fruits)-1))
    else:
        print(fruit + " pie")
 
ex 5
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
      total_likes = total_likes + post['Likes']
    except KeyError:
       pass  # or total_likes += 0
print(total_likes)

def calculate():
  try:
    cal=  lambda a,b,c,d: a+b +c+d
    print(cal(a=10,b=5))
  except TypeError: 
    print(cal(a=10,b=5, c=2, d=6))
  else:
    print("some value are missing")
calculate()
