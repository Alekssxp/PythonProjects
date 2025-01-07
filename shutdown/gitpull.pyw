import git
import os
import time
from time import sleep
shutdawn = 'D:\\aleks\\Desktop\\py\\shutdown\\shutdawn.pyw'
gitpull = 'D:\\aleks\\Desktop\\py\\shutdown\\gitpull.pyw'
dateModifyFileShut = os.path.getmtime(shutdawn)
dateModifyFileGit = os.path.getmtime(gitpull)
repoLocal = "D:\\aleks\\Desktop\\py"
repo = git.Repo(repoLocal)
origin = repo.remote(name='origin')
newModifyFileshut = dateModifyFileShut
newModifyFileGit = dateModifyFileGit
while dateModifyFileGit == newModifyFileGit:
    try:
        origin.pull()
        sleep(2)
        newModifyFileGit = os.path.getmtime(gitpull)
        if dateModifyFileGit != newModifyFileGit:
            os.startfile(gitpull)
            break
        else: 
            while newModifyFileshut == dateModifyFileShut:
                # repo = git.Repo(repoLocal)
                # origin = repo.remote(name='origin')
                try:
                    origin.pull()
                    newDateModifyFileShut = os.path.getmtime(shutdawn)
                    if dateModifyFileShut != newDateModifyFileShut:
                        os.startfile(shutdawn)
                    sleep(10)
                except Exception:
                    sleep(10)
                
    except Exception:
        sleep(10)





# try:
#     origin.pull()
#     os.startfile(shutdawn)
# except Exception:
#         sleep(10)
# i = 1
# while i < 5:
#     repo = git.Repo(repoLocal)
#     origin = repo.remote(name='origin')
#     try:
#         origin.pull()
#         newDateModifyFileShut = os.path.getmtime(shutdawn)
#         if dateModifyFileShut != newDateModifyFileShut:
#             os.startfile(shutdawn)
#         sleep(10)
#     except Exception:
#         sleep(10).
