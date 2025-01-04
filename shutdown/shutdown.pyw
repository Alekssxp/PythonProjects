import os
import time
shulink = "D:\\aleks\\Desktop\\py\\shutdown\\shutdown.exe.lnk"
def shutdown ():
    t = time.localtime()
    if t[6] < 4:
        if t[3] < 17 or t[3] > 21:
            os.startfile(shulink)
    elif t[6] == 5 or t[4]:
        if t[3] > 2 and t[3] < 14:
            os.system(shulink)
    elif t[6] == 6 and t[3] > 21:
        os.system(shulink)
# shutdown()
def test():
    os.system(shulink)
test()