
forbidden_words = ['hack', 'cheat', 'fake']


message = input("Enter the secret message: ")


count = 0


sanitized_message = message


for word in forbidden_words:
    occurrences = sanitized_message.lower().count(word)
    if occurrences > 0:
        count += occurrences

        sanitized_message = sanitized_message.replace(word, '****')


print("\nSanitized message:")
print(sanitized_message)
print(f"\nNumber of forbidden words found and replaced: {count}")
