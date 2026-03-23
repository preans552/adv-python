def custom_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

b = int(input("Enter base: "))
e = int(input("Enter exponent: "))
print(f"{b}^{e} = {custom_power(b, e)}")