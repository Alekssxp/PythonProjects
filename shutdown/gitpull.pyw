import git
import os
import time
from time import sleep
dateCreateFile = os.path.getmtime('D:\\aleks\\Desktop\\py\\shutdown\\shutdawn.pyw')
repoUrl = "https://github.com/Alekssxp/PythonProjects.git"
repoLocal = "D:\\aleks\\Desktop\\py"
i = 1
def repo():
    repo = git.Repo(repoLocal)
    origin = repo.remote(name='origin')
    try:
        origin.pull()
        os.startfile('D:\\aleks\\Desktop\\py\\shutdown\\shutdawn.pyw')
        sleep(10)
    except Exception:
        sleep(10)
repo()
while i < 5:
    newDateCreateFile = os.path.getmtime('D:\\aleks\\Desktop\\py\\shutdown\\shutdawn.pyw')
    if dateCreateFile != newDateCreateFile:
        repo()