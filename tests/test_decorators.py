### decorators.py

def input_validation(validation_func):
	def decorator(func):
		def wrapper(*args, **kwargs):
			value = func(*args, **kwargs)
			if validation_func(value):
				return value
			print("Invalid input, please try again.")
		return wrapper
	return decorator