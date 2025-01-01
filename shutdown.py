import os
import time

t = time.localtime()
def shutdown ():
    if t[6] < 4 and t[3] < 17 or t[3] > 21:
        os.startfile('D:\\aleks\\Desktop\\shutdown.exe.lnk')
    elif t[6] < 7 and t[3] > 2 and t[3] < 14:
        os.startfile('D:\\aleks\\Desktop\\shutdown.exe.lnk')
    elif t[6] == 6 and t[3] > 21:
        os.startfile('D:\\aleks\\Desktop\\shutdown.exe.lnk')
shutdown()
