a = int(input("Enter a: "))
b = int(input("Enter b: "))

result = 1
for _ in range(b):
    temp = 0
    for _ in range(a):
        temp += result
    result = temp

print("Result:", result)
