################################################################################
 # Copyright (C) 2023 Analog Devices, Inc., All Rights Reserved.
 # 
 # This software is protected by copyright laws of the United States and
 # of foreign countries. This material may also be protected by patent laws
 # and technology transfer regulations of the United States and of foreign
 # countries. This software is furnished under a license agreement and/or a
 # nondisclosure agreement and may only be used or reproduced in accordance
 # with the terms of those agreements. Dissemination of this information to
 # any party or parties not specified in the license agreement and/or
 # nondisclosure agreement is expressly prohibited.
 #
 # The above copyright notice and this permission notice shall be included
 # in all copies or substantial portions of the Software.
 #
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
 # OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 # MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 # IN NO EVENT SHALL MAXIM INTEGRATED BE LIABLE FOR ANY CLAIM, DAMAGES
 # OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 # ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 # OTHER DEALINGS IN THE SOFTWARE.
 #
 # Except as contained in this notice, the name of Maxim Integrated
 # Products, Inc. shall not be used except as stated in the Maxim Integrated
 # Products, Inc. Branding Policy.
 #
 # The mere transfer of this software does not imply any licenses
 # of trade secrets, proprietary technology, copyrights, patents,
 # trademarks, maskwork rights, or any other form of intellectual
 # property whatsoever. Maxim Integrated Products, Inc. retains all
 # ownership rights.
 #
 ###############################################################################
 
# This a script for the lunch gang to find fud.
# Please use this wisely.
 
import argparse
import random
 
 
 
 
# Instantiate the argument parser.
parser = argparse.ArgumentParser(description='Find fudd for the lunch gang.')
 
# Add required arguments.
parser.add_argument('path_to_food_list', type=str, help='Add path to list of restaurants and their weights.')

# Parse incoming arguments.
args = parser.parse_args()

# Global scope for food dictionary
food_options = {}
 
# Open text file with list of food places and their associated weights.
#	This program does not write to the text file.
with open(args.path_to_food_list, 'r') as file:
    # Create a dictionary (restaurant:weight).
    # Read each line of file and track its row number
    for row, line in enumerate(file, 1):
        # Don't worry about the comments or empty in the text file.
        if "#" not in line and len(line.strip()) != 0:
            food_to_weight = line.split(":");

            # Remove leading to trailing spaces or new line characters.
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

