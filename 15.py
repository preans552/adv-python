s = input("Enter a string: ")
is_palindrome = s == s[::-1]

vowels = "aeiouAEIOU"
vowel_count = consonant_count = digit_count = special_count = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    elif ch.isdigit():
        digit_count += 1
    else:
        special_count += 1

print("Palindrome:", is_palindrome)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Digits:", digit_count)
print("Special characters:", special_count)