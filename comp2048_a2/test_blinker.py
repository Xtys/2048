import numpy as np
from conway import GameOfLife

# Vertical Blinker RLE string
blinker_rle = """#N Blinker
x = 1, y = 3, rule = B3/S23
o$o$o!"""

# Initialize a 5x5 grid to accommodate the 1x3 pattern with padding
game = GameOfLife(N=5, finite=True)

# Insert the blinker from RLE with padding=1
game.insertFromRLE(blinker_rle, pad=1)

# Print initial state
print("Initial Blinker State (from RLE, vertical):")
print(game.getGrid())

# Evolve one generation
game.evolve()
print("\nAfter 1 generation (should be horizontal):")
print(game.getGrid())

# Evolve another generation
game.evolve()
print("\nAfter 2 generations (should be vertical again):")
print(game.getGrid())
