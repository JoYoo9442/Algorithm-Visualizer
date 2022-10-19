import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n = 100
target = 32

data = []
for i in range(1, n+1):
    data.append(i)

colors = ['green']*n

start = 0
end = n-1
mid = math.floor(end/2)

colors[start] = 'red'
colors[end] = 'red'
colors[mid] = 'orange'

def update(frame):
    global start
    global end
    global mid

    colors[start] = 'green'
    colors[end] = 'green'
    colors[mid] = 'green'

    if target == data[mid]:
        colors[mid] = 'blue'
        ani.event_source.stop()
    else:
        if target < data[mid]:
            end = mid
        elif target > data[mid]:
            start = mid
        mid = start + math.floor((end-start)/2)

        colors[start] = 'red'
        colors[end] = 'red'
        colors[mid] = 'orange'

    plt.bar(data, data, color = colors)

fig = plt.figure()

plt.bar(data, data, color = colors)

ani = FuncAnimation(fig, update, frames=len(colors), interval=1000)

plt.show()
