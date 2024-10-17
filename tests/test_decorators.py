### test for decorators.py

# Example use case, to be used in every input() calls
@input_validation(lambda x: x.isdigit())
def get_input(prompt):
    return input(prompt)

# Example test case for age
age = get_input("Enter your age: ")

# Would it be better to refactor use case and test case?