# This script is for the lunch gang to find fud.
# Please use this wisely.
 
import argparse
import random


# Instantiate the argument parser.
parser = argparse.ArgumentParser(description='Find fudd for the lunch gang.')
 
# Add required arguments.
parser.add_argument('path_to_food_list', type=str, help='Add path to list of restaurants and their weights.')

# Parse incoming arguments.
args = parser.parse_args()

# Global scope for food dictionary.
food_options = {}
 
# Open text file with list of food places and their associated weights.
#	This program does not write to the text file.
with open(args.path_to_food_list, 'r') as file:
    # Create a dictionary (restaurant:weight).
    # Read each line of file and track its row number
    for row, line in enumerate(file, 1):
        # Don't worry about the comments or empty lines in the text file.
        if "#" not in line and len(line.strip()) != 0:
            food_to_weight = line.split(":");

            # Remove leading and trailing spaces or newline characters.
            food_to_weight = list(map(str.strip, food_to_weight))
            
            # A valid line in the text file should only contain two elements,
            #   the restaurant name and their associated weight.
            if len(food_to_weight) == 2:
                # Just making this readable :)
                food_place = food_to_weight[0]
                weight = int(food_to_weight[1])

                food_options[food_place] = weight
            else:
                print("Disregarding line number: ", row)


# Prep for RNGesus.
food_places = list(food_options.keys())
weights = list(food_options.values())

selected_option = random.choices(food_places, weights=weights, k=1)

print("RNGesus has chosen: ", selected_option[0])

