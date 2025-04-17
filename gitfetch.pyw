import git
import os
from time import sleep

workFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(workFolder)

shatdawn = "\\".join([workFolder, "shatdawn.pyw"])
gitfetch = "\\".join([workFolder, "gitfetch.pyw"])
try:
    dateModifyFileShat = os.path.getmtime(shatdawn)
    dateModifyFileGit = os.path.getmtime(gitfetch)

    newModifyFileShat = dateModifyFileShat
    newModifyFileGit = dateModifyFileGit
finally:

    while True:
        try:
            try:
                repo = git.Repo.init(workFolder)
                repo.git.fetch('origin', 'shutdown')
                repo.git.reset('--hard', 'FETCH_HEAD')
            except:
                repo = git.Repo.init(workFolder)
                repo.create_remote('origin', 'https://github.com/Alekssxp/PythonProjects.git')
                origin = repo.remotes.origin
                repo.git.fetch('origin', 'shutdown')
                repo.git.reset('--hard', 'FETCH_HEAD')    
        except: 
            sleep(10)
        newDateModifyFileShat = os.path.getmtime(shatdawn)
        if dateModifyFileShat != newDateModifyFileShat:
                os.startfile(shatdawn)
        sleep(10)
