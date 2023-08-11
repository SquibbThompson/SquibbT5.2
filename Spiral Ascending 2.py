import itertools

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# convert binary string to matrix
def string_to_bin_matrix(bin_string):
    return [[int(bit) for bit in line] for line in bin_string.split('\n') if line]

binary_string = """
0000000011111111
0001100011100111
0010010011011011
0011110011000011
0100001010111101
0101101010100101
0110011010011001
0111111010000001
1000000101111110
1001100101100110
1010010101011010
1011110101000010
1100001100111100
1101101100100100
1110011100011000
1111111100000000

""".strip()


# generate initial state
initial_state = np.array(string_to_bin_matrix(binary_string))

# define the function that checks and updates the matrix
def update_matrix(matrix):
    updated_matrix = matrix.copy()
    height, width = matrix.shape

# loop over each cell in the matrix
    for i in range(height):
        for j in range(width):
        # check the number of black cells surrounding the current cell
            n_1 = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if (x, y) != (i, j) and x >= 0 and y >= 0 and x < height and y < width:
                        if matrix[x, y] == 1:
                            n_1 += 1

        # invert the cell color if a white cell borders 2 black cells
        if matrix[i, j] == 0 and n_1 == 2:
            updated_matrix[i, j] = 1
        elif matrix[i, j] == 1 and n_1 % 2 == 1:
            # turn two horizontal/vertical black cells to white
            if i > 0 and matrix[i - 1, j] == 1:
                updated_matrix[i - 1, j] = 0
            if j > 0 and matrix[i, j - 1] == 1:
                updated_matrix[i, j - 1] = 0
            if i < height - 1 and matrix[i + 1, j] == 1:
                updated_matrix[i + 1, j] = 0
            if j < width - 1 and matrix[i, j + 1] == 1:
                updated_matrix[i, j + 1] = 0
    return updated_matrix

# generate initial state
initial_state = np.array(string_to_bin_matrix(binary_string))

# User input for number of frames and interval
n_frames = int(input("Enter the number of frames: "))
interval = int(input("Enter the interval in milliseconds: "))

# animate cellular automata evolution
def animate(i):
    global initial_state

    # reset state after n_frames
    if i % n_frames == 0:
        initial_state = np.array(string_to_bin_matrix(binary_string))

    initial_state = update_matrix(initial_state)
    plt.imshow(initial_state, cmap='binary')

fig, ax = plt.subplots()
# set frames to None for infinite loop
ani = animation.FuncAnimation(fig, animate, frames=None, interval=interval)
plt.show()



