# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
# import conway

# N = 64

# #create the game of life object
# life = conway.GameOfLife(N)
# # life.insertBlinker((0,0))
# # part B
# life.insertGlider((0,0)) #option 1
# # part C
# # life.insertGliderGun((0,0)) #swap this when option 2
# cells = life.getStates() #initial state

# # #-------------------------------
# # #plot cells
# # import matplotlib.pyplot as plt
# # import matplotlib.animation as animation

# fig = plt.figure()

# plt.gray()

# img = plt.imshow(cells, animated=True)

# def animate(i):
#     """perform animation step"""
#     global life

#     life.evolve()
#     cellsUpdated = life.getStates()

#     img.set_array(cellsUpdated)

#     return img,

# interval = 50 #ms

# #animate 24 frames with interval between them calling animate function at each frame
# ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)

# plt.show()

import conway
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration each pattern
CONFIG = {
    'part_b': {
        'N': 64,
        'frames': 24,
        'title': "Part B: Glider (N=64)"
    },
    'part_c': {
        'N': 64,
        'frames': 24,
        'title': "Part C: Gosper Glider Gun (N=64)"
    },
    'part_d_simkin': {
        'N': 64,
        'frames': 120,  # Increased to observe Glider production
        'pattern_file': '36-cell single-barreled gun.txt',
        'title': "Part D: 36 Cell Single Barreled Gun (N=64)"
    },
    'part_d_lobster': {
        'N': 64,
        'frames': 24,
        'pattern_file': 'lobster.txt',
        'title': "Part D: Lobster (N=64)"
    },
    'part_d_loafer': {
        'N': 64,
        'frames': 24,
        'pattern_file': 'sysn.txt',
        'title': "Part D: Loafer Synthesis (N=64)"
    }
}

PART_E_PATTERNS = [
    {
        'N': 64,
        'pattern_file': 'jason_p22.txt',
        'title': "Part E: Jason's p22 (20x20, N=64)",
        'frames': 44
    },
    {
        'N': 64,
        'pattern_file': 'p20_gliderless_gun.txt',
        'title': "Part E: Period-20 Gliderless Gun (20x20, N=64)",
        'frames': 40
    },
    {
        'N': 64,
        'pattern_file': 'Period-156 glider gun.txt',
        'title': "Part E: Period-156 Glider Gun (43x42, N=64)",
        'frames': 156  # least one cycle
    }
]

# Part F patterns (large patterns for N > 1024)
PART_F_PATTERNS = [
    {
        'pattern_file': 'P110_tj.txt',
        'title': "Part F simulation",
        'frames': 100
    }
]

# Terminal
def display_menu():
    print("Select a pattern to simulate:")
    print("1. Glider : Part B")
    print("2. Gosper Glider Gun : Part C")
    print("3. Part D - Plain Text Patterns")
    print("4. Part E - Multiple Patterns >=20x20")
    print("5. Part F - Fast Mode Simulation with Large Grid (N > 1024)")
    print("6. Exit")
    return input("Enter your choice (1-6): ")

def display_part_d_menu():
    print("\n=== Part D: Pattern  Selection ===")
    print("1. Simkin Glider Gun (36-cell single-barreled gun)")
    print("2. Lobster")
    print("3. Loafer Synthesis")
    print("4. Back to Main Menu")
    return input("Enter your choice (1-4): ")

def display_part_f_menu():
    print("\n=== Part F: Select a Large Pattern ===")
    print("1. P110")
    print("2. Back to Main Menu")
    return input("Enter your choice (1-2): ")

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

def get_grid_size_input():
    while True:
        try:
            N = int(input("\nEnter the grid size N (must be > 1024, e.g., 2048): "))
            if N <= 1024:
                print("Grid size N must be greater than 1024. Please try again.")
                continue
            return N
        except ValueError:
            print("Invalid input. Please enter a positive integer greater than 1024.")

def run_simulation(config, interval):
    # Create the game of life object
    life = conway.GameOfLife(config['N'])

    # Insert the pattern
    pattern_str = read_pattern_file(config['pattern_file'])
    if pattern_str is None:
        return False
    life.insertFromPlainText(pattern_str, pad=0)

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

    # Animate with the specified number of frames and interval
    ani = animation.FuncAnimation(fig, animate, frames=config['frames'], interval=interval, blit=True)
    plt.title(config['title'])
    plt.show()
    return True


