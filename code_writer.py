import datetime


class CodeWriter(object):
	"""docstring for CodeWriter
	for the moment let's suppose inputs are equal to attributes
	add private methods and public methods and class method, instance and class methods"""
	def __init__(self, class_name, parent_class_name, user_name, attributes, \
						methods, project_path, file_name, imports, inputs):
		self.class_name = class_name
		self.parent_class_name = parent_class_name
		self.attributes = attributes
		self.methods = methods
		self.inputs = inputs
		self.path_file = project_path+'/'+file_name
		self.user_name = user_name
		self.imports = imports


	def init_file(self):
		content = self._header_str() + self._imports_str() + self._class_declaration_str()\
					+ self._init_str() + self._empty_methods_str()

		# print('header', self._header_str())
		# print('imports', self._imports_str())
		# print('declaration', self._class_declaration_str())
		# print('init', self._init_str())
		# print('methods', self._empty_methods_str())
		open('file.txt', 'w').close()
		with open(self.path_file,"a+") as f:
			f.truncate(0)
			f.write(content)
		return

	def update_file(self):
		return 


	def _header_str(self):
		return "# Creation date {} \n # Author {}".format(datetime.datetime.now().isoformat(timespec='minutes'),\
			self.user_name)

	def _imports_str(self):
		imports_str = ""
		for this_import in self.imports:
			imports_str += '\nimport {}'.format(this_import)
		return imports_str

	def _class_declaration_str(self):
		if self.parent_class_name == None:
			return '''\n\nclass {}(object): \n """docstring for {}"""'''.format(self.class_name, self.class_name)
		else:
			return '''\n\nclass {}({}): \n """docstring for {}"""'''\
					.format(self.class_name, self.parent_class_name, self.class_name)


	def _init_str(self):
		def_init_func = "\ndef __init__(self,"
		init_attr = ""
		for this_input in inputs:
			def_init_func += " {},".format(this_input)
		for attr in self.attributes:
			init_attr += "\nself.{} = {}".format(attr, attr)
		def_init_func = def_init_func[:-1]+'):'

		return def_init_func+init_attr

	def _empty_methods_str(self):
		methods_str = ""
		for method, arguments in methods.items():
			methods_str += '\ndef {}(self,'.format(method)
			for argument in arguments:
				methods_str += ' {},'.format(argument)
			methods_str= methods_str[:-1]+'):\npass'
		return methods_str


if __name__ == "__main__":
	class_name = "Test"
	parent_class_name = 'ParentTest'
	user_name = 'Ismail Naziz'
	attributes = ["size", "time"]
	inputs = ["size", "time"]
	methods = {"calculate_time": ["speed", "distance"], "calculate_amount": ["unit_price"]}
	project_path = "/home/ismail/Documents/code_manager/test" 
	file_name = "test.py"
	imports = ["pandas", "numpy"]
	CW = CodeWriter(class_name, parent_class_name, user_name, attributes, \
						methods, project_path, file_name, imports, inputs)
	CW.init_file()