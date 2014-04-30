import time

import pygame
pygame.init()
from pygame.colordict import THECOLORS

import settings
import GameBoard
from utilities import log


def main():
    """
    The main game function
    """
    log("Game started.")
    
    #Initialize the gameboard class and screen:
    screen = pygame.display.set_mode(settings.SCREEN_SIZE, 0)
    screen.fill(settings.BACKGROUND_FILL_COLOR)
    
    game_board = GameBoard.GameBoard()
    screen.blit(game_board.bg_surface, game_board.bg_rect)

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


if __name__ == "__main__":
    main()