"""

Caching decorator -
    Implement decorator to store input arguments and result for the covered function.
    If arguments are not presented in the history, call the covered function, otherwise return the result from the history.

"""

# Built in modules
from functools import wraps
import logging

# Initialize logger
logging.basicConfig()
_LOGGING_LEVEL = logging.DEBUG
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(_LOGGING_LEVEL)


def cached(function) :
    """Store the arguments and result in cache and user cache.

    Args:
        function (function) : Function to wrap.

    Returns :
        function: Caching function.

    """
    cache = {}

    @wraps(function)
    def enabled_caching(*args) :

        """Enable caching and manage cache.

        Args:
            args (multiple) : Arguments to perform calculation.

        Returns :
            function: Cached function to execute.

        """

        signature = (function, args)

        _LOGGER.debug("Enabled caching for : %s ", signature)

        if signature in cache :
            _LOGGER.debug("Retrieving from cache for : %s ", signature)
            result = cache[signature]
        else :
            _LOGGER.debug("Calculating : %s ", signature)
            result = function(*args)
            _LOGGER.debug("Adding to cache : %s ", signature)
            cache[signature] = result
        return result

    return enabled_caching


@cached
def addition(number1, number2) :
    result = number1 + number2
    return result


@cached
def multiplication(number) :
    result = number * number
    return result


if __name__ == '__main__' :

    addition(100, 100)
    addition(100, 100)
    multiplication(200)
    multiplication(200)

