import subprocess
import time
import git
from git import Repo
import os

workfolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(workfolder)
pushfolder = 'D:\\push'
    
def shut ():
    subprocess.run(['shutdown', '/p', '/f'], creationflags=subprocess.CREATE_NO_WINDOW)

def shutdown ():
    t = time.localtime()
    if t[6] < 4:
        if t[3] < 17 or t[3] > 21:
            shut()
    elif t[6] == 5 or t[6] == 4:
        if t[3] > 2 and t[3] < 14:
            shut ()
    elif t[6] == 6:
        if t[3] > 21:
            shut ()
        elif t[3] > 2 and t[3] < 14:
            shut ()
def push():

    try:
        repoFolder = Repo.init(pushfolder)
        repoFolder.create_remote(name='origin', url='https://github.com/Alekssxp/PythonProjects.git')
        repoFolder.git.add('.')
        repoFolder.git.commit('-m', 'update')
        repoFolder.git.branch('-m', 'test')
        repoFolder.git.push('-u', 'origin', 'test')
    except:
        repoFolder.git.add('.')
        repoFolder.git.commit('-m', 'update')
        repoFolder.git.push()

def list():
    os.mkdir(pushfolder)
    with open(pushfolder+'\\log.txt', 'w') as f:
        for i in os.listdir('D:\\'):
            print(i, file=f)
# shutdown()
def test():
    shut ()
# test()
# push()
list()
