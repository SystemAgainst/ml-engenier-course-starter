# яв-ся ли год високосным
year = 163
if year % 4 == 0 and year % 100 != 0:
  print(f"{year} is a leap year")
elif year % 400 == 0:
  print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year") 


# if not year % 4 and year % 100:
#     print("Year is leap")
# elif not year % 400:
#     print("Year is leap")
# else:
#     print("Year is not leap")