import time

import pygame
pygame.init()
from pygame.colordict import THECOLORS

import Player
import settings
import BaseEnemy
import GameBoard
from utilities import log

g_dirty_rects = []

def main():
    """
    The main game function
    """
    clock = pygame.time.Clock()
    
    log("Game started.")
    
    #Initialize the gameboard class and screen:
    screen = pygame.display.set_mode(settings.SCREEN_SIZE, 0)
    screen.fill(settings.BACKGROUND_FILL_COLOR)
    
    game_board = GameBoard.GameBoard()
    screen.fill(THECOLORS["blue"], game_board.bg_rect)

    #Initialize the player ship:
    player_ship = Player.Player(game_board)
    screen.blit(player_ship.image , player_ship.rect)
    
    #Initialize enemies:
    enemies = [BaseEnemy.BaseEnemy(game_board)]
    for e in enemies:
        screen.blit(e.image, e.rect)
    
    #Show evrything:
    pygame.display.flip()
    
    #A list of rects that changed since last update:
    global dirty_rects
    g_dirty_rects = []
    
    #A boolean specifying wheteher the space was pressed:
    is_attacking = False
    
    #Main event loop:
    while 1:
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                log("Player exited!")
                return
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    log("Player exited!")
                    return
                

        #Player moving:
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_SPACE]:
            is_attacking = True
            
        dirty_player_locations = []
        if keystate[pygame.K_LEFT]:
            dirty_player_locations = player_ship.move(settings.D_LEFT , is_attacking)
            
        elif keystate[pygame.K_RIGHT]:
            dirty_player_locations = player_ship.move(settings.D_RIGHT , is_attacking)
            
        elif keystate[pygame.K_UP]:
            dirty_player_locations = player_ship.move(settings.D_UP , is_attacking)

        elif keystate[pygame.K_DOWN]:
            dirty_player_locations = player_ship.move(settings.D_DOWN, is_attacking)
        
        g_dirty_rects += dirty_player_locations
        
        #Blit evrything in place...
        screen.fill(settings.BACKGROUND_FILL_COLOR)
        screen.fill(THECOLORS["blue"], game_board.bg_rect)
        
        #screen.blit(game_board.bg_surface, game_board.bg_rect)
        for e in enemies:
            screen.blit(e.image, e.rect)
            if pygame.sprite.collide_rect(e, player_ship):
                #Death by touching enemy
                pass
        
        for i in player_ship.line_segments:
            screen.fill((255 , 255 , 255) , i)
            
        screen.blit(player_ship.image , player_ship.rect)
        
        
        pygame.display.update(g_dirty_rects)
        if len(player_ship.line_segments):
            pygame.display.update(player_ship.line_segments)
            
        g_dirty_rects = []        #Clean the list for the next run
        is_attacking = False
        
        print clock.get_fps()


if __name__ == "__main__":
    main()