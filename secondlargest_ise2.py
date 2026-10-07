
n = int(input("Enter number of elements: "))
a = []
for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

largest = a[0]
second = a[0]

for x in a:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x

print("Second largest =", second)
