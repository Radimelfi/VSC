 
# practicing with list comprehension 
#   li = [new_item for item in list]

lista = [1,2,3,4,5,6,7,8,9,10]

new_list = [n * 2 for n in lista ]
print(new_list)

another_list = [item * 10  for item in range (1,11)]
print(another_list)

# conditional list comprehension
 # li = [new_item for item in list IF TEST ]

name = ["Maria","Ban","Nancy","Gay","Joel","Hanna","Maria","Maria","Maria"]
new_name_list = [item.upper() for item in name if len(item) > 3]
print (new_name_list)


# squared numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number * number for number in numbers]
print(squared_numbers)

# the new list should only contain the even numbers from the list numbers.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num  for num in numbers if num % 2 == 0]
print(result)

# Working with file 

with open("file1.txt") as file1:
    list1 = file1.readlines()
#print(list1)
    
with open("file2.txt") as file2:
    list2 = file2.readlines()
#print(list2)
    
result = [int(num) for num in list1 if num in list2]
print (result)

#Dictionary Comprehension
  #new_dict = {new_key: new_value for item in list}
  #new_dict = {new_key: new_value for (key,Value) in dict.items()}
  #new_dict = {new_key: new_value for (key,Value) in dict.items() if test}
  
import random
names = ["Ana Maria", "Radimelfi Maria", "Randy Jose", "Francisca", "Silvestre", "Maria Rachel", "Ramona"]
student_score = {student:random.randint(1,100)  for student  in names}
print(student_score)

new_student_score = {student:score   for (student, score) in student_score.items() if score >= 70}
print(new_student_score)






