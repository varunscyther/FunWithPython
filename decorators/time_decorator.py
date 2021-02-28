"""

Time decorator -
     Implement a decorator that calculates time of execution for covered function and prints it.

"""

# Built in modules
from functools import wraps
import time


def execution_timer(function) :

    """
    Calculate the execution time of function and prints it.

    Args:
        function (function) : Function to wrap.

    Returns :
        function: calculate function.

    """

    @wraps(function)
    def calculate_time(*args) :
        start_time = time.perf_counter()
        value = function(*args)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Finished {function.__name__!r} in {execution_time:.4f} secs")
        return value

    return calculate_time


@execution_timer
def time_decorator(n_items) :
    for _ in range(n_items) :
        sum([i ** 2 for i in range(2000)])


if __name__ == '__main__' :
    time_decorator(20000)
