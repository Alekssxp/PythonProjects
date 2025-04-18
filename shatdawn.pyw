import subprocess
import time

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
# shutdown()
def test():
    shut ()
test()
