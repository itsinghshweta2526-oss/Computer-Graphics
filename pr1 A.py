#Circle
import pygame 
from pygame.locals import * 
pygame.init() 
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Shweta S056")
window.fill((255, 255, 255)) 
pygame.draw.circle(window, (0, 255, 0), [300, 300], 170, 0)
pygame.display.update()
