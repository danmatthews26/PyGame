"""This file contains code for the player along with the perks and functions of the player"""
#!/usr/bin/python

import pygame




class Player:
    def __init__( self, display, width, height, x, y, color ):
        """TODO: add perks"""
        self.display = display
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
#         pygame.draw.rect(self.display, self.color, self.x, self.y, self.width, self.height)
    
    
    
    
    def Draw_Player(self):
        pygame.draw.rect(self.display, self.color, [self.x, self.y, self.width, self.height])
    
    
    
    
#     def Movement(self):
#         """TODO: add player movement only on x"""
        
     
     
     
    def Opening_Ball_Throw(self):
        """TODO: create function for starting off with the ball and hitting space to send it"""
        pass    
     
     
 
     
    def Hit_Ball(self):
        pass
 
 
     
     
    def Miss_Ball(self):
        pass