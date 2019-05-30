import pygame, sys
from pygame.locals import *
import random

pygame.mixer.pre_init(48000, 16, 1, 4096)
pygame.init()

screenx = 640
screeny = 480
screen = pygame.display.set_mode((screenx, screeny))
clock = pygame.time.Clock()

"""colors"""
black = (0,0,0)
light_gray = (75,75,75)

blue = (50,50,200)
dark_blue = (25,25,100)

white = (255,255,255)
green = (50,150,50)
red = (150,25,25)
orange = (150,70,70)
yellow = (150,150,25)

colors_change = [blue,light_gray]

font = pygame.font.Font(None, 30)
class Shape:
    def __init__(self,typee,x,y,width,height,direction,speed,color,move):
        self.typee = typee
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.speed = speed
        self.color = color
        self.move = move
        
    def move_function(self):
        if self.move != False:
            if self.direction[0] == 'left':
                self.x -= self.speed
            if self.direction[0] == 'right':
                self.x += self.speed

    def collision(self):
        if self.move != False:
            if (self.x + self.width + 5) > screenx:
                self.direction.reverse()
            if (self.x - 5) < 0:
                self.direction.reverse()
    
    def click(self):
        if self.typee == 'button':
            colors_change.reverse()
        else:
            pass
        
class Circle:
    def __init__(self,typee,x,y,diameter,direction_x,direction_y,speed,color,collide):
        self.typee = typee
        self.x = x
        self.y = y
        self.diameter = diameter
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.speed = speed
        self.color = color
        self.collide = collide
        
    def move_function(self):
        global modify_x, modify_y
        modify_x = 0
        modify_y = 0
        
        self.collide = False

        if self.direction_x[0] == 'left':
            self.x -= self.speed
        if self.direction_x[0] == 'right':
            self.x += self.speed

        if self.direction_y[0] == 'up':
            self.y -= self.speed
        if self.direction_y[0] == 'down':
            self.y += self.speed

        self.x -= modify_x
        self.y -= modify_y
        
    def collision(self):
        global modify_x, modify_y
        #(self.x,self.y,self.width,self.height)
        random_color = random.randrange(1,6)
        if random_color == 1:
            random_color = red
        if random_color == 2:
            random_color = orange
        if random_color == 3:
            random_color = yellow
        if random_color == 4:
            random_color = green
        if random_color == 5:
            random_color = dark_blue

        random_speed = random.randrange(5,7)
            

        modify_x = 0
        modify_y = 0
        
        if self.collide != True:
            if pygame.Rect(circle.x - (circle.diameter/2) - self.speed,circle.y - (circle.diameter/2),circle.diameter,circle.diameter).colliderect(value.x,value.y,value.width,value.height):
                modify_x = (value.x - (circle.x + (circle.diameter/2)))
                
            if pygame.Rect(circle.x - (circle.diameter/2) + self.speed,circle.y - (circle.diameter/2),circle.diameter,circle.diameter).colliderect(value.x,value.y,value.width,value.height):
                modify_x = (circle.x - (value.x + value.width))

            if pygame.Rect(circle.x - (circle.diameter/2),circle.y - (circle.diameter/2) - self.speed,circle.diameter,circle.diameter).colliderect(value.x,value.y,value.width,value.height):
                modify_y = (value.y - (circle.y + (circle.diameter/2)))
                
            if pygame.Rect(circle.x - (circle.diameter/2) + self.speed,circle.y - (circle.diameter/2) + self.speed,circle.diameter,circle.diameter).colliderect(value.x,value.y,value.width,value.height):
                modify_y = (circle.y - (value.y + value.height))
                
            if pygame.Rect(circle.x - (circle.diameter/2) ,circle.y - (circle.diameter/2),circle.diameter,circle.diameter).colliderect(value.x,value.y,value.width,2):
                self.direction_y.reverse()
                self.collide = True
                self.color = random_color
                self.speed = random_speed
                
            if pygame.Rect(circle.x - (circle.diameter/2) ,circle.y - (circle.diameter/2),circle.diameter,circle.diameter).colliderect(value.x,value.y,2,value.height):
                self.direction_x.reverse()
                self.collide = True
                self.color = random_color
                self.speed = random_speed
                
            if (self.x + (self.diameter/2) + self.speed) > screenx:
                self.direction_x.reverse()
                self.collide = True
                self.color = random_color
                self.speed = random_speed
                
            if (self.x - (self.diameter/2) - self.speed) < 0:
                self.direction_x.reverse()
                self.collide = True
                self.color = random_color
                self.speed = random_speed
                
            
            if (self.y + (self.diameter/2) + self.speed) > screeny:
                self.direction_y.reverse()
                self.collide = True
                self.color = random_color
                self.speed = random_speed

                
            if (self.y - (self.diameter/2) - self.speed) < 0:
                self.collide = True
                self.color = random_color
                self.speed = random_speed
                self.direction_y.reverse()
     
line = Shape('rectangle',220,50,200,4,['right','left'],5,white,True)
rectangle = Shape('rectangle',540,380,100,100,None,5,red,False)
button = Shape('button',540,0,100,25,None,5,white,False)
button_text = font.render('CHANGE', True, black)

circle = Circle('circle',240,320,50,['left','right'],['up','down'],5,green,False)

shapes = [line,rectangle,button]

def start_screen():
    start = Shape('button',0,0,100,25,None,5,white,False)
    start_text = font.render('START', True, black)
    shapes = [start]
    while True:
        click_var = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_ = event.pos
                click_var = True
                
        if click_var == True:
            if pygame.Rect(pos_[0],pos_[1],1,1).colliderect(start.x,start.y,start.width,start.height):
                break
                
        screen.fill(light_gray)

        pygame.draw.rect(screen, start.color, (start.x,start.y,start.width,start.height))
        screen.blit(start_text, (start.x+18,start.y+3))
        clock.tick_busy_loop(60)
        pygame.display.update()
        
start_screen()
    
while True:
    click_var = False
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_ = event.pos
            click_var = True

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(colors_change[0])
    
    pygame.draw.circle(screen, circle.color, (circle.x,circle.y), (int(circle.diameter / 2)))
                
    for value in shapes:
        circle.collision()
        pygame.draw.rect(screen, value.color, (value.x,value.y,value.width,value.height))
        value.collision()
        value.move_function()
    
        if click_var == True:
            if pygame.Rect(pos_[0],pos_[1],1,1).colliderect(value.x,value.y,value.width,value.height):
                value.click()
        screen.blit(button_text, (button.x+5,button.y+3))
    
    circle.move_function()
    clock.tick_busy_loop(60)
    pygame.display.update()
    
