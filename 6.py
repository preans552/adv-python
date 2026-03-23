mixed_tuple = (5, "hello", 12, 3.5, 8, 20, "world")
mixed_list = list(mixed_tuple)

filtered_list = [x for x in mixed_list if not (isinstance(x, int) and x < 10)]

filtered_tuple = tuple(filtered_list)
print("Filtered tuple:", filtered_tuple)