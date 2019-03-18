import pygame
import sys
from pygame.locals import *

pygame.init()
main_clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,460))
screen.fill((0,0,0))

pygame.display.set_caption("Bubble Blaster")

player = pygame.Rect(300,400,60,10)
move_left = False
move_right = False
move_up = False
move_down = False
player_speed = 10
all_bubbles =[]
bubble_radius = 20
intial_pos = 70
spacing = 60
bubble_edge = 1
xb = 380
yb = 320
lxb = xb
lyb = yb
speed = [5,-5]
ballm = False
pygame.display.set_caption("Bubble Blaster")
font = pygame.font.SysFont(None, 36)

def draw_text(display_string, font, surf, x,y):
    textd = font.render(display_string,1,(255,200,0))
    textrect = textd.get_rect()
    textrect.topleft = (x,y)
    surf.blit(textd,textrect)

    
def create():
    bx = intial_pos
    by = intial_pos

    for rows in range(0,3):
        for columns in range(0,10):
            bubble = pygame.draw.circle((screen), (17,193,67), (bx,by), bubble_radius, bubble_edge)
            bx += spacing
            all_bubbles.append(bubble)
        by += spacing
        bx = intial_pos
def draw():
    for bubble in all_bubbles:
        bubble = pygame.draw.circle((screen), (17,193,67), (bubble.x, bubble.y), bubble_radius, bubble_edge)
create()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == KEYDOWN:
            if event.key == K_a:
                move_right = False
                move_left = True
                move_down = False
                move_up = False
            if event.key == K_d:
                move_left = False
                move_right = True
                move_down = False
                move_up = False
            
        if event.type == KEYUP:
            if event.key == K_a:
                move_left = False
            if event.key == K_d:
                move_right = False
            if event.key == K_w:
                move_up == False
            if event.key == K_s:
                move_down = False
            if event.key == K_SPACE:
                ballm = True

            
    main_clock.tick(50)
    if move_left and player.left > 0:
        player.x -= player_speed
    if move_right and player.right < 640:
        player.x += player_speed
    if ballm:
        lxb = xb
        lyb = yb
        xb += speed[0]
        yb += speed[1]
        if ball.x <=0:
            xb = 15
            speed[0]=-speed[0]
        if ball.x >= 640:
            xb = 625
            speed[0] = -speed[0]
        if ball.y <= 0:
            yb = 15
            speed[1] = -speed[1]
        if ball.colliderect(player):
            yb -= 15
            speed[1] = -speed[1]
        moved = ((xb-lxb),(yb-lyb))
        for bubble in all_bubbles:
            if ball.colliderect(bubble):
                if moved[1] > 0:
                    speed[1] = -speed[1]
                    yb -= 10
                elif moved[1] < 0:
                    speed[1]=-speed[1]
                    yb += 10
                all_bubbles.remove(bubble)
                break
                
    else:
        xb = player.x+30
    screen.fill((0,0,0))
    draw()
    ball = pygame.draw.circle(screen, (0,0,255), (xb,yb), 5,0)
    pygame.draw.rect(screen, (255,255,255), player)
    draw_text("Text", font, screen, 5,5)
    pygame.display.update()
    

































    
            
