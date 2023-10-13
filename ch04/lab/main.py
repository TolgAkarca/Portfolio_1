import random
import pygame
import math 


pygame.init()


screen = pygame.display.set_mode((800, 600))


red = (255, 0, 0)
blue = (0, 0, 255)


player_selection = None

screencreen = pygame.display.set_mode((800, 600))
red = (255, 0, 0)
blue = (0, 0, 255)
running = True

iteration1 = 0
iteration2 = 0


while True:
    while running:
        pygame.draw.rect(screen, red, (200, 200, 200, 200))
        pygame.draw.rect(screen, blue, (400, 200, 200, 200))
        pygame.display.flip()
        while player_selection == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                
                if event.type == pygame.MOUSEBUTTONDOWN:
                
                    x, y = pygame.mouse.get_pos()

                    
                    if 200 <= x <= 400 and 200 <= y <= 400:
                        player_selection = red
                    elif 400 <= x <= 600 and 200 <= y <= 400:
                        player_selection = blue

        
        pygame.display.flip()
        break





    pygame.init()
    screen = pygame.display.set_mode((500,500))
    window = screen.get_rect()

    player1points = []
    player2points = []

    while True:
        for event in pygame.event.get():
            pass
        
        
        while True:
            screen.fill('lightblue')
            pygame.draw.circle(screen , 'white', (250,250) , 250)
            pygame.draw.line(screen , 'black', (250,0) ,(250,500) , 5 )
            pygame.draw.line(screen , 'black', (0,250) ,(500,250) , 5 )
            font = pygame.font.Font(None, 48)
            player1hit = font.render("Player red hits", True, "black")
            player1miss = font.render("Player red miss", True, "black")

            player2hit = font.render("Player blue hits", True, "black")
            player2miss = font.render("Player blue miss", True, "black")
            player1win = font.render("Player red win the game", True, "black")
            player2win = font.render("Player blue win the game", True, "black")


            if iteration1 < 10 :

                message1 = None
                
                x1 = random.randrange(0,500)
                y1 = random.randrange(0,500)
                
                distance_from_center1 = math.hypot(250-x1,250-y1) 
                is_in_circle1 = distance_from_center1 <= 500/2 
                

                pygame.draw.circle(screen , 'red' , (x1 ,y1) , 10)

                if is_in_circle1  :
                    color = 'red'
                    message1 = player1hit
    
                    player1points.append((x1,y1,color))

                else: 
                    color = 'red'
                    message1 = player1miss
                    #screen.blit(player1miss, (0,300)) 

                

                
                screen.blit(message1 ,(0,300)) 

                iteration1+=1


            if iteration2 < 10 :
                message2 = None 

                x2 = random.randrange(0,500)
                y2 = random.randrange(0,500)

                distance_from_center2 = math.hypot(250-x2,250-y2) 
                is_in_circle2 = distance_from_center2 <= 500/2 

                pygame.draw.circle(screen , 'blue', (x2,y2) , 10)

                if is_in_circle2 : 
                    color = 'blue'
                    message2 = player2hit
                    player2points.append((x2,y2,color))

            
                    

                else :
                    color = 'blue' 
                    message2 = player2miss
                    
                

                
                screen.blit(message2 , (270,300))
                iteration2+=1

            pygame.display.flip()
            pygame.time.wait(500)
            break

    
        
        while True:
         pygame.init()
         screen = pygame.display.set_mode((500,500))
         window = screen.get_rect()
        
         pygame.draw.rect(screen, 'white ', (200, 200, 200, 200))
         pygame.display.flip()
         if len(player1points) > len(player2points) :
            message3 = player1win
            color = 'black'

         elif len(player2points) > len(player1points) :
            message4 = player2win
            color = 'black'

         pygame.display.flip()
         pygame.time.wait(500)

         


   


