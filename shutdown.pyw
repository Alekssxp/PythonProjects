import os
import time

def shutdown ():
    t = time.localtime()
    if t[6] < 4:
        if t[3] < 17 or t[3] > 21:
            os.system("shutdown /p /f")
    elif t[6] < 7 and t[3] > 2 and t[3] < 14:
        os.system("shutdown /p /f")
    elif t[6] == 6 and t[3] > 21:
        os.system("shutdown /p /f")
# shutdown()
def test():
    os.system("shutdown /p /f")
test()