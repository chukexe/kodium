
#   Decide the dimensions of the matrix
#   Display the matrix
#   Place current number in the center of the matrix
#   Choose direction
#   Update current number
#   Move to the next cell
#   Update steps to next cell
#   Place current number in the cell
#   Update move variable
#   Compare steps and move values
#       if same
#           change direction
#       else
#           continue

import numpy as np
from collections import Counter
from itertools import cycle

print('''
    This program aims to create a matrix with a range of numbers
    - starting from 1 - spiralling from the center of the matrix.
    You get to choose the dimension of the square matrix,
    but the length of the sides must be an odd number.
''')

# Check for oddness
while True:
  try:
    side_length = int(input("Please, enter an odd number: "))
    if side_length % 2 == 1:                                    
      break                                                     # Valid input, exit the loop
    else:
      print("Invalid input. ", end = ' ')
  except ValueError:
    print("Invalid input. Please, enter an integer.")

#   Creating the matrix
matrix = [[None] * side_length for _ in range(side_length)]

#   creating a Numpy array
matrix_np = np.array(matrix)

#   Set the central coordinates of the matrix to variables x and y
x = int((side_length - 1)/2)
y = int((side_length - 1)/2)

#   Initialize variables
current_number = 1
direction = "up"
move = 0
steps = 0
step_logger = []
count = 0

# List of directions
directions = ['right', 'down', 'left', 'up']

'''
To create the spiral, for each pair of directions, each step is made twice.
and then the step is incremented by 1 for the next pair, and this will continue
until the last number is placed in a cell in the matrix.
'''

# Use Counter to count occurrences of steps

def count_items(items_list, target_element):
    """Counts the occurrences of a target element in a list.

    Args:
        items_list: A list of items.
        target_element: The element to count.

    Returns:
        The count of the target element in the list.
    """

    return Counter(items_list).get(target_element, -1)



# Create a cyclic iterator from the list
dir_iter = cycle(directions)


#   Generating the spiral
while current_number < (side_length ** 2) + 1:

    #   Fill each cell
    matrix_np[x, y] = current_number
        
    if move == steps:
        direction = next(dir_iter)
        step_logger.append(steps)
        count = count_items(step_logger, steps)
        if count == 2 or len(step_logger) == 1:
            steps += 1
        move = 1                              # Resets move
    else:
        move += 1

    #   Positioning the numbers in the cells
    if direction == "right":
        y+=1
    elif direction == "down":
        x+=1
    elif direction == "left":
        y-=1
    else:
        x-=1
        
    current_number += 1

#   Final display
print(matrix_np)           
    