def run_fast_simulation(config, N, interval):
    # Create the game of life object with fastMode=True
    life = conway.GameOfLife(N, fastMode=True)

    # Insert the pattern
    pattern_str = read_pattern_file(config['pattern_file'])
    if pattern_str is None:
        return False
    life.insertFromPlainText(pattern_str, pad=0)

    # Get initial state
    cells = life.getStates()

    # Set up the animation
    fig = plt.figure()
    plt.gray()
    img = plt.imshow(cells, animated=True)

    def animate(i):
        """Perform animation step using evolve_two"""
        life.evolve_two()  # Use evolve_two for fast mode
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
            print("\nRunning simulation with Glider pattern...")
            pattern = 'glider'
            config = CONFIG['part_b']
            break
        elif choice == '2':
            print("\nRunning simulation with Gosper Glider Gun pattern...")
            pattern = 'glider_gun'
            config = CONFIG['part_c']
            break
        elif choice == '3':
            while True:
                part_d_choice = display_part_d_menu()
                if part_d_choice == '1':
                    print("\nRunning Part D with Simkin Glider Gun...")
                    pattern = 'plain_text'
                    config = CONFIG['part_d_simkin']
                    break
                elif part_d_choice == '2':
                    print("\nRunning Part D with Lobster...")
                    pattern = 'plain_text'
                    config = CONFIG['part_d_lobster']
                    break
                elif part_d_choice == '3':
                    print("\nRunning Part D with Loafer Synthesis...")
                    pattern = 'plain_text'
                    config = CONFIG['part_d_loafer']
                    break
                elif part_d_choice == '4':
                    print("\nReturning to main menu...")
                    break
                else:
                    print("\nInvalid choice. Please select a number between 1 and 4.")
            if config:
                break
        elif choice == '4':
            print("\nRunning Part E: Demonstrating multiple patterns...")
            for pattern_config in PART_E_PATTERNS:
                pattern_name = pattern_config['title'].split(": ")[1]
                interval = get_interval_input(pattern_name)
                print(f"\nSimulating {pattern_name} with interval {interval} ms...")
                if not run_simulation(pattern_config, interval):
                    print("Simulation aborted due to file error.")
                    break
            return
        elif choice == '5':
            print("\nRunning Part F: Fast mode simulation with large grid...")
            # Prompt user for grid size N
            N = get_grid_size_input()
            config = None

            while True:
                part_f_choice = display_part_f_menu()
                if part_f_choice == '1':
                    print("\nRunning Part F...")
                    config = PART_F_PATTERNS[0]
                    break
                elif part_f_choice == '2':
                    print("\nReturning to main menu...")
                    break
                else:
                    print("\nInvalid choice. Please select a number between 1 and 2.")
            if config:
                title_parts = config['title'].split(": ")
                if len(title_parts) > 1:
                    pattern_name = title_parts[1]
                else:
                    pattern_name = config['title']
                interval = get_interval_input(f"{pattern_name} (N={N})")
                print(f"\nSimulating {pattern_name} with N={N} and interval {interval} ms...")
                if not run_fast_simulation(config, N, interval):
                    print("Simulation aborted due to file error.")
            return
        elif choice == '6':
            print("\nExiting the program. Goodbye!")
            return
        else:
            print("\nInvalid choice. Please select a number between 1 and 6.")

    # Prompt user for interval
    interval = get_interval_input(config['title'].split(": ")[1])

    #create the game of life object
    life = conway.GameOfLife(config['N'])

    # Insert the selected pattern
    if pattern == 'glider':
        life.insertGlider((0, 0)) # How can you tell your code is working correctly?

    elif pattern == 'glider_gun':
        life.insertGliderGun((0, 0)) # part C

    elif pattern == 'plain_text' and config.get('pattern_file'):
        pattern_str = read_pattern_file(config['pattern_file'])
        if pattern_str is None:
            return  # Exit
        life.insertFromPlainText(pattern_str, pad=0)  # Part D


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
