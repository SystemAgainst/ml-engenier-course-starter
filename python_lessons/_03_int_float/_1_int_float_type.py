"""numbers in Python (int, float)"""
my_integer = 10
my_float = 10.5


"""operators in Python"""
result_add = 5 + 3
result_sub = 5 - 3
result_mul = 5 * 3
result_div = 5 / 3  # Output: 1.6666666666666667

result_floor_div = 5 // 3  # Output: 1; equivalent 1!!! * 3 + 2  
result_mod = 5 % 3  # Output: 2; equivalent 1 * 3 + 2!!! 
result_exp = 5 ** 3  # Output: 125

"""converting between int and float in Python"""
my_int = 1
my_float = float(my_int)  # Convert int to float
print(my_float)  # Output: 1.0

my_float2 = 1.5
my_int2 = int(my_float2)  # Convert float to int (truncates decimal part)
print(my_int2)  # Output: 1 

rounded_int = round(my_float2)  # Round float to nearest int
print(rounded_int)  # Output: 2
print("####")