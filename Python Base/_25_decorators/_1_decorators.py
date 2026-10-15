def my_decorator(func):
    def wrapper():
        print("Smth is  happening before the func is called")
        func()
        print("Smth is  happening after the func is called")

    return wrapper

'''without sugar syntaxis (без синтаксического сахара)/декоратора'''
def say_hello_without_decorator():
    print("hello")

my_decorator(say_hello_without_decorator)()

print("\n")

'''c декоратором'''
@my_decorator
def say_hello():
    print("hello")
say_hello()

print("\n")


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello(*, name: str):
    print(f"Hello, {name}!")

say_hello(name="Sasha")

print("\n")

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper

@my_decorator
def add_numbers(*, a:int, b:int) -> int:
    print("Adding numbers...")
    return a + b

result = add_numbers(a=1, b=2)
print(result)
