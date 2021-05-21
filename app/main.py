import pygame
import time
import random
import threading
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
dis_width = 2000
dis_height = 1000
themap = 'start'
e = 'sword'
gold = 0
map2 = pygame.image.load('/Users/jackm/Desktop/app/images/map1.gif')
map2 = pygame.transform.scale(map2, (dis_width, dis_height))
map3 = pygame.image.load('/Users/jackm/Desktop/app/images/0.png')
door = pygame.image.load('/Users/jackm/Desktop/app/images/door.gif')
shop = pygame.image.load('/Users/jackm/Desktop/app/images/shop.gif')
sword2 = pygame.image.load('/Users/jackm/Desktop/app/images/sword.png')
redstaff = pygame.image.load('/Users/jackm/Desktop/app/images/redstaff.png')
button = pygame.image.load('/Users/jackm/Desktop/app/images/buttonRedStaff.png')
buttonD = False
dis = pygame.display.set_mode((dis_width, dis_height), pygame.RESIZABLE)
pygame.display.set_caption('PixelQuest')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 150
totalSwordRot = 0
class Keydown:
    def __init__(self):
        self.down = False
        self.key = ''
keydown = Keydown()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
class Sword:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.justHit = False
        self.beenDrawn = False
        self.Used = False
        self.justHit = False
        self.face = "left"
    def draw(self):
         global sword2
         sword2 = pygame.transform.scale(sword2, (100, 100))
         if e == 'sword':
            if keydown.key == 'w' or keydown.key == 'd':
                dis.blit(sword2, (position[0] + 30, position[1]))
            else:
                dis.blit(sword2, (position[0] - 60, position[1]))
         else:
            dis.blit(sword2, (380, 100))
    def hit(self):
        global sword2
        global totalSwordRot
        if keydown.key == 'd':
            if not self.justHit:
                self.justHit = True
                sword2 = pygame.transform.rotate(sword2, totalSwordRot + -totalSwordRot)
                sword2 = pygame.transform.rotate(sword2, -90)
                totalSwordRot = totalSwordRot - 90
                def test():
                    global sword2
                    global totalSwordRot
                    sword2 = pygame.transform.rotate(sword2, 90)
                    totalSwordRot = totalSwordRot + 90
                    self.justHit = False
                f=threading.Timer(.25,test)
                f.start()
        elif keydown.key == 'a':
            if not self.justHit:
                self.justHit = True
                sword2 = pygame.transform.rotate(sword2, totalSwordRot + -totalSwordRot)
                sword2 = pygame.transform.rotate(sword2, 90)
                def test():
                    global sword2
                    sword2 = pygame.transform.rotate(sword2, -90)
                    self.justHit = False
                f=threading.Timer(.25,test)
                f.start()
class RedStaff:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.price = 7
        self.Used = False
    def draw(self):
        global redstaff
        redstaff = pygame.transform.scale(redstaff, (100, 100))
        if e != 'redstaff':
            dis.blit(redstaff, (self.x, self.y))
        else:
            if keydown.key == 'w' or keydown.key == 'd':
                dis.blit(redstaff, (position[0] + 30, position[1]))
            else:
                dis.blit(redstaff, (position[0] - 60, position[1]))
    def shoot(self, d):
        pass
