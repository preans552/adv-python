words = ["madam", "hello world", "racecar", "python programming", "level"]

sorted_words = sorted(words, key=len)
print("Sorted by length:", sorted_words)

palindromes = [w for w in words if w == w[::-1]]
print("Palindromes:", palindromes)

hyphenated = [w.replace(" ", "-") for w in words]
print("Spaces replaced with hyphens:", hyphenated)