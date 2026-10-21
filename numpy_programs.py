# 1. Write a Python program using NumPy to create a one-dimensional array containing 10
# integers and display the array, its size, data type, and number of dimensions.

# import numpy as np

# arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# print("Array:", arr)
# print("Size:", arr.size)
# print("Data type:", arr.dtype)
# print("Number of dimensions:", arr.ndim)


# 2. Create two NumPy arrays of 5 integers each. Perform and display:
#  Addition
#  Subtraction
#  Multiplication
#  Division
#  Modulus

# import numpy as np

# a = np.array([10, 20, 30, 40, 50])
# b = np.array([2, 4, 5, 8, 10])

# print("Array A:", a)
# print("Array B:", b)

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Modulus:", a % b)


# 3. Create a NumPy array containing 10 numbers. Find and display the maximum, minimum,
# sum, and average of the elements.

# import numpy as np

# arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# print("Array:", arr)
# print("Maximum:", np.max(arr))
# print("Minimum:", np.min(arr))
# print("Sum:", np.sum(arr))
# print("Average:", np.mean(arr))

# 4. Create a NumPy array of integers from 1 to 20. Use Boolean indexing to separate and
# display the even and odd numbers.

# import numpy as np

# arr = np.arange(1, 21)

# even = arr[arr % 2 == 0]
# odd = arr[arr % 2 != 0]

# print("Array:", arr)
# print("Even numbers:", even)
# print("Odd numbers:", odd)

# 5. Create a one-dimensional array containing numbers from 1 to 12. Reshape it into:
#  2 × 6 matrix
#  3 × 4 matrix
#  4 × 3 matrix

# import numpy as np

# arr = np.arange(1, 13)

# print("Original Array:")
# print(arr)

# print("\n2 x 6 Matrix:")
# print(arr.reshape(2, 6))

# print("\n3 x 4 Matrix:")
# print(arr.reshape(3, 4))

# print("\n4 x 3 Matrix:")
# print(arr.reshape(4, 3))

# 6. Create two 3 × 3 NumPy matrices and perform matrix addition.

# import numpy as np

# a = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])

# b = np.array([[9, 8, 7],
#               [6, 5, 4],
#               [3, 2, 1]])

# print("Matrix A:")
# print(a)

# print("Matrix B:")
# print(b)

# print("Addition:")
# print(a + b)


# 7. Create two compatible matrices using NumPy and perform matrix multiplication using an
# appropriate NumPy function.

# import numpy as np

# a = np.array([[1, 2],
#               [3, 4]])

# b = np.array([[5, 6],
#               [7, 8]])

# print("Matrix A:")
# print(a)

# print("Matrix B:")
# print(b)

# result = np.dot(a, b)

# print("Matrix Multiplication:")
# print(result)


# 8. Create a 3 × 4 matrix and display its transpose.

# import numpy as np

# a = np.array([[1, 2, 3, 4],
#               [5, 6, 7, 8],
#               [9, 10, 11, 12]])

# print("Original Matrix:")
# print(a)

# print("Transpose:")
# print(a.T)

# 9. Create a 4 × 4 NumPy array and write a program to:
#  Display the first row
#  Display the last column
#  Display the diagonal elements
#  Display the elements from the second and third rows
# import numpy as np

# a = np.array([[1, 2, 3, 4],
#               [5, 6, 7, 8],
#               [9, 10, 11, 12],
#               [13, 14, 15, 16]])

# print("Array:")
# print(a)

# print("First row:")
# print(a[0])

# print("Last column:")
# print(a[:, -1])

# print("Diagonal elements:")
# print(np.diag(a))

# print("Second and third rows:")
# print(a[1:3])

# 10. Create a 4 × 4 matrix and calculate the sum of each row and each column separately.\
# import numpy as np

# a = np.array([[1, 2, 3, 4],
#               [5, 6, 7, 8],
#               [9, 10, 11, 12],
#               [13, 14, 15, 16]])

# print("Matrix:")
# print(a)

# print("Sum of each row:")
# print(np.sum(a, axis=1))

# print("Sum of each column:")
# print(np.sum(a, axis=0))


# 11. Create a NumPy array containing numbers from 1 to 20. Using slicing, display:
#  First 5 elements
#  Last 5 elements
#  Alternate elements
#  Elements in reverse order
# import numpy as np

# a = np.arange(1, 21)

# print("Array:")
# print(a)

# print("First 5 elements:")
# print(a[:5])

# print("Last 5 elements:")
# print(a[-5:])

# print("Alternate elements:")
# print(a[::2])

# print("Reverse order:")
# print(a[::-1])


# 12. Create an array of 10 integers. Replace all elements greater than 50 with 0 using NumPy
# Boolean indexing.
# import numpy as np

# a = np.array([10, 25, 55, 40, 75, 30, 90, 45, 60, 20])

# print("Original array:")
# print(a)

# a[a > 50] = 0

# print("After replacement:")
# print(a)

# 13. Create an unsorted NumPy array and display it in:
#  Ascending order
#  Descending order
import numpy as np

a = np.array([45, 12, 89, 23, 67, 5, 34])

print("Original array:")
print(a)

print("Ascending order:")
print(np.sort(a))

print("Descending order:")
print(np.sort(a)[::-1])


# 14. Create an array containing duplicate values. Find and display only the unique elements.
# import numpy as np

# a = np.array([10, 20, 10, 30, 20, 40, 30, 50, 40])

# print("Original array:")
# print(a)

# print("Unique elements:")
# print(np.unique(a))


# 15. Create two NumPy arrays and concatenate them horizontally and vertically.
# 
import numpy as np

# a = np.array([[1, 2],
#               [3, 4]])

# b = np.array([[5, 6],
#               [7, 8]])

# print("Horizontal Concatenation:")
# print(np.hstack((a, b)))

# print("Vertical Concatenation:")
# print(np.vstack((a, b)))

# import numpy as np

# a= np.array([[1,3],
#             [4,6]])

# b= np.array([[10,36],
#             [42,64]])

# print(np.hstack((a,b)))