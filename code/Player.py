import pygame

import settings
import utilities

class Player(pygame.sprite.Sprite):
    """
    The class of the player ship.
    """
    def __init__(self, game_board):
        """
        Initializes the player ship parameters.
        """
        pygame.sprite.Sprite.__init__(self)
        
        self.game_board = game_board
        
        #Load the player image ship:
        image_file_path = settings.PLAYER_SHIP_IMAGE_PATH
        self.image , self.rect = utilities.load_image(image_file_path)
        
        self.rect.center = self.game_board.get_player_start_position()
        
        #Declare some variables:
        self.movement_per_press = settings.PLAYER_MOVE_SPEED
        self.current_direction = settings.D_DOWN
        self.is_attacking = False
        self.num_of_lines = 0
        self.num_of_points = 0
            

    def fill_place(self):
        """
        Fills the area the player 'ate' after he finished moving.
        """
        ###WRITE THE CODE

           
    def move(self, direction, is_attacking = False):
        """
        Moves the ship if possible.
        """
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
            

    def _move_once(self , direction , direction_in_words):
        """
        Moves the space ship by the movement_per_press to the direction direction
        
        Direction is a tuple (x , y) where x and y are either 1 , -1 or 0, where
        x is for vertical movemente and y for horizontal. Thus moving left is:
        (0 , -1).
        """
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
           

    def change_image_direction(self , direction_in_words):
        """
        Changes the image direction to the direction_in_words
        """
        global game_board
        if direction_in_words != self.current_direction:
            #Get the direction from the string values:
            old_direction = ANGLES_DICT[self.current_direction]
            new_direction = ANGLES_DICT[direction_in_words]
            
            #And rotate the image:
            self.image = pygame.transform.rotate(self.image , 90 * -(new_direction - old_direction))
            self.current_direction = direction_in_words
            
            self._create_line(old_direction)
        

    def _create_line(self , old_direction):
        """
        Creates a line off the points previously in the list
        """
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

