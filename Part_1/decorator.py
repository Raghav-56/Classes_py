def print_my_args(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with:")

        # Print positional arguments
        if args:
            print(f"  Positional arguments: {args}")

        # Print keyword arguments
        if kwargs:
            print(f"  Keyword arguments: {kwargs}")

        # Call the original function and return its result
        result = func(*args, **kwargs)
        print(f"  Return value: {result}")
        return result

    return wrapper


@print_my_args
def func(a, b, c):
    return a * b + c


func(2, 3, 4)

func(2, b=3, c=4)
