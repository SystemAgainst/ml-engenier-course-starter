user_roles = ("admin", "editor", "viewer")
print(user_roles)  # Outputs: ("admin", "editor", "viewer")
print(len(user_roles)) # Outputs: 3

for role in user_roles:
  print(role)

print("admin" in user_roles) # Outputs: True
print("writer" in user_roles) # Outputs: False

print(user_roles[1]) # Outputs: editor
# user_roles[1] = "author"  # TypeError: 'tuple' object does not support item assignment

'''когда создаешь коржет с одинм элементом через скобку, то будет тип строка'''
not_tuple = ("admin")
print(type(not_tuple)) # <class 'str'>

my_tuple = ("admin", )
print(type(my_tuple)) # <class 'tuple'>

'''распаковка кортежа'''
role_1, role_2, role_3 = user_roles
print(role_1)  # Outputs: "admin"
print(role_2)  # Outputs: "editor"
print(role_3)  # Outputs: "viewer"

user_roles = ["admin", "editor", "viewer"]  # with lists it works too
role_1, role_2, role_3 = user_roles
print(role_1)  # Outputs: "admin"
print(role_2)  # Outputs: "editor"
print(role_3)  # Outputs: "viewer"

role_1, role_2, _ = user_roles
print(role_1)  # Outputs: "admin"
print(role_2)  # Outputs: "editor"
