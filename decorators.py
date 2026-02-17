# Decorators are functions that modify the behavior of other functions.
# They are often used to add functionality to existing functions without modifying their code.
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("*********")
        func(*args, **kwargs)
        print("*********")
    return wrap_func

# We can use the decorator to modify the behavior of the say_hello function
@my_decorator
def say_hello(greeting="hi"):
    print(greeting)
say_hello("hellooooo")
say_hello()


# Create a performance decorator to measure the time is takes to execute a function
from time import time
def performance(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Time taken to execute {func.__name__}: {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        i * 5

long_time()


# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
        else:
            print("User is not authenticated")
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
user1['valid'] = True
message_friends(user1)