# Traditional way of creating a list with squares of numbers
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)  # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = [x ** 2 for x in range(10)]
print(squares)  # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print("\n")

even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x ** 2)
print(even_squares) 

even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)

print("\n")

numbers = [1, 2, 3, 4, 5]
labeled_numbers = []

for num in numbers:
    if num % 2 == 0:
        labeled_numbers.append("even")
    else:
        labeled_numbers.append("odd")
print(labeled_numbers)

labeled_numbers = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(labeled_numbers)

print("\n")

square_dict = { x: x ** 2 for x in range(10) }
print(square_dict)

print("\n")

matrix = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9], 
]
'''
transpose_matrix = [
    [1, 4, 7],
    [2, 5, 8], 
    [3, 6, 9], 
]
'''
transpose_matrix = []

for i in range(len(matrix)): 
    transpose_row = []
    for row in matrix:
        transpose_row.append(row[i])
    transpose_matrix.append(transpose_row)
print(transpose_matrix)

transpose_matrix_lh = [[row[i] for row in matrix] for i in range(len(matrix))]
print(f"transpose_matrix with list comprehension: {transpose_matrix_lh}")