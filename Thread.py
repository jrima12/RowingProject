import threading
import time

ls = []

def func(t):
    for i in range(1, t+1):
        ls.append(i)
        time.sleep(0.5)

def func2(t):
    for i in range(1, t+1):
        ls.append(i)
        time.sleep(0.5)

x = threading.Thread(target=func, args =(5,))
x.start()

#.join() wait for thread to finish before continuing with main. uncomment this and comment the other one to see different output
# x.join() 

y = threading.Thread(target=func2, args =(5,))
y.start()

x.join()
y.join()

print(ls)