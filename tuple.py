# # 1. Write a Python program to create a tuple of five integers and display it.
# tuple=(1,2,3,4,5)
# print(tuple)

# # 2.Create a tuple containing five city names. Display:
# #  First city
# #  Last city
# #  Third city
# cities=("kolhapur", "mumbai", "pune", "delhi", "bangalore")
# print("First city:", cities[0])
# print("Last city:", cities[-1])
# print("Third city:", cities[2]) 

# #3. Create a tuple of student names and display the total number of students using the len() function.
# students = ("Rahul", "Priya", "Amit", "Sneha", "Riya")

# print("Students:", students)
# print("Total number of students:", len(students))

# # 4. Create a tuple of colors. Check whether a given color exists in the tuple
# colors = ("Red", "Blue", "Green", "Yellow", "Black")

# color = input("Enter color to search: ")

# if color in colors:
#     print(color, "exists in the tuple")
# else:
#     print(color, "does not exist in the tuple")

# # 5. Create a tuple of fruits and display each fruit using a loop.
# fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

# print("Fruits:")

# for fruit in fruits:
#     print(fruit)

# # 6. Create a tuple with repeated numbers and count how many times a particular number
# # appears.
# numbers = (10, 20, 10, 30, 10, 40, 20, 10)
# num = int(input("Enter number to count: "))
# print("Number of occurrences:", numbers.count(num))

# # 7. Create a tuple of employee IDs and find the index of a given ID.
# employee_ids = (101, 102, 103, 104, 105)

# id = int(input("Enter employee ID: "))

# if id in employee_ids:
#     print("Index of", id, "is:", employee_ids.index(id))
# else:
#     print("Employee ID not found")

# # 8. Create two tuples of numbers and concatenate them into a single tuple.
# tuple1 = (10, 20, 30)
# tuple2 = (40, 50, 60)

# result = tuple1 + tuple2

# print("Tuple 1:", tuple1)
# print("Tuple 2:", tuple2)
# print("Concatenated tuple:", result)

# # 9. Create a tuple containing three elements and repeat it four times.
# numbers = (10, 20, 30)

# result = numbers * 4

# print("Original tuple:", numbers)
# print("Repeated tuple:", result)

# # 10. Create a tuple of 10 numbers and display:
# #  First five elements
# #  Last five elements
# #  Middle four elements
# #  Alternate elements
# #  Reverse tuple
# numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# print("Tuple:", numbers)

# # First five elements
# print("First five elements:", numbers[:5])

# # Last five elements
# print("Last five elements:", numbers[5:])

# # Middle four elements
# print("Middle four elements:", numbers[3:7])

# # Alternate elements
# print("Alternate elements:", numbers[::2])

# # Reverse tuple
# print("Reverse tuple:", numbers[::-1])
