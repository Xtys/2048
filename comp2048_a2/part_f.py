import conway
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define pattern
pulsar = """
.......OOO...OOO.......
.......................
.......................
.......................
....O....O.O....O.....
....O....O.O....O.....
....O....O.O....O.....
.......OOO...OOO.......
.......................
.......OOO...OOO.......
....O....O.O....O.....
....O....O.O....O.....
....O....O.O....O.....
.......................
.......................
.......................
.......OOO...OOO.......
.......................
.......................
.......................
.......................
"""

# Split and clean the Pulsar pattern
pulsar_rows = [row for row in pulsar.strip().split('\n') if row]
pulsar_height = len(pulsar_rows)  # 21
pulsar_width = 21

# Ensure each row is exactly 21 characters
pulsar_rows = [row.ljust(pulsar_width, '.')[:pulsar_width] for row in pulsar_rows]

# Create a 512x512 pattern with only the Pulsar in the center
pattern_size = 512
pattern = np.full((pattern_size, pattern_size), '.', dtype='<U1')  # All dead cells
start_row = (pattern_size - pulsar_height) // 2  # 245
start_col = (pattern_size - pulsar_width) // 2  # 245

for i in range(pulsar_height):
    for j in range(pulsar_width):
        pattern[start_row + i, start_col + j] = pulsar_rows[i][j]

pattern_str = '\n'.join(''.join(row) for row in pattern)

# Set up the simulation
N = 2048
life = conway.GameOfLife(N)
life.insertFromPlainText(pattern_str, pad=0)  # Insert at (0,0)
cells = life.getStates()

# Animation with zoom centered on the Pulsar
fig = plt.figure()
plt.gray()

# Zoom to a 50x50 region centered on the Pulsar (245, 245) to (266, 266)
zoom_start = start_row - 15  # 230
zoom_end = start_row + 35    # 280
pulsar_region = cells[zoom_start:zoom_end, zoom_start:zoom_end]  # 50x50 region
im = plt.imshow(pulsar_region, animated=True)

def update(i):
    life.evolve_two()
    cells_updated = life.getStates()
    im.set_array(cells_updated[zoom_start:zoom_end, zoom_start:zoom_end])
    return im,

ani = animation.FuncAnimation(fig, update, frames=50, interval=10, blit=True)
plt.title("Simulation (2048x2048) with 512x512 Pattern")
plt.show()
