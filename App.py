import matplotlib.pyplot as plt
import numpy as np

# PF = open("PullForce.txt", "r").readlines()
y1 = open("PullForce.txt", "r").readlines()
y2 = [i.replace("\n","") for i in y1]
y = [float(j) for j in y2]

print(y)
x = np.linspace(0, len(y),num = 100)
# y = open("PullForce.txt", "r").readlines()

   
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
# line1, = ax.plot(x, y, 'b-')
ax.plot(x, y, 'b-')


ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
# for i in PF:
#     line1.set_ydata(i)
#     fig.canvas.draw()
#     fig.canvas.flush_events()