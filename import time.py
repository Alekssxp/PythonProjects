import time
p = time.localtime()
for t in range(len(p)):
    print(t, '=', time.localtime()[t])
# print(len(p))