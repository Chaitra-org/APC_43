def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice: "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print("Answer =", add(a, b))

elif choice == 2:
    print("Answer =", sub(a, b))

elif choice == 3:
    print("Answer =", mul(a, b))

elif choice == 4:
    print("Answer =", div(a, b))

else:
    print("Invalid choice")