  #Part A

import pygame  
import random 
import math

pygame.init()
screen = pygame.display.set_mode((500,500))
window = screen.get_rect()

while True:
    for event in pygame.event.get():
        pass
    screen.fill('blue')
    pygame.draw.circle(screen , 'white', (250,250) , 250)
    pygame.draw.line(screen , 'black', (250,0) ,(250,500) , 5 )
    pygame.draw.line(screen , 'black', (0,250) ,(500,250) , 5 )
  
    #Part B
    for x in range(10) :
      x = random.randrange(0,500)
      y = random.randrange(0,500)
      distance_from_center = math.hypot(250-x,250-y) 
      is_in_circle = distance_from_center <= 500/2 
      if is_in_circle  :
         pygame.draw.circle(screen , 'green' , (x ,y) , 10)
      else: pygame.draw.circle(screen , 'red',(x ,y) , 10)
     
      pygame.display.flip()
      pygame.time.wait(500)
    

