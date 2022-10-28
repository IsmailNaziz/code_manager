import subprocess

class VEnvManager(object):
	"""docstring for VEnvManager
	doc pour utiliser l'API + efficace https://docs.python.org/fr/3/library/venv.html"""

	def __init__(self, project_path, venv_name):
		self.project_path = project_path
		self.venv_name = venv_name


	def create_venv(self):
		command = "python3 -m venv {}".format(self.project_path+'/'+self.venv_name)
		return self._cmd_runner(command)

	def source_venv(self):
		command = "source {}/bin/activate".format(self.project_path+'/'+self.venv_name)
		return self._cmd_runner(command)

	def install_lib(self, lib):
		command = "python3 -m pip install {}".format(lib)
		return self._cmd_runner(command)

	def install_libs(self, libs):
		for lib in libs:
			command = "python3 -m pip install {}".format(lib)
			if not(self._cmd_runner(command)):
				return 0, lib
		return 1
		
	@classmethod
	def _cmd_runner(cls, command):
		command_list = command.split(' ')
		try:
			subprocess.run(command_list)
		except Exception as e:
			return 0
		return 1

	def update_requirements(self):
		command = 'pip3 freeze > requirements.txt'
		return self._cmd_runner(command)

	def install_venv(self):
		return


if __name__ == "__main__":
	project_path = "/home/ismail/Documents/code_manager/test"
	venv_name = 'venv'
	VEM = VEnvManager(project_path, venv_name)
	VEM.create_venv()
	VEM.source_venv()
	VEM.install_lib('pandas')
		
