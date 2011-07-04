################################################################################
#                   Michael Sverdlin        4/2006                             #
#           A volified clone - working name "Volified new gen"                 #
#                                                                              #
# TODO : Version 0.1:                                                          #
#       Make the ship run when pressing a long key                           V #
#       Make the ship turn to whatever direction needed                      V #
#       Ship moves on the line                                               V #
#       Faster fill rects algorithm                                            #
#       Statistical choosing from a dictionary of background pictures          #
#       Make an enemy class                                                    #
#       Make the eating of hte surface work                                    #
#       Pretty evrything up and make it FASTER!                                #
#                                                                              #
################################################################################


#-------------------------------------------------------------------------------
#IMPORTS
#-------------------------------------------------------------------------------

import os
import sys
import logger
import traceback
import ConfigParser

import Image
import pygame
from pygame.locals import *
pygame.init()                               #Initialize all of the pygame parts

#-------------------------------------------------------------------------------
#GLOBALS
#-------------------------------------------------------------------------------

#Debug level:
DEBUG = True
MAIN_INI_FILE = "game.ini"

LOG_FILE = "LastRun.log"
BLUE = (30 , 0 , 0)
BLACK = (0 , 0 , 0)
MAX_POINTS_BEFORE_LINE = 75

#Image globals:
IMAGE_FOLDER = "Images"                     #Image folder name
BACKGROUND_SPACE_IMAGE = "BGSpace.jpg"      #The background photo
PLAYER_SHIP_IMAGE_NAME = "player_ship.gif"  #The image of the players ship

#Game globals
SCREEN_SIZE = (800 , 600)                   #The size of the game window
GAME_BOARD_SIZE = (760 , 530)               #The size of the game board
BG_RECT = [20 , 50 , 760 , 530]             #Size of the bg image - to allow full ship view
PLAYER_MOVE_SPEED = 5                       #Number of pixels the player moves
                                            #on a single key press
                                            
ANGLES_DICT = {"up" : 1 ,"down" : 3 , "right" : 2 , "left" : 4} #A dicrionary of angles to numbers


#-------------------------------------------------------------------------------
#CLASSES
#-------------------------------------------------------------------------------
#Classes of : boss (*X?) , littles , shooting bullets , score board/HUD

class Line:
    """
    The class contains lines, that the player makes when he changes direction.
    """
    
    def __init__(self, direction, beginning, num_of_points=MAX_POINTS_BEFORE_LINE):
        """
        Initialize the line, with the number of points specified and the
        direction specified.
        """
        try:
            self.direction = direction
            self.num_of_points = num_of_points
            self.beginning = beginning
            self.fill_me = None
        except Exception as error:
            Log("Initializing the line class failed: %s" % error, True)
    
    def return_rect(self):
        """
        Return the rect corresponding to this line.
        """
        try:
            
            if direction == 2:
                self.fill_me = Rect([self.beginning.centerx - self.num_of_points , self.beginning.centery , self.num_of_points + 1 , 1])
            elif direction == 4:
                self.fill_me = Rect([self.beginning.centerx , self.beginning.centery , self.num_of_points , 1])
            elif direction == 3:
                self.fill_me = Rect([self.beginning.centerx , self.beginning.centery - self.num_of_points, 1 , self.num_of_points + 1])
            else:
                self.fill_me = Rect([self.beginning.centerx , self.beginning.centery , 1 , self.num_of_points])
                
            return self.fill_me
                
        except Exception as error:
            Log("return_rect in class Line failed: %s" % error)
            

class GameBoard(pygame.sprite.Sprite):
    """
    This is the game board class, meaning the space where the space ship can
    move, or more specifically, move on it's edges. Will control the calculation
    of what places to blit XXXblackXXX (meaning conquered).
    """
    
    def __init__(self):
        """Initialize the background."""
        try:
            #Load the bg pic:
            self._get_background_path()
            
            #Save the ranges that the player can move in:
            self.y_ranges = xrange(self.bg_rect.top , self.bg_rect.bottom)
            self.x_ranges = xrange(self.bg_rect.left , self.bg_rect.right)
            
            #The eaten place on the game board:
            self.movable = [Line(1, self.bg_rect.)]
                        
        except Exception as error:
            Log("Initializing GameBoard class failed: %s" % error , True)

    def _get_background_path(self):
        """
        Returns a path to a background picture.
        
        TODO: Statistical choosing from a dictionary of background pictures availible
        """
    
        try:
            bg_path = os.path.join(IMAGE_FOLDER , BACKGROUND_SPACE_IMAGE)
            self.bg_surface = load_image(bg_path)[0]
            self.bg_rect = Rect(BG_RECT)
        
        except Exception as error:
            Log("Choosing a bg picture path failed: %s" % error)
            
    def can_move(self , (x , y)):
        """
        Checks if the point x , y (meaning the center of a rect - the player ship)
        can be a valid center point (meaning it's on the specified GameBoard
        edge).
        """
        
        try:
            
            if (x == self.x_ranges[0] or x == self.x_ranges[-1] or y == self.y_ranges[0] or y == self.y_ranges[-1]):
                if (x in self.x_ranges) and (y in self.y_ranges):
                    return True

            return False
        
        except Exception as error:
            Log("can_move failed: %s" % error)



