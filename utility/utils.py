from functools import wraps
def print_result(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} : {result}")
        return result
    return wrapper