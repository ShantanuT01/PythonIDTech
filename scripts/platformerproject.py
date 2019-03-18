import pygame
import sys
import time
from pygame.locals import *
import random
pygame.init()
screen = pygame.display.set_mode((1000,1000))
import random
import threading
from threading import Thread
pygame.display.set_caption("Platformer! by Shantanu T.")
main_clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)





#Variables
gravity = [False, 5]
lmove = False   
rmove = False
dmove = False
umove = False


player_speed = 10
player = pygame.Rect(700,800,50,50)
enemy1 = pygame.Rect(00,610,30,30)
enemy2 = pygame.Rect(00,510,30,30)
enemy3 = pygame.Rect(00,410,30,30)
enemy4 = pygame.Rect(00,310,30,30)
enemy5 = pygame.Rect(00,210,30,30)
enemy6 = pygame.Rect(00,10,40,40)
enemy7 = pygame.Rect(00,710,30,30)
enemies = [enemy1,enemy2,enemy3,enemy4,enemy5,enemy6,enemy7]


platform = pygame.Rect(200,100,100,10)
platform2 = pygame.Rect(100,200,100,10)
platform3 = pygame.Rect(200,300,100,10)
platform4 = pygame.Rect(300,400,100,10)
platform5 = pygame.Rect(400,500,100,10)
platform6 = pygame.Rect(500,600,100,10)
platform7 = pygame.Rect(600,700,100,10)
platform8 = pygame.Rect(700,800,100,10)

pl = [platform,platform2,platform3,platform4,platform5,platform6,platform7,platform8]
jump_counter= 0
jumpTimer = False
grounded = False
platLeft = True
platRight = False
g = None
rightLeft = [True,False]
rightLeft2 = [True,False]
rightLeft3 = [True,False]
rightLeft4 = [True,False]
rightLeft5 = [True,False]
rightLeft6= [True,False]
rightLeft7 = [True,False]
rightLeft8= [True,False]
victory = False
lose = False
e1 = [True,False]
e2 =[True,False]
e3 =[True,False]
e4 = [True,False]
e5 =[True,False]
e6 =[True,False]
e7 = [True,False]
enemyKeys = [e1,e3,e6]
b = False
platKeys =[rightLeft,rightLeft2,rightLeft3,rightLeft4,rightLeft5,rightLeft6,rightLeft7,rightLeft8]
def draw_text(display_string, font, surf, x,y):
    textd = font.render(display_string,1,(255,255,255))
    textrect = textd.get_rect()
    textrect.topleft = (x,y)
    surf.blit(textd,textrect)


def sideToSide(plat,speed,rightLeft):
    
        

    if rightLeft[0]:
        plat.x += speed
        if plat.x >=900:
            
            return [False, True]
            plat.x-= speed
        else:
            return [True , False]
    else:
       plat.x -= speed
       if plat.x <=0:
            return [True , False]
       else:
           return [False, True]
        
def emove(e,speed,this):
    
        

    if this[0]:
        e.x += random.randint(1,50)
        if e.x >=1000:
            
            return [False, True]
            e.x-= speed
        else:
            return [True , False]
    else:
       e.x -= random.randint(1,50)
       if e.x <=0:
            return [True , False]
       else:
           return [False, True]
        

#Variables

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                lmove = True
                dmove = False
                rmove = False
                umove = False
            if event.key == K_d:
                lmove = False
                dmove = False
                rmove = True
                umove = False
            if event.key == K_w:
                lmove = False
                dmove = False
                rmove = False
                umove = True
                
            
        if event.type == KEYUP:
            if event.key == K_a:
                lmove = False
            if event.key == K_d:
                rmove = False
            #if event.key == K_w:
                #umove = False
    main_clock.tick(50)

    helper = 0
    for plat in pl:
        
        #if lmove:
            #
            

        #elif rmove:

        #elif umove:
        
        if player.colliderect(plat):
           #player.y -= 0
            player.y = plat.y-48

            
            if platKeys[helper][0]:
                player.x +=5
            else:
                player.x -= 5
            
            grounded = True
            break
        else:
            grounded = False
        helper += 1
    if player.colliderect(platform):
        victory = True
        b = True
        break
    if player.y >= 1000:
        lose = True
        
    for enemy in enemies:
        if player.colliderect(enemy):
            lose = True
    if lose:
        b = True
        break
        
    if victory:
        b = True
        break
        
    def jump(s):
        player.x-=s
    def fall(s):
        player.y+=s
    if lmove and player.left > 0:
        player.x -= player_speed
    if rmove and player.right < 1000:
        player.x += player_speed
    if umove and player.y > 0 and not jump_counter >= 10:
        player.y-=10
        jump_counter+=1
        grounded = False
    elif not grounded :
        player.y += 6
    elif grounded and jump_counter >= 10 :
        jump_counter = 0
    if jump_counter >= 10 and not grounded:
        umove = False
    if umove and lmove:
        Thread(target = fall(9)).start()
        Thread(target = jump(15)).start()
    rand = None
    count = 0

        
    #for platforms in pl:
        
        #if platLeft:
            #pspeed = random.randint(1,100)
            #platforms.x += pspeed
            #if platforms.x >=1000:
                #platLeft = False
                #platRight = True
        #elif platRight:
            #pspeed = random.randint(1,5)
            #platforms.x -= pspeed
            #if platforms.x <= 0:
                #platLeft = True
                #platRight = False
    platKeys[0] = sideToSide(platform,5,platKeys[0])
    platKeys[1] = sideToSide(platform2,5,platKeys[1])
    platKeys[2] = sideToSide(platform3,5,platKeys[2])
    platKeys[3] = sideToSide(platform4,5,platKeys[3])
    platKeys[4] = sideToSide(platform5,5,platKeys[4])
    platKeys[5] = sideToSide(platform6,5,platKeys[5])
    platKeys[6] = sideToSide(platform7,5,platKeys[6])
    platKeys[7] = sideToSide(platform8,5,platKeys[7])
    e1 = emove(enemy1, .01,e1)
    e2 = emove(enemy2, 5,e2)
    e3 = emove(enemy3, 5,e3)
    e4 = emove(enemy4, .01,e4)
    e5 = emove(enemy5, 5,e5)
    e6 = emove(enemy6, .01,e6)
    e7 = emove(enemy7,5,e7)
    
    
    
        
        
        
    
        
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), player)
    for x in pl:
        pygame.draw.rect(screen, (255,255,255), x)
    for s in enemies:
        pygame.draw.rect(screen, (0,255,0),s)
    pygame.draw.rect(screen, (255,0,0),platform)
    pygame.display.update()



while True:
    if victory:
        print("ok")
        screen.fill((0,0,0))
        draw_text("You win!",font, screen, 500, 500)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    pygame.display.update()
                
    if lose:
        print("ok")
        screen.fill((0,0,0))
        draw_text("You lose!",font, screen, 500, 500)
        print("got it")
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    pygame.display.update()









    
            