class Player(pygame.sprite.Sprite):
    """
    The class of the player ship.
    """
    
    def __init__(self):
        """
        Initializes the player ship parameters.
        """
        
        try:
            #Load the player image ship:
            image_file_path = os.path.join(IMAGE_FOLDER , PLAYER_SHIP_IMAGE_NAME)
            self.image , image_rect = load_image(image_file_path)
            self.rect = image_rect
            self.rect.center = game_board.bg_rect.topleft
            
            #Declare some variables:
            self.movement_per_press = PLAYER_MOVE_SPEED
            self.current_direction = "up"
            self.is_attacking = False
            self.num_of_lines = 0
            self.num_of_points = 0
            
        except Exception as error:
            Log("Error initializing the player class: %s" % error , True)
            
    def FillPlace(self):
        """Fills the area the player 'ate' after he finished moving"""
        try:
            global fill_rects
            for i in fill_rects:
                print i.size
            fill_rects = []            
            
        except Exception as error:
            Log("Filling place failed: %s" % error , True)
        
    def move(self , direction , direction_in_words , is_attacking = False):
        "Moves the ship"
        
        try:
            #Adjust the direction of the image:
            if direction_in_words != self.current_direction:
                self.change_image_direction(direction_in_words)
                
            old_attacking = self.is_attacking
            
            #Add the current rect to the dirty rects list:
            global dirty_rects
            dirty_rects += [self.rect]
            
            #If the player started attacking:
            if (not is_attacking) and (not game_board.can_move(self.rect.center)):
                self.is_attacking = True
            else:
                self.is_attacking = is_attacking
            
            for i in xrange(self.movement_per_press):
                self._move_once(direction , direction_in_words)
                
            #Add the new rect to the dirty rects list:
            dirty_rects += [self.rect]
            
            #If finihed moving:
            if game_board.can_move(self.rect.center):
                self.FillPlace()
            return self.rect
                
        except Exception as error:
            Log("Moving ship failed: %s" % error)
            
    def _move_once(self , direction , direction_in_words):
        """
        Moves the space ship by the movement_per_press to the direction direction
        
        Direction is a tuple (x , y) where x and y are either 1 , -1 or 0, where
        x is for vertical movemente and y for horizontal. Thus moving left is:
        (0 , -1).
        """
        
        try:
            global fill_rects
            
            #Move the image rect:
            vert , hori = direction
            new_rect = self.rect.move(vert , hori)
            
            #Don't do anything if if the ship can't move to the specified place:
            #Check if in the map:
            if (not new_rect.centerx in game_board.x_ranges) or (not new_rect.centery in game_board.y_ranges):
                return
            #Check if moving out of boreder without attacking:
            if (not game_board.can_move(new_rect.center)) and (not self.is_attacking):
                return
            #Check if not going over an existing line:
            if (not game_board.can_move(new_rect.center) and len(fill_rects) > 0):
                for i in fill_rects:
                    if (Rect([new_rect.centerx , new_rect.centery , 0 , 0]).colliderect(i)):
                        return
            
            #Create a line if there are too much points (to prevent lag):
            self.num_of_points += 1
            if self.num_of_points > MAX_POINTS_BEFORE_LINE:
                self._create_line(ANGLES_DICT[self.current_direction])
            
            #Replace the rect with the new one and add the middle to  the filled line behind it:
            self.rect = new_rect
            if not game_board.can_move(new_rect.center):
                fill_rects += [Rect([self.rect.centerx , self.rect.centery , 1 , 1])]
        
        except Exception as error:
            Log("Error in _move_once the ship: %s" % error)
            

    def change_image_direction(self , direction_in_words):
        "Changes the image direction to the direction_in_words"

        try:
            global game_board
            if direction_in_words != self.current_direction:
                #Get the direction from the string values:
                old_direction = ANGLES_DICT[self.current_direction]
                new_direction = ANGLES_DICT[direction_in_words]
                
                #And rotate the image:
                self.image = pygame.transform.rotate(self.image , 90 * -(new_direction - old_direction))
                self.current_direction = direction_in_words
                
                self._create_line(old_direction)
                
        except Exception as error:
            Log("Error changing the image direction: %s" % error)

                
        
    def _create_line(self , old_direction):
        "Creates a line off the points previously in the list"
        
        try:
            if (not game_board.can_move(self.rect.center)):
                global fill_rects   
                if old_direction == 2:
                    fill_me = Rect([self.rect.centerx - self.num_of_points , self.rect.centery , self.num_of_points + 1 , 1])
                elif old_direction == 4:
                    fill_me = Rect([self.rect.centerx , self.rect.centery , self.num_of_points , 1])
                elif old_direction == 3:
                    fill_me = Rect([self.rect.centerx , self.rect.centery - self.num_of_points, 1 , self.num_of_points + 1])
                else:
                    fill_me = Rect([self.rect.centerx , self.rect.centery , 1 , self.num_of_points])
                    
                fill_rects[self.num_of_lines:] = [fill_me]
                self.num_of_lines += 1
            self.num_of_points = 0
                
        except Exception as error:
            Log("Creating line failed: %s")


