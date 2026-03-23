mixed_tuple = (1, "hello", 3.5, True, 42)

numeric_values = tuple(x for x in mixed_tuple if isinstance(x, (int, float)))
print("Numeric values:", numeric_values)

try:
    mixed_tuple[0] = 99
except TypeError as e:
    print("Error:", e)

tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
concatenated = tuple1 + tuple2
print("Concatenated tuple:", concatenated)