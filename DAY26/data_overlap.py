
# A list called result which contains the numbers that are common in both files.

with open ("file1.txt") as firt_file:
    file1 = firt_file.readlines()
    
with open ("file2.txt") as second_file:
    file2 = second_file.readlines()

result = [int(num) for num in file1 if num in file2 ]
print (result)   