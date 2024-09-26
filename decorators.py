def input_validation(validation_function):
    def decorator(function):
        def wrapper(*args, **kwargs):
            while True:
                # function() takes in args and kwargs
                value = function(*args, **kwargs)
                # validation_function() is the function that is used to validate the input
                if validation_function(value):
                    return value
                else:
                    print("Invalid input, please try again.")
        return wrapper
    return decorator

# Example use case, to be used in every input() calls
@input_validation(lambda x: x.isdigit())
def get_input(prompt):
    return input(prompt)

age = get_input("Enter your age: ")