# ### 10 Simple Problem Statements Based on Matplotlib

# 1\. Line Plot: Write a Python program using Matplotlib to create a line plot showing the marks of a student in five subjects.
# import matplotlib.pyplot as plt

# subjects = ['English', 'Maths', 'Science', 'Python', 'Computer']
# marks = [75, 85, 90, 88, 95]

# plt.plot(subjects, marks, marker='o')
# plt.xlabel('Subjects')
# plt.ylabel('Marks')
# plt.title('Student Marks')
# plt.show()

# 2\. Scatter Plot: Write a Python program to create a scatter plot showing the relationship between students' study hours and their marks.
# import matplotlib.pyplot as plt

# hours = [1, 2, 3, 4, 5, 6]
# marks = [40, 50, 60, 65, 80, 90]

# plt.scatter(hours, marks)
# plt.xlabel('Study Hours')
# plt.ylabel('Marks')
# plt.title('Study Hours vs Marks')
# plt.show()


# 3\. Bar Plot: Write a Python program to create a bar chart comparing the sales of five different products.
# import matplotlib.pyplot as plt

# products = ['Pen', 'Book', 'Bag', 'Pencil', 'Scale']
# sales = [50, 80, 40, 70, 30]

# plt.bar(products, sales)
# plt.xlabel('Products')
# plt.ylabel('Sales')
# plt.title('Product Sales')
# plt.show()


# 4\. Horizontal Bar Plot: Write a Python program to create a horizontal bar chart showing the number of students in different departments.
# import matplotlib.pyplot as plt

# departments = ['CS', 'IT', 'ENTC', 'Mechanical']
# students = [60, 50, 45, 35]

# plt.barh(departments, students)
# plt.xlabel('Number of Students')
# plt.ylabel('Departments')
# plt.title('Students in Departments')
# plt.show()

# 5\. Pie Chart: Write a Python program to create a pie chart showing the percentage distribution of students participating in different activities.
# import matplotlib.pyplot as plt

# activities = ['Sports', 'Music', 'Dance', 'Coding']
# students = [30, 20, 25, 25]

# plt.pie(students, labels=activities, autopct='%1.1f%%')
# plt.title('Student Activities')
# plt.show()

# 6\. Histogram: Write a Python program to create a histogram showing the distribution of marks obtained by students in an examination.
# import matplotlib.pyplot as plt

# marks = [45, 50, 55, 60, 65, 65, 70, 75, 80, 85, 90, 90]

# plt.hist(marks, bins=5, edgecolor='black')
# plt.xlabel('Marks')
# plt.ylabel('Number of Students')
# plt.title('Distribution of Marks')
# plt.show()

# # 7\. Multiple Plots: Write a Python program to display two plots in the same figure using Matplotlib subplots.
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y1 = [10, 20, 30, 40, 50]
# y2 = [5, 15, 25, 35, 45]

# plt.subplot(1, 2, 1)
# plt.plot(x, y1)
# plt.title('Line Plot')

# plt.subplot(1, 2, 2)
# plt.bar(x, y2)
# plt.title('Bar Plot')

# plt.tight_layout()
# plt.show()


# 8\. Plot Customization: Write a Python program to create a line plot with a title, axis labels, a legend, and a red-colored line.
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 30, 25]

# plt.plot(x, y, color='red', label='Sales')
# plt.xlabel('Days')
# plt.ylabel('Sales')
# plt.title('Daily Sales')
# plt.legend()
# plt.show()

# 9\. Save a Plot: Write a Python program to create a line graph and save it as a PNG image using `plt.savefig()`.
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y, marker='o')
# plt.title('Simple Line Graph')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# plt.savefig('line_graph.png')
# plt.show()

# 10\. 3D Plot: Write a Python program to create a simple 3D scatter plot using Matplotlib to visualize data along the X, Y, and Z axes.
# import matplotlib.pyplot as plt

# from mpl_toolkits.mplot3d import Axes3D

# x = [1, 2, 3, 4, 5]
# y = [5, 4, 3, 2, 1]
# z = [2, 4, 6, 8, 10]

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# ax.scatter(x, y, z)
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# ax.set_title('3D Scatter Plot')

# plt.show()