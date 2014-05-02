import pygame

import settings
import utilities

class GameBoard(pygame.sprite.Sprite):
    """
    This is the game board class, meaning the space where the space ship can
    move, or more specifically, move on it's edges. Will control the calculation
    of what places to blit conquered.
    """
    
    def __init__(self):
        """
        Load the background image.
        """
        pygame.sprite.Sprite.__init__(self)
        
        #Load the bg pic:
        self._choose_background()
        self.bg_rect = pygame.Rect(settings.BG_RECT)
        
        #Save the ranges that the player can move in:
        self.y_ranges = xrange(self.bg_rect.top , self.bg_rect.bottom)
        self.x_ranges = xrange(self.bg_rect.left , self.bg_rect.right)
        
                       
    def _choose_background(self):
        """
        Load the background picture.
        """
        self.bg_surface, _ = utilities.load_image(settings.BACKGROUND_SPACE_IMAGE_PATH)
        
        
    def can_move(self , (x , y)):
        """
        Checks if the point x , y (meaning the center of a rect - the player ship)
        can be a valid center point (meaning it's on the specified GameBoard
        edge).
        """
        if (x == self.x_ranges[0] or x == self.x_ranges[-1] or
            y == self.y_ranges[0] or y == self.y_ranges[-1]):
            if (x in self.x_ranges) and (y in self.y_ranges):
                return True

        return False
    
    
    def get_player_start_position(self):
        """
        Return the start position of the player on this particular board.
        """
        return self.bg_rect.topleft
    
    
    def get_enemy_spawn(self):
        return self.bg_rect.center
    