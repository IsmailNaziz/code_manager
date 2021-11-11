class GitHubManager(object):
	"""docstring for GitManager
	https://gist.github.com/c0ldlimit/4089101
	"""
	def __init__(self, git_user_name, token_file, url_repo, commit_comment):
		self.git_user_name = git_user_name
		self.token_file = token_file
		self.url_repo = url_repo
		self.token = self._get_token(token_file)
		self.commit_comment = commit_comment

	def first_push(self):
		touch_read, git_init, git_add_read_me, git_commit  = "touch README.md",\
															"git init",\
															 "git add README.md",\
															 'git commit -m "{}"'.format(self.commit_comment)
		self._cmd_runner(touch_read)
		self._cmd_runner(git_init)
		self._cmd_runner(git_add_read_me)
		self._cmd_runner(git_commit)
		self.git_push()


	def _get_token(self, token_file):
		with open(token_file, "r") as f:
			token = f.read()
		return token
	
	def git_push(self):
		git_remote_add = "git remote add origin {}".format(self.url_repo)
		git_push = "git push -u origin master"
		self._cmd_runner(git_remote_add)
		self._cmd_runner(git_push)

	def git_status(self):
		git_status = "git status"
		self._cmd_runner(git_push)

	def git_pull(self, commit):
		return

	def git_commit(self, comment=None):
		if comment==None:
			git_commit='git commit -m "{}"'.format(self.commit_comment)
			self._cmd_runner(git_commit)
		else:
			git_commit='git commit -m "{}"'.format(comment)
			self._cmd_runner(git_commit)

	@classmethod
	def _cmd_runner(cls, command):
		command_list = command.split(' ')
		try:
			subprocess.run(command)
		except Exception as e:
			return 0
		return 1

