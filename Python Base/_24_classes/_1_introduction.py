my_string = "Hello, World!"
print(type(my_string))  # Output: <class 'str'>
print(type(str))  # Output: <class 'type'>
'''
str - это класс
my_string = "Hello, World!" – это экземпляр

list - это класс
my_list = list() – это экземпляр

Синонимы к слову "экземпляр":
1. Инстанс
2. Объект
'''

'''создание собственного класса'''
class MyClass:
    pass


print(type(MyClass))  # Output: <class 'type'>; это экземпляр класса type
my_class = MyClass() # экземпляр класса MyClass
print(type(my_class))  # Output: <class '__main__.MyClass'> 
