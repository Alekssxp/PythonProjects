import git
import os
from time import sleep
repoUrl = "https://github.com/Alekssxp/PythonProjects.git"
repoLocal = "D:\\aleks\\Desktop\\py"
i = 1
while i < 5:
    repo = git.Repo(repoLocal)
    origin = repo.remote(name='origin')
    try:
        origin.pull()
        os.startfile('D:\\aleks\\Desktop\\py\\shutdown\\shutdawn.pyw')
        os.system('shutdown /s')
        sleep(10)
    except Exception:
        sleep(10)
