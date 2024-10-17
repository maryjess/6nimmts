class InvalidRowNumberException(Exception):
	def __init__(self, message="The row number that you have inputted is not valid. Please try again."):
		self.message = message
		super().__init__(self.message)

class CardNotInHandException(Exception):
	def __init__(self, message="The card that you have inputted is not in your hand! Please try again."):
		self.message = message
		super().__init__(self.message)

class CardParseError(Exception):
	def __init__(self, message="The card format you've entered is invalid. Please try again."):
		self.message = message
		super().__init__(self.message)