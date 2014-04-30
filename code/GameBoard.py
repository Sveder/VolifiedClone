import settings

class GameBoard(pygame.sprite.Sprite):
    """
    This is the game board class, meaning the space where the space ship can
    move, or more specifically, move on it's edges. Will control the calculation
    of what places to blit XXXblackXXX (meaning conquered).
    """
    
    def __init__(self):
        """Initialize the background."""
        #Load the bg pic:
        self._get_background_path()
        
        #Save the ranges that the player can move in:
        self.y_ranges = xrange(self.bg_rect.top , self.bg_rect.bottom)
        self.x_ranges = xrange(self.bg_rect.left , self.bg_rect.right)
        
        #The eaten place on the game board:
        ###self.movable = [Line(1, self.bg_rect.)]
                        
    def _get_background_path(self):
        """
        Returns a path to a background picture.
        
        TODO: Statistical choosing from a dictionary of background pictures availible
        """
        bg_path = settings.BACKGROUND_SPACE_IMAGE
        self.bg_surface = load_image(bg_path)[0]
        self.bg_rect = Rect(BG_RECT)
        
        
    def can_move(self , (x , y)):
        """
        Checks if the point x , y (meaning the center of a rect - the player ship)
        can be a valid center point (meaning it's on the specified GameBoard
        edge).
        """
        if (x == self.x_ranges[0] or x == self.x_ranges[-1] or y == self.y_ranges[0] or y == self.y_ranges[-1]):
            if (x in self.x_ranges) and (y in self.y_ranges):
                return True

        return False