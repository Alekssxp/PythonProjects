import git
import os
import time
from time import sleep
dateCreateFile = os.path.getmtime('D:\\aleks\\Desktop\\py\\shutdown\\shutdawn.pyw')
repoUrl = "https://github.com/Alekssxp/PythonProjects.git"
repoLocal = "D:\\aleks\\Desktop\\py"
repo = git.Repo(repoLocal)
origin = repo.remote(name='origin')
try:
    origin.pull()
    os.startfile('D:\\aleks\\Desktop\\py\\shutdown\\shutdawn.pyw')
except Exception:
        sleep(10)
i = 1
while i < 5:
    repo = git.Repo(repoLocal)
    origin = repo.remote(name='origin')
    try:
        origin.pull()
        newDateCreateFile = os.path.getmtime('D:\\aleks\\Desktop\\py\\shutdown\\shutdawn.pyw')
        if dateCreateFile != newDateCreateFile:
            os.startfile('D:\\aleks\\Desktop\\py\\shutdown\\shutdawn.pyw')
        sleep(10)
    except Exception:
        sleep(10)
