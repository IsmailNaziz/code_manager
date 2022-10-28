import datetime


class CodeWriter(object):
	"""docstring for CodeWriter
	for the moment let's suppose inputs are equal to attributes
	add private methods and public methods and class method, instance and class methods"""
	def __init__(self, class_name, parent_class_name, parent_class_file, user_name, attributes, \
						methods, project_path, file_name, imports, inputs):
		self.class_name = class_name
		self.parent_class_name = parent_class_name
		self.parent_class_file = parent_class_file
		self.attributes = attributes
		self.methods = methods
		self.inputs = inputs
		self.project_path = project_path
		self.path_file = self.project_path +'/'+file_name
		self.user_name = user_name
		self.imports = imports
		self._tab = '	'

	def create_parent_class(self):
		if self.parent_class_name is not None:
			CW = CodeWriter(self.parent_class_name, None, None, user_name, ['speed'], ['accelerate'], self.project_path, self.parent_class_file, [], ['speed'])
			CW.init_file()

	def init_file(self):
		self.create_parent_class()
		content = self._header_str() + self._imports_str() + self._class_declaration_str()\
					+ self._init_str() + self._empty_methods_str()
		with open(self.path_file, "a+") as f:
			f.truncate(0)
			f.write(content)
		return

	def update_file(self):
		return

	def _header_str(self):
		return f"# Creation date {datetime.datetime.now().isoformat(timespec='minutes')} \n# Author {self.user_name}"

	def _imports_str(self):
		imports_str = "\n\n"
		for this_import in self.imports:
			imports_str += f'\nimport {this_import}'
		if self.parent_class_name is not None:
			package = self.parent_class_file.split('.')[0]
			imports_str += f'\nfrom {package} import {self.parent_class_name}'
		return imports_str

	def _class_declaration_str(self):
		if self.parent_class_name is None:
			return f'''\n\nclass {self.class_name}(object): \n{self._tab}"""docstring for {self.class_name}"""'''
		else:
			return f'''\n\nclass {self.class_name}({self.parent_class_name}): \n{self._tab}"""docstring for {self.class_name}"""'''

	def _init_str(self):
		# add inheritance if parent class found
		def_init_func = f"\n\n{self._tab}def __init__(self,"
		init_attr = ""
		for this_input in inputs:
			def_init_func += f" {this_input},"
		for attr in self.attributes:
			init_attr += f"\n{self._tab}{self._tab}self.{attr} = {attr}"
		return f"{def_init_func[:-1]}):{init_attr}"

	def _empty_methods_str(self):
		methods_str = ""
		for method, arguments in methods.items():
			methods_str += f'\n\n{self._tab}def {method}(self,'
			for argument in arguments:
				methods_str += f' {argument},'
			methods_str = f"{methods_str[:-1]}):\n{self._tab}{self._tab}pass"
		return methods_str


if __name__ == "__main__":
	class_name = "Test"
	parent_class_file = 'parent_test.py'
	parent_class_name = 'ParentTest'
	user_name = 'Ismail Naziz'
	attributes = ["size", "time"]
	inputs = ["size", "time"]
	methods = {"calculate_time": ["speed", "distance"], "calculate_amount": ["unit_price"]}
	project_path = r"C:\Users\33768\Documents\Projects\code_manager\test"
	file_name = "generated_file.py"
	imports = ["pandas", "numpy"]
	CW = CodeWriter(class_name, parent_class_name, parent_class_file, user_name, attributes, methods, project_path, file_name, imports, inputs)
	CW.init_file()
