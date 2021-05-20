import pygame
import time
import random
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
img = pygame.image.load('/Users/jackm/Desktop/app/images/0-1.gif')
img2 = pygame.image.load('/Users/jackm/Desktop/app/images/0-2.gif')
img3 = pygame.image.load('/Users/jackm/Desktop/app/images/0-3.gif')
img4 = pygame.image.load('/Users/jackm/Desktop/app/images/0-4.gif')
theimg = img
dis_width = 600
dis_height = 400
themap = 'start'
map2 = pygame.image.load('/Users/jackm/Desktop/app/images/map1.gif')
map2 = pygame.transform.scale(map2, (dis_width, dis_height))
map3 = pygame.image.load('/Users/jackm/Desktop/app/images/0.png')
door = pygame.image.load('/Users/jackm/Desktop/app/images/door.gif')
shop = pygame.image.load('/Users/jackm/Desktop/app/images/shop.gif')
dis = pygame.display.set_mode((dis_width, dis_height), pygame.RESIZABLE)
pygame.display.set_caption('Game')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 150
class Keydown:
     def __init__(self):
         self.down = False
         self.key = ''
keydown = Keydown()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, were, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, were)
 
position = [dis_width / 2 - 20, dis_height / 2 - 20]
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    while not game_over:
        global dis_width
        global dis_height
        global keydown
        global theimg
        global map2
        global shop
        global themap
        global map3
        global door
        # clear frame
        dis.fill((0, 0, 0))
        surface = pygame.display.get_surface()
        dis_width = surface.get_width()
        dis_height = surface.get_height()
        if themap == 'start':
            map2 = pygame.transform.scale(map2, (dis_width, dis_height))
            dis.blit(map2, (0, 0))
            shop = pygame.transform.scale(shop, (200, 400))
            dis.blit(shop, (500, 10))
            dis.blit(theimg, (position[0], position[1]))
            def check(player, el2, offset):
                # 1: top, 2: bottom, 3: left, 4: right 
                rect1 = player
                rect2 = el2
                return not (
                rect1[1] > rect2[1] - offset or
                rect1[0] + 100 < rect2[2] + offset or
                rect1[1] + 100 < rect2[0] + offset or
                rect1[0] > rect2[3] - offset
                )
            def checkoutside():
                return (
                    position[0] > dis_width - 50 or
                    position[0] < 0 or
                    position[1] < -50 or
                    position[1] > dis_height - 50
                )
        elif themap == 'shop':
            map3 = pygame.transform.scale(map3, (dis_width, dis_height))
            dis.blit(map3, (0, 0))
            door = pygame.transform.scale(door, (400, 500))
            dis.blit(door, ((dis_width / 2) - 300, -100))
            dis.blit(door, ((dis_width / 2), -100))
            dis.blit(theimg, (position[0], position[1]))
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    position[1] = position[1] - 10
                    theimg = img
                    if themap == 'start':
                        if check(position, [10, 410, 500, 700], 0) == True:
                            position[1] = position[1] + 10
                    elif themap == 'shop':
                        if checkoutside() == True:
                            position[1] = position[1] + 10
                            themap = 'start'
                    keydown.down = True
                    keydown.key = 'w'
                elif event.key == pygame.K_s:
                    position[1] = position[1] + 10
                    if themap == 'start':
                        if check(position, [10, 410, 500, 700], 0) == True:
                            position[1] = position[1] - 10
                            themap = 'shop'
                    if checkoutside() == True:
                        position[1] = position[1] - 10
                    theimg = img3
                    keydown.down = True
                    keydown.key = 's'
                elif event.key == pygame.K_a:
                    position[0] = position[0] - 10
                    if themap == 'start':
                        if check(position, [10, 410, 500, 700], 0) == True:
                            position[0] = position[0] + 10
                    if checkoutside() == True:
                        position[0] = position[0] + 10
                    theimg = img4
                    keydown.down = True
                    keydown.key = 'a'
                elif event.key == pygame.K_d:
                    position[0] = position[0] + 10
                    if themap == 'start':
                        if check(position, [10, 410, 500, 700], 0) == True:
                            position[0] = position[0] - 10
                    if checkoutside() == True:
                        position[0] = position[0] - 10
                    theimg = img2
                    keydown.down = True
                    keydown.key = 'd'
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    keydown.down = False
                elif event.key == pygame.K_s:
                    keydown.down = False
                elif event.key == pygame.K_a:
                    keydown.down = False
                elif event.key == pygame.K_s:
                    keydown.down = False
                elif event.key == pygame.K_d:
                    keydown.down = False
        if keydown.down == True and keydown.key == 'w':
            position[1] = position[1] - 10
            if themap == 'start':
                if check(position, [10, 410, 500, 700], 0) == True:
                    position[1] = position[1] + 10
                    themap = 'shop'
            elif themap == 'shop':
                if checkoutside() == True:
                    position[1] = position[1] + 10
                    themap = 'start'
                    position[0] = 600
                    position[1] = 600
        elif keydown.down == True and keydown.key == 's':
            position[1] = position[1] + 10
            if themap == 'start':
                if check(position, [10, 410, 500, 700], 0) == True:
                    position[1] = position[1] - 10
            if checkoutside() == True:
                position[1] = position[1] - 10 
        elif keydown.down == True and keydown.key == 'a':
            position[0] = position[0] - 10
            if themap == 'start':
                if check(position, [10, 410, 500, 700], 0) == True:
                    position[0] = position[0] + 10
            if checkoutside() == True:
                position[0] = position[0] + 10
        elif keydown.down == True and keydown.key == 'd':
            position[0] = position[0] + 10
            if themap == 'start':
                if check(position, [10, 410, 500, 700], 0) == True:
                    position[0] = position[0] - 10
            if checkoutside() == True:
                position[0] = position[0] - 10
        pygame.display.update()
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()

