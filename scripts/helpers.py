import time
from functools import wraps


def time_it(func):
    """
    The `time_it` function is a decorator that measures the execution time of a function and prints the
    elapsed time.

    Args:
      func: The `func` parameter is a function that we want to measure the execution time of.

    Returns:
      The function being returned is the wrapper function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"Time elapsed: {time.time() - start_time}")
        return result

    return wrapper
