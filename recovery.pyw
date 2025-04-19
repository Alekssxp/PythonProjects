import os
import git
from time import sleep

workFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(workFolder)

while True:
    isGitfetch = os.path.isfile('..\\Pictures\\gitfetch.pyw')
    if isGitfetch != True:
        while True:
            try:
                try:
                    repo = git.Repo.init(workFolder)
                    repo.git.fetch('origin', 'shutdown')
                    repo.git.reset('--hard', 'FETCH_HEAD')
                    break
                except:
                    repo = git.Repo.init(workFolder)
                    repo.create_remote('origin', 'https://github.com/Alekssxp/PythonProjects.git')
                    origin = repo.remotes.origin
                    repo.git.fetch('origin', 'shutdown')
                    repo.git.reset('--hard', 'FETCH_HEAD')  
                    break  
            except: 
                sleep(10)
        os.chdir('..')
        os.rename("\\".join([workFolder, 'gitfetch.pyw']), "\\".join([os.getcwd(), 'Pictures\\gitfetch.pyw']))
        os.startfile('Pictures\\gitfetch.pyw')
        os.chdir(workFolder)
    else:
        sleep(30)