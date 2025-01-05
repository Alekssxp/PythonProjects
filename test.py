import os
from time import sleep
pathFile = "D:\\aleks\\Desktop\\py\\test.py"
dataModify = os.path.getmtime(pathFile)
newDataModify = dataModify
while dataModify == newDataModify:
    newDataModify = os.path.getmtime(pathFile)
    print(dataModify, newDataModify)
    sleep(10)
print(newDataModify, 'hws')