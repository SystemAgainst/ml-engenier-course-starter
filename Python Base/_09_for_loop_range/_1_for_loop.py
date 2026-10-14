file_names = ["document1.txt", "image1.jpg", "document2.txt", "image2.jpg"]

for file_name in file_names:
    print(file_name)

print("\n")

greeting = 'Hello, World!'
count_o = 0
for char in greeting:
    if char == "o":
        count_o += 1
        print(char)
print(count_o)

print("\n")

students = ["Alice", "Bob", "Charlie", "David"]
for student in students:
  print(student)
  for char in student:
    print(char)

print("\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for num in numbers:
  if num % 2 == 0:
    continue
  print(num)

print("\n")

for num in numbers:
  if num == 10:
    break
  print(num)

print("\n")


