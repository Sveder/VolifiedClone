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
                                            

class Direction:
    def __init__(self, in_words, angle_modifier, move_modifier):
        self.in_words = in_words
        self.move_modifier = move_modifier
        self.angle_modifier = angle_modifier
    
    def __repr__(self):
        return "Direction %s" % self.in_words


D_UP =    Direction("up",    1, (0, -1))
D_RIGHT = Direction("right", 2, (1, 0))
D_DOWN =  Direction("down",  3, (0, 1))
D_LEFT =  Direction("left",  4, (-1, 0))


#-------------------------------------------------------------------------------
#Paths and files
#-------------------------------------------------------------------------------
ASSETS_DIRECTORY = os.path.join(os.curdir, "assets")

MAIN_CONFIG = os.path.join(ASSETS_DIRECTORY, "game.ini")

IMAGE_FOLDER = os.path.join(ASSETS_DIRECTORY, "images")

BACKGROUND_SPACE_IMAGE_PATH = os.path.join(IMAGE_FOLDER, "BGSpace.jpg")
PLAYER_SHIP_IMAGE_PATH = os.path.join(IMAGE_FOLDER, "player_ship.gif")