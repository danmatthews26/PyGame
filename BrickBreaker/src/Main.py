#!/usr/bin/python

import pygame
import random
from colorFile import colors
from Player_Class import Player




screen_width = 800
screen_height = 800
FPS = 60
running = True

"""Player_Class variables"""
player_width = 100
player_height = 20
player_start_x = screen_width / 2 - player_width / 2
player_start_y = (screen_height - player_height) - player_height


pygame_init = pygame.init()
game_display = pygame.display.set_mode(( screen_width, screen_height ))
pygame.display.set_caption( "Brick Breaker" )
clock = pygame.time.Clock()


player = Player(game_display ,player_width,player_height,player_start_x,player_start_y,colors['red'])




while( running == True ):
    """TODO: setup movement"""
    clock.tick( FPS )
    
    
    game_display.fill( colors['white'] )
    player.Draw_Player()
    
    
    
    for event in pygame.event.get():
        if( event.type == pygame.QUIT ):
            running = False
                
    pygame.display.update()  



pygame.quit()
quit()


