class InvalidRowNumberException(Exception):
	def __init__(self, message="The row number that you have inputted is not valid. Please try again."):
		self.message = message
		super().__init__(self.message)