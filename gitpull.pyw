import git
import os
from time import sleep
# repoUrl = "https://github.com/Alekssxp/PythonProjects.git"
repoLocal = "D:\\aleks\\Desktop\\py"
repo = git.Repo(repoLocal)
origin = repo.remote(name='origin')
i = 1
while i < 1:
    i -= 1
    try:
        origin.pull()
        os.startfile('D:\\aleks\\Desktop\\py\\shutdown.pyw')
    except Exception:
        sleep(10)