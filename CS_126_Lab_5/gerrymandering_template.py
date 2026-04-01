# Building Python Programs
# Programming Project Chapter 6 Gerrymandering

# This program prompts the user for a state name and then outputs a chart 
# displaying the population of democrats and republicans in each district in 
# the state and whether or not that district is gerrymandered. If the user
# types in a state name that doesn't exist the program outputs a not found 
# message.

import turtle
from Lab5_functions import draw_line, draw_rect

WIDTH = 500
HEIGHT = 500

def main():

    setworldcoordinates(0, HEIGHT, WIDTH, 0)
    clear()
    shape('turtle')
    pencolor('olive drab')
    fillcolor('sienna')
    bgcolor('grey')

    print_intro_message()

    #### YOUR CODE GOES HERE #################
    #### Note - YOU CAN USE THE BELOW TEMPLATE or 
    #### YOU CAN WRITE YOU OWN CUSTOM FUNCTIONS ######

    # take state input

    # check if state exists or not

    # if exists, gather the total counts of dem, 
    # gop votes of all districts of the states

    # if not, print state not found


# function to output the introduction message to console.
def print_intro_message():
    pass

# function to print state name, eligible voters and 
# horizontal and vertical lines to panel
def draw_intro_graphics(state_name, eligible_voters):
    pass

# function to check whether state exists or not
# if exits, returns the state details line
def get_state_details(file_name, state_name):
    pass

# function to process the state details in the format:
# <state>,<district1>,<dem votes>,<gop votes>,<district2>,<dem votes>,<gop votes>,...
# calculate and return total dem and gop votes
# also prints the district graphics to the panel
def process_state_details(state_details):
    pass

# function which caluculate the width of dem_votes and gop_votes
# and print the rectangles to the panel using the y_index as starting point
def draw_district_graphics(dem_votes, gop_votes, y_index):
    pass

# function to check whether the votes are gerrymandered or not
# and prints out a message if the state is gerrymandered.
# If it is, prints out who has gerrymandered it
def is_gerrymandered(dem_votes, gop_votes):
    pass

# takes the total number of dem votes and total number of gop
# votes as parameters and calculates and returns the
# total wasted dem votes and total wasted gop votes
def calculate_wastage(dem, gop):
    pass

    ##########################################

main()