redstaff2 = RedStaff(160, 100)
sword = Sword(10, 10)
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
        global sword
        global sword2
        global e
        global gold
        global buttonD
        # clear frame
        dis.fill((0, 0, 0))
        surface = pygame.display.get_surface()
        dis_width = surface.get_width()
        dis_height = surface.get_height()
        if themap == 'start':
            map2 = pygame.transform.scale(map2, (dis_width, dis_height))
            dis.blit(map2, (0, 0))
            shop = pygame.transform.scale(shop, (200, 410))
            dis.blit(shop, (500, 10))
            if e == 'sword':
                sword.draw()
            elif e == 'redstaff':
                redstaff2.draw()
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
            if buttonD == True:
                dis.blit(button, (dis_width / 5, dis_height - 200))
        elif themap == 'shop':
            def checkoutside():
                return (
                    position[0] > dis_width - 50 or
                    position[0] < 0 or
                    position[1] < 0 or
                    position[1] > dis_height - 50
                )
            map3 = pygame.transform.scale(map3, (dis_width, dis_height))
            dis.blit(map3, (0, 0))
            door = pygame.transform.scale(door, (300, 500))
            dis.blit(door, ((dis_width / 2) - 300, -100))
            dis.blit(door, ((dis_width / 2), -100))
            redstaff2.draw()
            sword.draw()
            dis.blit(theimg, (position[0], position[1]))
            if buttonD == True:
                dis.blit(button, (dis_width / 5, dis_height - 200))
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
                        if check(position, [10, 350, 500, 700], 0) == True:
                            position[1] = position[1] + 10
                        if checkoutside() == True:
                            position[1] = position[1] + 10
                    keydown.down = True
                    keydown.key = 'w'
                elif event.key == pygame.K_s:
                    position[1] = position[1] + 10
                    if themap == 'start':
                        if check(position, [10, 350, 500, 700], 0) == True:
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
                        if check(position, [10, 350, 500, 700], 0) == True:
                            position[0] = position[0] + 10
                    if checkoutside() == True:
                        position[0] = position[0] + 10
                    theimg = img4
                    keydown.down = True
                    keydown.key = 'a'
                elif event.key == pygame.K_d:
                    position[0] = position[0] + 10
                    if themap == 'start':
                        if check(position, [10, 350, 500, 700], 0) == True:
                            position[0] = position[0] - 10
                    if checkoutside() == True:
                        position[0] = position[0] - 10
                    theimg = img2
                    keydown.down = True
                    keydown.key = 'd'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttonD == True:
                    posX, posY = pygame.mouse.get_pos()
                    rect = button.get_rect(topleft=(dis_width / 5, dis_height - 200))
                    def collide():
                        return not (
                            posY > rect.bottom or
                            posX < rect.left or
                            posY < rect.top or
                            posX > rect.right
                        )
                    if collide() == True:
                        buttonD = False
                if themap == 'shop' and e != 'redstaff':
                    posX, posY = pygame.mouse.get_pos()
                    rect = redstaff.get_rect(topleft=(160, 100))
                    def collide():
                        return not (
                            posY > rect.bottom or
                            posX < rect.left or
                            posY < rect.top or
                            posX > rect.right
                        )
                    if collide() == True:
                        # buy the redstaff
                        if redstaff2.Used == False:
                            if gold > 7 or gold == 7:
                                gold = gold - 7
                                e = 'redstaff'
                                redstaff2.Used = True
                            else:
                                buttonD = True
                        else:
                            e = 'redstaff'
                            redstaff2.Used = True
                elif themap == 'shop' and e != 'sword':
                    posX, posY = pygame.mouse.get_pos()
                    rect = sword2.get_rect(topleft=(380, 100))
                    def collide():
                        return not (
                            posY > rect.bottom or
                            posX < rect.left or
                            posY < rect.top or
                            posX > rect.right
                        )
                    if collide() == True:
                        print 'huh?'
                        e = 'sword'
                if e == 'sword':
                    sword.hit()
                elif e == 'redstaff':
                    if keydown.key == 'd':
                        redstaff2.shoot('d')
                    elif keydown.key == 'a':
                        redstaff2.shoot('a')
                    elif keydown.key == 's':
                        redstaff2.shoot('a')
                    elif keydown.key == 'w':
                        redstaff2.shoot('w')
                    else:
                        redstaff2.shoot('w')
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
                if check(position, [10, 350, 500, 700], 0) == True:
                    position[1] = position[1] + 10
                    themap = 'shop'
                elif checkoutside() == True:
                    position[1] = position[1] + 10
            elif themap == 'shop':
                if checkoutside() == True:
                    position[1] = position[1] + 10
                    themap = 'start'
                    position[0] = 600
                    position[1] = 600
        elif keydown.down == True and keydown.key == 's':
            position[1] = position[1] + 10
            if themap == 'start':
                if check(position, [10, 350, 500, 700], 0) == True:
                    position[1] = position[1] - 10
            if checkoutside() == True:
                position[1] = position[1] - 10 
        elif keydown.down == True and keydown.key == 'a':
            position[0] = position[0] - 10
            if themap == 'start':
                if check(position, [10, 350, 500, 700], 0) == True:
                    position[0] = position[0] + 10
            if checkoutside() == True:
                position[0] = position[0] + 10
        elif keydown.down == True and keydown.key == 'd':
            position[0] = position[0] + 10
            if themap == 'start':
                if check(position, [10, 350, 500, 700], 0) == True:
                    position[0] = position[0] - 10
            if checkoutside() == True:
                position[0] = position[0] - 10
        pygame.display.flip()
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
gameLoop()
