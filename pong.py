import pygame
import numpy as np
import cv2


 
class Player():
        def __init__(self):
                self.x, self.y = 0, SCR_WID-2
                self.speed = 3
                self.padWid, self.padHei = 64, 8
                self.score = 0
                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
       
      
       
        def movement(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                        self.y -= self.speed
                elif keys[pygame.K_s]:
                        self.y += self.speed
       
                if self.y <= 0:
                        self.y = 0
                elif self.y >= SCR_HEI-64:
                        self.y = SCR_HEI-64
       
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))
 
class Obstacle():
        def __init__(self):
                self.x, self.y = 0, SCR_WID-2
                self.speed = 3
                self.padWid, self.padHei = 64, 8
                self.score = 0
                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
       
      
       
        def movement(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                        self.y -= self.speed
                elif keys[pygame.K_s]:
                        self.y += self.speed
       
                if self.y <= 0:
                        self.y = 0
                elif self.y >= SCR_HEI-64:
                        self.y = SCR_HEI-64
       
        def draw(x,y,w):
                pygame.draw.rect(screen, (255, 255, 255), (x, y, w, 2))


                
class Ball():
        def __init__(self):
                self.x, self.y = SCR_WID/2, SCR_HEI/2
                self.speed_x = -3
                self.speed_y = 3
                self.size = 8
       
        def movement(self):
                self.x += self.speed_x
                self.y += self.speed_y
 
                #wall col
                if self.y <= 0:
                        self.speed_y *= -1
                elif self.y >= SCR_HEI-self.size:
                        self.speed_y *= -1
 
                if self.x <= 0:
                        
                        self.speed_x *= -1
                       
                elif self.x >= SCR_WID-self.size:
                        
                        self.speed_x *= -1
                        
                      
                ##wall col
                #paddle col
                #player
                for n in range(-self.size, player.padHei):
                        if self.y == player.y + n:
                                if self.x <= player.x + player.padWid:
                                        self.speed_x *= -1
                                        self.speed_y *= -1
                                        break
                        n += 1
             
                ##paddle col
 
        def draw(self):
                pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 10, 10)


def findObstacle():
    im = cv2.imread('teste.jpg')
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if (len(contours) > 0):
        for cont in contours:
            x,y,w,h = cv2.boundingRect(cont)
            Obstacle.draw(x,y,w)
            
        
        
    
    



 
SCR_WID, SCR_HEI = 640, 480
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
pygame.display.set_caption("Pong")
pygame.font.init()
clock = pygame.time.Clock()
FPS = 60
 
ball = Ball()
player = Player()

 
while True:
        #process
        for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                              
                                exit()
        ##process
        #logic
        ball.movement()
        player.movement()
        
        ##logic
        #draw
        screen.fill((0, 0, 0))
        ball.draw()
        player.draw()
        findObstacle()
        ##draw
        #_______
        pygame.display.flip()
        clock.tick(FPS)
