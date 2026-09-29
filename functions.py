##1.Write a function factorial(n) that accepts an integer and returns its factorial.

#def factorial(n):
#   fact = 1
  #  for i in range(1, n + 1):
   #     fact = fact * i
    #return fact

#n = int(input("Enter a number: "))
#print("Factorial =", factorial(n))

##2. Write a function check_even_odd(n) that determines whether a given number is even or
##odd.

#def check_even_odd(n):
#    if n%2==0:
#        print("even number")
#    else:
#        print("odd number")

#n=int(input("enter a num: "))
#check_even_odd(n)

##3. Define a function that accepts two numbers and returns the greater number.

#def greater(a,b):
#    if a>b:
#        print(" ",a,"is greater")
#    else:
#        print(" ",b,"is greater")

#a=int(input("enter 1st number"))
#b=int(input("enter 2nd num"))

#greater(a,b)

##4. Create a function simple_interest(p, r, t) to calculate simple interest.

#def simp_int(p,r,t,):
#    si= (p*r*t)/100
#    return si
#p=float(input("enter principle amount: "))
#r=float(input("enter rate: "))
#t=float(input("enter period: "))

#print("simple interest = ",simp_int(p,r,t,))

##5. Write a function is_prime(n) that returns True if a number is prime; otherwise, returns
#False.

#def is_prime(n):
#    if n <= 1:
#        return False

#    for i in range(2, n):
#        if n % i == 0:
 #           return False
#    return True
#n = int(input("Enter a number: "))

#if is_prime(n):
#    print("Prime number")
#else:
#    print("Not a prime number")


##6. Define a function to calculate the area of a circle using its radius.

#def area_cir(r):
#    area= 3.14 * r* r
#    return area
#r=float(input("enter radius of circle"))
#print("area of circle= ",area_cir(r))


##7. Write a function that accepts n and returns the sum of the first n natural numbers.
#def sum_natural(n):
#    sum = 0
#    for i in range(1, n + 1):
#        sum = sum + i
#    return sum

#n = int(input("Enter n: "))
#print("Sum =", sum_natural(n))

##8. Create a function power(base, exponent) to calculate the value of base raised to exponent.
#def power(base, exponent):
#    return base ** exponent
#base = int(input("Enter base: "))
#exponent = int(input("Enter exponent: "))
#print("Result =", power(base, exponent))


#9. Write a function that accepts a list of numbers and returns the largest element without
#using the built-in max() function.
#def largest(numbers):
#   large = numbers[0]
#
#    for i in numbers:
#        if i > large:
#            large = i

#    return large
#numbers = [10, 25, 7, 45, 18]
#print("Largest element =", largest(numbers))

##10. Define a function that accepts a string and returns the number of vowels present in it.
#def count_vowels(s):
#   count = 0

#    for ch in s:
#        if ch in "aeiouAEIOU":
#            count = count + 1

#    return count

#s = input("Enter a string: ")

#print("Number of vowels =", count_vowels(s))

#--------lambda function------#
##33. Write a lambda function to calculate the square of a given number.
square = lambda n: n * n

n = int(input("Enter a number: "))
print("Square =", square(n))

##34. Create a lambda function that returns the cube of a number.

cube = lambda n: n * n * n

n = int(input("Enter a number: "))
print("Cube =", cube(n))

##35. Write a lambda function that returns True if a number is even and False otherwise.
even = lambda n: n % 2 == 0

n = int(input("Enter a number: "))
print(even(n))

##36. Use a lambda function to find the maximum of two numbers.

maximum = lambda a, b: a if a > b else b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Maximum =", maximum(a, b))


##37. Create a lambda function to calculate simple interest using principal, rate, and time.

simple_interest = lambda p, r, t: (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest =", simple_interest(p, r, t))

##38. Take a list of numbers, use map() and a lambda function to generate a list containing their
##squares.
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda n: n * n, numbers))

print("Squares =", squares)


##39. Use map() with lambda to calculate the cube of every element in a list.

numbers = [1, 2, 3, 4, 5]

cubes = list(map(lambda n: n * n * n, numbers))

print("Cubes =", cubes)

##40. Take two lists of numbers, use map() and lambda to create a third list containing the sum
##of corresponding elements.

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

result = list(map(lambda a, b: a + b, list1, list2))

print("Sum =", result)S
