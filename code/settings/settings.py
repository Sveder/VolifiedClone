import os

#-------------------------------------------------------------------------------
#Debug parameters:
#-------------------------------------------------------------------------------
DEBUG = True

SHOULD_LOG_TO_FILE = True
LOG_FILE = os.path.join(os.curdir, "logs", "last_run.log")



BACKGROUND_FILL_COLOR  = (0 , 0 , 50)
BLACK = (0 , 0 , 0)
MAX_POINTS_BEFORE_LINE = 75

SCREEN_SIZE = (800 , 600)                   #The size of the game window
GAME_BOARD_SIZE = (760 , 530)               #The size of the game board
BG_RECT = [20 , 50 , 760 , 530]             #Size of the bg image - to allow full ship view


PLAYER_MOVE_SPEED = 5                       #Number of pixels the player moves
                                            #on a single key press
                                            
D_UP = "up"
D_DOWN = "down"
D_RIGHT = "right"
D_LEFT = "up"

DIRECTIONS_DICT = {D_UP: 1 ,
                   D_RIGHT : 2 ,
                   D_DOWN : 3 ,
                   D_LEFT : 4}



#-------------------------------------------------------------------------------
#Paths and files
#-------------------------------------------------------------------------------
ASSETS_DIRECTORY = os.path.join(os.curdir, "assets")

MAIN_CONFIG = os.path.join(ASSETS_DIRECTORY, "game.ini")

IMAGE_FOLDER = os.path.join(ASSETS_DIRECTORY, "images")

BACKGROUND_SPACE_IMAGE_PATH = os.path.join(IMAGE_FOLDER, "BGSpace.jpg")
PLAYER_SHIP_IMAGE_PATH = os.path.join(IMAGE_FOLDER, "player_ship.gif")