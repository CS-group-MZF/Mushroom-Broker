import math
import random
import time


seconds_left = 60


def create_array():
    return [[0 for _ in range(10)] for _ in range(10)]

def reset(array):
    for i in range(10):
        for j in range(10):
            array[i][j] = 0

def display(array):
    for row in array:
        print(' '.join(map(str, row)))

# this will be timed in the future too
def spawn_mushroom():
    x_pos = random.randint(0, 9)
    y_pos = random.randint(0, 9)
    array[x_pos][y_pos] = 1

def play_game():
    spawn_mushroom()
    display(array)
    destroy_mushroom()

# this will be reworked to be clicking instead
def destroy_mushroom():
    print("Type the coordinates of the mushroom to destroy")
    x_pos = int(input("Row:")) - 1
    y_pos = int(input("Column:")) - 1
    if(array[x_pos][y_pos] == 1):
      array[x_pos][y_pos] = 0
    else:
        print("Mushroom not found")
    play_game()


# Example usage
##array = create_array()
##display(array)  # Display the initial array (all zeros)
##print()
##reset(array)    # Reset the array (all zeros again)
##display(array)  # Display the array after reset



array = create_array()


spawn_mushroom()
display(array)
destroy_mushroom()











