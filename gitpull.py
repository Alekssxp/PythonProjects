import git
import os
repoUrl = "https://github.com/Alekssxp/PythonProjects.git"
repoLocal = "D:\\aleks\\Desktop\\py"
repo = git.Repo(repoLocal)
origin = repo.remote(name='origin')
origin.pull()
os.startfile('D:\\aleks\\Desktop\\py\\shutdown.py')