#-------------------------------------------------------------------------------
#FUNCTIONS
#-------------------------------------------------------------------------------
        
def load_image(path):
        "Loads the image and returns it and it's rect."
        
        try:
            #Check if the file exists:
            assert os.path.isfile(path) , "A game file doesn't exist: %s" % path
            
            #Load the image and return the needed values:
            image = pygame.image.load(path)
            rect = image.get_rect()
            return image , rect
            
        except Exception as error:
            Log("Loading image (%s) failed: %s" % (path , error) , True)

def resize_image(path , x , y):
    "Resizes the image in the path path to the specified size"
    try:
        image_obj = Image.open(path)
        resized_image = image_obj.resize((x , y))
        resized_image.save(path)
        
    except Exception as error:
        raise Exception , "Resizing the image failed: %s" % error


def Log(message , isCritical = False):
    """
    Log the message in the selected method.
    If he isCritical flag is on, the error is critical and caused the program termination.
    """
    
    try:
        if is_critical:
            message = "\r\nThe following error has caused the program to terminate:\r\n%s"  % message
        
        print message
        if DEBUG:
            logFile = open(LOG_FILE , "w")
            logFile.write(message)
            logFile.close()
            
        if is_critical:
            os._exit(1)
            
    except SystemExit:
        pass
    except Exception as error:
        print "Error in logging: %s" % error

        
#-------------------------------------------------------------------------------
#MAIN
#-------------------------------------------------------------------------------

def main():
    "The main game function"
    try:
        global game_board
        Log("Player started game!")
        
        #Initialize the gameboard class and screen:
        flag = FULLSCREEN
        if FS:
            flag |= FULLSCREEN
        screen = pygame.display.set_mode(SCREEN_SIZE , flag)
        screen.fill(BLUE)
        
        game_board = GameBoard()
        screen.blit(game_board.bg_surface , game_board.bg_rect)
       
        #Initialize the player ship:
        player_ship = Player()
        screen.blit(player_ship.image , player_ship.rect)
        
        #Show evrything:
        pygame.display.flip()
        
        #A list of rects that changed since last update:
        global dirty_rects
        dirty_rects = []
        global fill_rects
        fill_rects = []
        
        
        #A boolean specifying wheteher the space was pressed:
        is_attacking = False
        
        #Main event loop:
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT: #Quit...
                    Log("Player exited!")
                    os._exit(0)
                    
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        Log("Player exited!")
                        os._exit(0)

            #Player moving:
            keystate = pygame.key.get_pressed()
            
            if keystate[K_SPACE]:
                is_attacking = True
                
            if keystate[K_LEFT]:
                player_ship.move((-1 , 0) , "left" , is_attacking)
                
            elif keystate[K_RIGHT]:
                player_ship.move((1 , 0) , "right" , is_attacking)
                
            elif keystate[K_UP]:
                player_ship.move((0 , -1) , "up" , is_attacking)

            elif keystate[K_DOWN]:
                player_ship.move((0 , 1) , "down" , is_attacking)
                
            #Blit evrything in place...
            screen.fill(BLUE)
            screen.blit(game_board.bg_surface , game_board.bg_rect)
            for i in fill_rects:
                screen.fill((255 , 255 , 255) , i)
            screen.blit(player_ship.image , player_ship.rect)
            pygame.display.update(dirty_rects)
            if len(fill_rects):
                pygame.display.update(fill_rects[-1])
            dirty_rects = []        #Clean the list for the next run
            is_attacking = False
                
    except Exception as error:
        Log("Main failed WOOT: %s" % error , True)

if __name__ == "__main__":
    main()