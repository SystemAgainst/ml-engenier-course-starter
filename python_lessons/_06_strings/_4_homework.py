"""
1) string.format(value1, value2, ...)
2) Different Ways to Escape percent (%) in Python strings
"""

# 1 string.format(value1, value2, ...)
name = "Emma"
age = 25
msg = "My name is {} and I am {} years old.".format(name, age)
print("string.format(value1, value2, ...): ", msg)  # Outputs: "My name is Emma and I am 25 years old."


# 2 Different Ways to Escape percent (%) in Python strings
website = "GFG"
"""
print("The percent is % and the website is %s."%(website) #When we try to use percent (%) as a string literal in a string we get this error: not enough arguments for format string
"""

#1. Using Double Percent (%%) for String Formatting
percentage = 50
format_string = "The success rate is %d%%." % percentage
print(format_string)  # Output: The success rate is 50%.


#2. Using f-strings
percentage = 75
formatted_string = f"The success rate is {percentage}%."
print(formatted_string)

#3. Using Raw Strings for Escaping
formatted_str = r"The success rate is %d%%." % 95
print(formatted_str)

#4. Using format() Method
percentage = 85
formatted_string = "The success rate is {}%.".format(percentage)
print(formatted_string)

#5. Using String Concatenation
percentage = 65
formatted_string = "The success rate is " + str(percentage) + "%"
print(formatted_string)