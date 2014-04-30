def load_image(path):
        """
        Loads the image and returns it and it's rect.
        """
        #Check if the file exists:
        assert os.path.isfile(path) , "A game file doesn't exist: %s" % path
        
        #Load the image and return the needed values:
        image = pygame.image.load(path)
        rect = image.get_rect()
        return image , rect

def resize_image(path , x , y):
    """
    Resizes the image in the path path to the specified size
    """
    image_obj = Image.open(path)
    resized_image = image_obj.resize((x , y))
    resized_image.save(path)


def Log(message , is_critical = False):
    """
    Log the message in the selected method.
    If he isCritical flag is on, the error is critical and caused the program termination.
    """
    if is_critical:
        message = "\r\nThe following error has caused the program to terminate:\r\n%s"  % message
    
    print message
    if DEBUG:
        logFile = open(LOG_FILE , "w")
        logFile.write(message)
        logFile.close()
            
