import settings

class Line:
    """
    The class contains lines, that the player leaves behind himself and
    makes when he changes direction.
    """
    
    def __init__(self, direction, beginning, num_of_points=settings.MAX_POINTS_BEFORE_LINE):
        """
        Initialize the line, with the number of points specified and the
        direction specified.
        """
        self.direction = direction
        self.num_of_points = num_of_points
        self.beginning = beginning
        self.fill_me = None
    
    def return_rect(self):
        """
        Return the rect corresponding to this line.
        """
        if direction == 2:
            self.fill_me = Rect([self.beginning.centerx - self.num_of_points , self.beginning.centery , self.num_of_points + 1 , 1])
        elif direction == 4:
            self.fill_me = Rect([self.beginning.centerx , self.beginning.centery , self.num_of_points , 1])
        elif direction == 3:
            self.fill_me = Rect([self.beginning.centerx , self.beginning.centery - self.num_of_points, 1 , self.num_of_points + 1])
        else:
            self.fill_me = Rect([self.beginning.centerx , self.beginning.centery , 1 , self.num_of_points])
            
        return self.fill_me
