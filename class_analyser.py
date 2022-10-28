import os
import sys

class  ClassAnalyser(object):
	"""docstring for ClassAnalyser"""
	def __init__(self, file_folder, file_name, class_name):
		sys.path.append(file_folder)

	def import_class(self):
		os.chdir()