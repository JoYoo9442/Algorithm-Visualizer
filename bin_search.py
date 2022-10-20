import math
import matplotlib.patches as mpatches
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

    global colors
    global start
    global end
    global mid

    print(start, end)
    plt.bar(data, data, color = colors, edgecolor = colors)

    colors[start] = 'green'
    colors[end] = 'green'
    colors[mid] = 'green'

    if target == data[mid]:
        colors[mid] = 'blue'
        # ani.event_source.stop()
    else:
        if target < data[mid]:
            end = mid
        elif target > data[mid]:
            start = mid
        mid = start + math.floor((end-start)/2)

        colors[start] = 'red'
        colors[end] = 'red'
        colors[mid] = 'orange'

fig, ax = plt.subplots()
red_patch = mpatches.Patch(color='red', label='Start and End Indexes')
orange_patch = mpatches.Patch(color='orange', label='Middle Value')
blue_patch = mpatches.Patch(color='blue', label='Search Target Found')
ax.legend(handles=[red_patch, orange_patch, blue_patch])
ax.set_title(f"Target:{target}")

plt.bar(data, data, color = colors, edgecolor = colors)

ani = FuncAnimation(fig, update, frames=7, interval=1000)
ani.save("bin_search.gif", writer='Pillow', fps=60)

# plt.show()
