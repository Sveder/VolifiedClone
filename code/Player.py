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
        self.current_direction = settings.D_UP
        self.is_attacking = False
        self.num_of_lines = 0
        self.num_of_points = 0
        
        self.line_segments = []
            

    def fill_place(self):
        """
        Fills the area the player 'ate' after he finished moving.
        """
        ###WRITE THE CODE

           
    def move(self, direction, is_attacking=False):
        """
        Moves the ship if possible.
        """
        #Adjust the direction of the image:
        if direction != self.current_direction:
            self.change_image_direction(direction)
            
        old_attacking = self.is_attacking
        old_rect = self.rect
        dirty_rects = [old_rect]
        
        #If the player started attacking:
        if (not is_attacking) and (not self.game_board.can_move(self.rect.center)):
            self.is_attacking = True
        else:
            self.is_attacking = is_attacking
        
        for i in xrange(self.movement_per_press):
            self._move_once(direction)
            
        #Add the new rect to the dirty rects list:
        dirty_rects.append(self.rect)
        
        #If finihed moving:
        if self.game_board.can_move(self.rect.center):
            self.fill_place()
        
        return dirty_rects
            

    def _move_once(self, direction):
        """
        Moves the space ship by the one pixel to the direction given.
        
        Direction is a tuple (x , y) where x and y are either 1 , -1 or 0, where
        x is for vertical movemente and y for horizontal. Thus moving left is:
        (0 , -1).
        """
        #Move the image rect:
        vert , hori = direction.move_modifier
        new_rect = self.rect.move(vert , hori)
        
        #Don't do anything if if the ship can't move to the specified place:
        #Check if in the map:
        if (not new_rect.centerx in self.game_board.x_ranges) or (not new_rect.centery in self.game_board.y_ranges):
            return
        
        #Check if moving out of border without attacking:
        if (not self.game_board.can_move(new_rect.center)) and (not self.is_attacking):
            return
        
        #Check if not going over an existing line:
        if (not self.game_board.can_move(new_rect.center) and len(self.line_segments) > 0):
            for i in self.line_segments:
                if (pygame.Rect([new_rect.centerx, new_rect.centery, 0, 0]).colliderect(i)):
                    return
        
        #Create a line if there are too much points (to prevent lag):
        self.num_of_points += 1
        if self.num_of_points > settings.MAX_POINTS_BEFORE_LINE:
            self._create_line(self.current_direction.angle_modifier)
        
        #Replace the rect with the new one and add the middle to the filled line behind it:
        self.rect = new_rect
        if not self.game_board.can_move(new_rect.center):
            self.line_segments += [pygame.Rect([self.rect.centerx , self.rect.centery , 1 , 1])]
           

    def change_image_direction(self, direction):
        """
        Changes the image direction to the given direction.
        """
        if direction != self.current_direction:
            old_direction = self.current_direction.angle_modifier
            new_direction = direction.angle_modifier
            
            #And rotate the image:
            self.image = pygame.transform.rotate(self.image , 90 * -(new_direction - old_direction))
            self.current_direction = direction
            
            self._create_line(old_direction)
        

    def _create_line(self, direction):
        """
        Creates a line of the points previously in the list.
        """
        #TODO: Why do we need this conditional?
        if (not self.game_board.can_move(self.rect.center)):
            if direction == 2:
                fill_me = pygame.Rect([self.rect.centerx - self.num_of_points , self.rect.centery , self.num_of_points + 1 , 1])
            elif direction == 4:
                fill_me = pygame.Rect([self.rect.centerx , self.rect.centery , self.num_of_points , 1])
            elif direction == 3:
                fill_me = pygame.Rect([self.rect.centerx , self.rect.centery - self.num_of_points, 1 , self.num_of_points + 1])
            elif direction == 1:
                fill_me = pygame.Rect([self.rect.centerx , self.rect.centery , 1 , self.num_of_points])
            else:
                raise ValueError("Direction given is not valid: %s." % direction)
                
            self.line_segments[self.num_of_lines:] = [fill_me]
            self.num_of_lines += 1
            
        self.num_of_points = 0

