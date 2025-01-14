import os
import time
shucom = 'shutdown /p /f'
def shutdown ():
    t = time.localtime()
    if t[6] < 4:
        if t[3] < 17 or t[3] > 21:
            os.system(shucom)
    elif t[6] == 5 or t[6] == 4:
        if t[3] > 2 and t[3] < 14:
            os.system(shucom)
    elif t[6] == 6:
        if t[3] > 21:
            os.system(shucom)
        elif t[3] > 2 and t[3] < 14:
            os.system(shucom)
# shutdown()
def test():
    os.system(shucom)
# test().
