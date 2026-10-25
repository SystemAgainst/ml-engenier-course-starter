'''для произвольной строки посчитай количество символов, слов и уникальных букв
'''


text = input("Введите строку: ")
characters_count = len(text)
words_count = len(text.split())
unique_letters = {char.lower() for char in text if char.isalpha()}

print(f"Количество символов: {characters_count}")
print(f"Количество слов: {words_count}")
print(f"Количество уникальных букв: {len(unique_letters)}")