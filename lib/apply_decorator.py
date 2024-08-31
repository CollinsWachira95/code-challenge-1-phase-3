def decorator_func(func):
    def wrapper():
        print("Decorator Applied")
        return func()
    return wrapper

def apply_decorator(func):
    return decorator_func(func)

def my_function():
    print("Original function called")

decorator_func = apply_decorator(my_function)
decorator_func()