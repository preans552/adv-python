a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division: Cannot divide by zero")

print(f"{a} is", "Even" if a % 2 == 0 else "Odd")
print(f"{b} is", "Even" if b % 2 == 0 else "Odd")

print("Float conversion of first integer:", float(a))