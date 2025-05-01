# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


padding = 0

# Set grid size to accommodate the pattern (1714x1647)
# N = 2048

PART_H_PATTERNS = [
    {
        'pattern_file': 'gosperglidergun.rle',
        'title': "Part H simulation gosperglidergun",
        'frames': 100
    },
    {
        'pattern_file': 'turingmachine.rle',
        'title': "Part H simulation turingmachine",
        'frames': 100
    }
]

#read RLE file
#~ with open("gosperglidergun.rle", "r") as text_file:
# with open("turingmachine.rle", "r") as text_file:
#         rleString = text_file.read()

# Terminal
def display_menu():
    print("Select a pattern to simulate:")
    print("1. TURING : Part H")
    print("2. Exit")
    return input("Enter your choice (1-2): ")

def display_part_h_menu():
    print("\n=== Part H: Select a Large Pattern ===")
    print("1. GGG")
    print("2. TURINGMACHINE")
    print("3. Back to Main Menu")
    return input("Enter your choice (1-3): ")

def read_pattern_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"\nError: File '{filename}' not found. Please ensure it is in the same folder as this script.")
        return None

def get_interval_input(pattern_name):
    while True:
        try:
            interval = int(input(f"\nEnter the interval for {pattern_name} (eg. 50): "))
            if interval <= 0:
                print("Interval must be a positive integer. Please try again.")
                continue
            return interval
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def turing_simulation(config, N, interval):
    # Create game of life object with fastMode=True
    life = conway.GameOfLife(N, fastMode=True)

    # Insert pattern into the grid to get the tiled dimensions
    pattern_str = read_pattern_file(config['pattern_file'])
    if pattern_str is None:
        return False

    pattern_height, pattern_width = life.insertFromRLE(pattern_str, pad=0)

    # Check if the pattern is valid
    if pattern_height == 0 or pattern_width == 0:
        print("Error: Failed to load pattern dimensions.")
        return False

    # Calculate padding to center the pattern
    pad_x = (N - pattern_width) // 2
    pad_y = (N - pattern_height) // 2

    # Clear the grid (since we inserted with pad=0, we need to reload with correct padding)
    life.grid = np.zeros((N, N), np.int64)
     # Insert the pattern into the actual grid with the calculated padding
    life.insertFromRLE(pattern_str, pad=(pad_y, pad_x))

    # get initial state
    cells = life.getStates()

    # Set up the animation
    fig = plt.figure()
    plt.gray()
    img = plt.imshow(cells, animated=True)

    # Zoom in on the pattern region (adjust based on pattern size and padding)
    zoom_size = max(pattern_width, pattern_height) + 50  # Add some margin
    plt.xlim(pad_x - 25, pad_x + zoom_size)
    plt.ylim(pad_y - 25, pad_y + zoom_size)

    def animate(i):
        """Perform animation step using evolve_two"""
        life.evolve_two()  #convolution
        cells_updated = life.getStates()
        img.set_array(cells_updated)
        return img,

    # Update title to include the user-specified N
    title = f"{config['title']} (N={N})"
    # Animate with the specified number of frames and interval
    ani = animation.FuncAnimation(fig, animate, frames=config['frames'], interval=interval, blit=True)
    plt.title(title)
    plt.show()
    return True

def main():
    global life
    config = None

    while True:
        choice = display_menu()

        if choice == '1':
            N = 2048
            config = None

            while True:
                part_h_choice = display_part_h_menu()
                if part_h_choice == '1':
                    print("\nRunning Part H GGG")
                    config = PART_H_PATTERNS[0]
                    break
                elif part_h_choice == '2':
                    print("\nRunning Part H Turing")
                    config = PART_H_PATTERNS[1]
                    break
                elif part_h_choice == '3':
                    print("\nReturning to main menu...")
                    break
                else:
                    print("\nInvalid choice. Please select a number between 1 and 3.")
            if config:
                title_parts = config['title'].split(": ")
                if len(title_parts) > 1:
                    pattern_name = title_parts[1]
                else:
                    pattern_name = config['title']
                interval = get_interval_input(f"{pattern_name} (N={N})")
                print(f"\nSimulating {pattern_name} with N={N} and interval {interval} ms...")
                if not turing_simulation(config, N, interval):
                    print("Simulation aborted due to file error.")
            return

        elif choice == '7':
            print("\nExiting the program. Goodbye!")
            return
        else:
            print("\nInvalid choice. Please select a number between 1 and 6.")

    # Prompt user for interval
    interval = get_interval_input(config['title'].split(": ")[1])

    #create the game of life object
    life = conway.GameOfLife(config['N'])

    # Insert the selected pattern
    # if pattern == 'glider':
    #     life.insertGlider((0, 0)) # How can you tell your code is working correctly?

    # elif pattern == 'glider_gun':
    #     life.insertGliderGun((0, 0)) # part C

    # elif pattern == 'plain_text' and config.get('pattern_file'):
    #     pattern_str = read_pattern_file(config['pattern_file'])
    #     if pattern_str is None:
    #         return  # Exit
    #     life.insertFromPlainText(pattern_str, pad=0)  # Part D


    # Get initial state
    cells = life.getStates()

    # Set up the animation
    fig = plt.figure()
    plt.gray()
    img = plt.imshow(cells, animated=True)

    def animate(i):
        """Perform animation step"""
        life.evolve()
        cells_updated = life.getStates()
        img.set_array(cells_updated)
        return img,

    #animate 24 frames with interval between them calling animate function at each frame
    ani = animation.FuncAnimation(fig, animate, frames=config['frames'], interval=interval, blit=True)
    plt.title(config['title'])
    plt.show()

if __name__ == "__main__":
    main()



#create the game of life object
# life = conway.GameOfLife(fastMode=True)
# pattern_height, pattern_width = life.insertFromRLE(rleString, padding)

# # Check if the pattern loaded successfully
# if pattern_height == 0 or pattern_width == 0:
#     print("Error: Failed to load Turing Machine pattern.")
#     exit()

# # Calculate padding to center the pattern
# pad_x = (N - pattern_width) // 2
# pad_y = (N - pattern_height) // 2

# # Clear the grid and re-insert the pattern with centered padding
# life.grid = np.zeros((N, N), np.int64)
# life.insertFromRLE(rleString, pad=(pad_y, pad_x))

# cells = life.getStates() #initial state

# #-------------------------------
# #plot cells
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# fig = plt.figure()

# plt.gray()

# img = plt.imshow(cells, animated=True)

#     # Zoom in on the pattern region (adjust based on pattern size and padding)
# zoom_size = max(pattern_width, pattern_height) + 50  # Add some margin
# plt.xlim(pad_x - 25, pad_x + zoom_size)
# plt.ylim(pad_y - 25, pad_y + zoom_size)

# def animate(i):
#     """perform animation step"""
#     global life

#     life.evolve_two()
#     cellsUpdated = life.getStates()

#     img.set_array(cellsUpdated)

#     return img,

# interval = 50 #ms

# #animate 24 frames with interval between them calling animate function at each frame
# ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)
# #~ animate(0)

# plt.show()
