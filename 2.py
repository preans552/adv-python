sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
vowel_count = sum(1 for ch in sentence if ch in vowels)
consonant_count = sum(1 for ch in sentence if ch.isalpha() and ch not in vowels)

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

print("Reversed:", sentence[::-1])

print("Spaces replaced:", sentence.replace(" ", "_"))

print("Capitalized:", sentence.title())