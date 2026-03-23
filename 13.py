sentence = input("Enter a sentence: ")

cleaned = ''.join(ch.lower() for ch in sentence if ch.isalnum())

unique_chars = set()
duplicates = set()

for ch in cleaned:
    if ch in unique_chars:
        duplicates.add(ch)
    else:
        unique_chars.add(ch)

result = [ch for ch in cleaned if ch not in duplicates]
print("Unique characters:", ''.join(result))