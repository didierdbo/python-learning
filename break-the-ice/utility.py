from time import time
def performance(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Time taken to execute {func.__name__}: {end_time - start_time:.8f} seconds")
        return result
    return wrapper