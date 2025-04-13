import git
import os
workFolder = os.path.dirname(os.path.abspath(__file__))
os.chdir(workFolder)


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
