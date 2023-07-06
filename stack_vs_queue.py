# Program creates a visual representation of a stack vs a queue

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.patches import Rectangle

# Create a figure and axis
fig, ax = plt.subplots()

# Set axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Remove axis ticks and labels
ax.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)

# Create a stack
stack = []
ax.text(2.5, 0.5, 'Stack: LIFO', fontsize=10, ha='center', va='center')
for i in range(5):
    rect = Rectangle((2, 1+i), 1, 1, fc='w', ec='k')
    ax.add_patch(rect)

# Create a queue
queue = []
ax.text(7.5, 0.5, 'Queue: FIFO', fontsize=10, ha='center', va='center')
for i in range(5):
    rect = Rectangle((7, 1+i), 1, 1, fc='w', ec='k')
    ax.add_patch(rect)

# Create a list of the numbers to be used
numbers = [54, 26, 93, 17, 77]

# total number of frames
TOTAL_FRAMES = 12
stack_text = ax.text(2.5, 7.5, '', fontsize=10, ha='center', va='center')
queue_text = ax.text(7.5, 7.5, '', fontsize=10, ha='center', va='center')


# Defining the update function
def update(frame_number):
    '''Function to update the animation'''
    if frame_number < 5:
        # Add a rectangle to the stack
        stack_text.set_text(f'stack.push({numbers[frame_number]})')
        srect = Rectangle((2, 1+frame_number), 1, 1, fc='c', ec='k')
        stext = ax.text(
                2.5, 1.5+frame_number, numbers[frame_number],
                fontsize=10, ha='center', va='center')
        ax.add_patch(srect)
        stack.append([srect, stext])

        # Add a rectangle to the queue
        queue_text.set_text(f'queue.append({numbers[frame_number]})')
        qrect = Rectangle((7, 1+frame_number), 1, 1, fc='c', ec='k')
        qtext = ax.text(
                7.5, 1.5+frame_number, numbers[frame_number],
                fontsize=10, ha='center', va='center')
        ax.add_patch(qrect)
        queue.append([qrect, qtext])
    elif frame_number == 5:
        stack_text.set_text('')
        queue_text.set_text('')
    elif frame_number == 6:
        stack_text.set_text(f'stack.pop() -> {stack[-1][1].get_text()}')
        queue_text.set_text(f'queue.pop(0) -> {queue[0][1].get_text()}')
        stack[-1][0].set_fc('tomato')
        queue[0][0].set_fc('tomato')
    else:
        print(len(stack), len(queue))
        # Remove a rectangle from the queue
        if queue:
            qrect, qtext = queue.pop(0)
            qrect.remove()
            qtext.remove()
            if queue:
                queue_text.set_text(f'queue.pop(0) -> {queue[0][1].get_text()}')
                queue[0][0].set_fc('tomato')
        # Remove a rectangle from the stack
        if stack:
            srect, stext = stack.pop()
            srect.remove()
            stext.remove()
            if stack:
                stack_text.set_text(f'stack.pop() -> {stack[-1][1].get_text()}')
                stack[-1][0].set_fc('tomato')
        if frame_number == TOTAL_FRAMES-1:
            stack_text.set_text('')
            queue_text.set_text('')


def init():
    '''Function to initialize the animation'''
    pass


ani = animation.FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000,
                              repeat=False, init_func=init)
plt.show()
