# Path-Finding-Project
A project of path finding visualization using pygame

# Requirements
* pygame

# Intruction
## Run the Main.py file.
This screen will open:

The board will open in sterile mode (1 on guide Image), **until changing the mode no editing can be made**.

Guide Image:


## Tile Number Editing
To increase or decrease the amount of tiles on board use the '+' and '-' button (5 on Guide Image) to change the number shown.\
After reaching the wanted number click the reset button (6 on Guide Image) to apply the changes

## Editing Board

### Setting Destination
1. Click the 'choose destination' option (2 on Guide Image)
2. Click a "regular" tile (colored white) on the board, it will change color as depicted in 9 on the Guide Image.

**Clicking a destination tile again while on 'choose destination' mode will set it as a "regular" tile again.**

### Setting Starting Points
1. Click the 'choose starting point' option (2 on Guide Image)
2. Click a "regular" tile (colored white) on the board, it will change color as depicted in 8 on the Guide Image.

**Clicking a destination tile again while on 'choose starting point' mode will set it as a "regular" tile again.**

### Switching tiles On/Off
1. Click the 'toggle button on/off' option (2 on Guide Image)
2.  * Click a "regular" tile (colored white) on the board, it will change color as depicted in 7 on the Guide Image, and will be switched off.
    * Click an "off" tile (7 on Guide Image) on the board, it will change color to white and will be switched on.


**Off tiles will be treated as obstacles in the algorithm**

### Choose Algorithm
Click on the wanted algorithm (4 on Guide Image).

## Run the Algorithm
After finishing the editing and setting the algorithm, click the 'play' option (3 on Guide Image).\
The algorithm will run, **DO NOT PRESS ANYTHING UNTIL IT IS FINISHED**.\
After the algorithm finished running the board will enter **Sterile Mode**, in order to reset the board press 'reset graph' (6 on Guide Image)
