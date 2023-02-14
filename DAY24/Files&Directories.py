

f = open("my_file.txt", "a")  
f.write(" finished")
f.close()

f = open("my_file.txt", "r")
print(f.read())

# import os

# filename = 'my_file.txt'
# if not os.path.exists(filename):
#     open(filename, 'w').close()

# Now the file exists and can be opened safely
#with open(filename, 'r') as file: