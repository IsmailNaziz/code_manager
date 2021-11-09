class ClassManager(object):
	
	"""docstring for ClassManager
		This is my doc for Class Manager
		"""
	def __init__(self, arg):
		self.arg = arg

	def run(self):
		return


if __name__ == "__main__":
	my_doc = ClassManager.__doc__
	method_list = [func for func in dir(ClassManager) if callable(getattr(ClassManager, func))]
	print(my_doc)
	print(method_list)	
	print(method_list[0].__doc__)