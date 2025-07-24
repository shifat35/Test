paragraph = input("Enter a paragraph: ").lower()

vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for char in paragraph:
    if char in vowel_counts:
        vowel_counts[char] += 1

print("\nVowel counts:")
for vowel in 'aeiou':
    print(f"{vowel}: {vowel_counts[vowel]}", end=' ')
