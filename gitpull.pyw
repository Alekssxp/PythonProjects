import git
import os
from time import sleep
repoUrl = "https://github.com/Alekssxp/PythonProjects.git"
repoLocal = "D:\\aleks\\Desktop\\py"
repo = git.Repo(repoLocal)
origin = repo.remote(name='origin')
for i in range (10):
    try:
        origin.pull()
        os.startfile('D:\\aleks\\Desktop\\py\\shutdown.pyw')
    except Exception:
        sleep(10)
        continue