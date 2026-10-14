counter = 1
while counter <= 5:
  print(f"Counter is: {counter}")
  counter += 1

print("\n")

my_list = [0, 1, 2]
while my_list:
  el = my_list.pop()
  print(f"element: {el}")
print(my_list)

print("\n")

'''бесконечный цикл'''
#while True:
#  print("Infinite loop")

while True:
  answer = input("Enter a number: ")
  if answer == "quit":
    break
  print(f"You entered: {answer}")