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
gold = 12
health = 10
map2 = pygame.image.load('/Users/jackm/Desktop/app/images/map1.gif')
map2 = pygame.transform.scale(map2, (dis_width, dis_height))
map3 = pygame.image.load('/Users/jackm/Desktop/app/images/0.png')
door = pygame.image.load('/Users/jackm/Desktop/app/images/door.gif')
shop = pygame.image.load('/Users/jackm/Desktop/app/images/shop.gif')
sword2 = pygame.image.load('/Users/jackm/Desktop/app/images/sword.png')
redstaff = pygame.image.load('/Users/jackm/Desktop/app/images/redstaff.png')
greenstaff = pygame.image.load('/Users/jackm/Desktop/app/images/greenstaff.png')
button = pygame.image.load('/Users/jackm/Desktop/app/images/buttonRedStaff.png')
button2 = pygame.image.load('/Users/jackm/Desktop/app/images/buttonGreenStaff.png')
infoP = pygame.image.load('/Users/jackm/Desktop/app/images/info.png')
br = pygame.image.load('/Users/jackm/Desktop/app/images/br.png')
bullet = pygame.image.load('/Users/jackm/Desktop/app/images/redstaffbullet.gif')
bullet2 = pygame.image.load('/Users/jackm/Desktop/app/images/greenstaffbullet.png')
bullet3 = pygame.image.load('/Users/jackm/Desktop/app/images/greenstaffbullet2.png')
bullet4 = pygame.image.load('/Users/jackm/Desktop/app/images/greenstaffbullet3.png')
bullet5 = pygame.image.load('/Users/jackm/Desktop/app/images/greenstaffbullet4.png')
icon = pygame.image.load('/Users/jackm/Desktop/app/applet.icns')
buttonD = False
buttonD2 = False
dis = pygame.display.set_mode((dis_width, dis_height), pygame.RESIZABLE)
pygame.display.set_caption('PixelQuest')
icon = pygame.transform.scale(icon, (200, 200))
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
inmessage = False
snake_block = 10
snake_speed = 1500
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
        self.price = 5
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
class GreenStaff:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.price = 7
        self.Used = False
    def draw(self):
        global greenstaff
        greenstaff = pygame.transform.scale(greenstaff, (100, 100))
        if e != 'greenstaff':
            dis.blit(greenstaff, (self.x, self.y))
        else:
            if keydown.key == 'w' or keydown.key == 'd':
                dis.blit(greenstaff, (position[0] + 30, position[1]))
            else:
                dis.blit(greenstaff, (position[0] - 60, position[1]))
greenstaff2 = GreenStaff(300, 100)
class GreenStaffBullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.startPosition = (position[0], position[1])
        self.fromStartpositon = 0
        self.justShot = False
        self.shotDirection = ''
    def shoot(self):
        global bullet2
        global bullet3
        global bullet4
        global bullet5
        if not self.justShot:
            self.startPosition = (position[0], position[1])
            self.ye = position[1]
            self.xe = position[0]
            self.y = position[1]
            self.fromStartpositon = 0
            self.shotDirection = keydown.key
            self.justShot = True
            bullet2 = pygame.transform.scale(bullet2, (100, 100))
            bullet3 = pygame.transform.scale(bullet3, (100, 100))
            bullet4 = pygame.transform.scale(bullet4, (100, 100))
            bullet5 = pygame.transform.scale(bullet5, (100, 100))
            if self.shotDirection == 'd':
                dis.blit(bullet2, self.startPosition)
            elif self.shotDirection == 'a':
                dis.blit(bullet3, self.startPosition)
            elif self.shotDirection == 'w':
                dis.blit(bullet4, self.startPosition)
            elif self.shotDirection == 's':
                dis.blit(bullet5, self.startPosition)
        else:
            if self.shotDirection == 'd':
                    dis.blit(bullet2, (self.x, self.y))
            elif self.shotDirection == 'a':
                    dis.blit(bullet3, (self.x, self.y))
            elif self.shotDirection == 'w':
                    dis.blit(bullet4, (self.x, self.y))
            elif self.shotDirection == 's':
                    dis.blit(bullet5, (self.x, self.y))
            if not self.check(bullet2, shop) and not self.checkoutside():
                if self.shotDirection == 'd':
                    self.fromStartpositon = self.fromStartpositon + 100
                    self.x = self.x + 100
                    self.y = self.ye
                elif self.shotDirection == 'a':
                    self.fromStartpositon = self.fromStartpositon - 100
                    self.x = self.x - 100
                    self.y = self.ye
                elif self.shotDirection == 'w':
                    self.fromStartpositon = self.fromStartpositon - 100
                    self.y = self.y - 100
                    self.x = self.xe
                elif self.shotDirection == 's':
                    self.fromStartpositon = self.fromStartpositon + 100
                    self.y = self.y + 100
                    self.x = self.xe
            else:
                self.x = position[0]
                self.y = position[1]
                self.fromStartpositon = 0
                self.justShot = False
    def check(self, player, el2):
        if themap == 'start':
            rect2 = el2.get_rect(topleft=(500, 10))
            return not (
                self.x > rect2.right or
                self.x < rect2.left or
                self.y < rect2.top or
                self.y > rect2.bottom 
            )
        elif themap == 'shop':
            return False
    def checkoutside(self):
        return (
            self.x > dis_width or
            self.x < 0 or
            self.y < 0 or
            self.y > dis_height
        )
class RedStaffBullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.startPosition = (position[0], position[1])
        self.fromStartpositon = 0
        self.justShot = False
        self.shotDirection = ''
    def shoot(self):
        if not self.justShot:
            self.startPosition = (position[0], position[1])
            self.ye = position[1]
            self.xe = position[0]
            self.y = position[1]
            self.fromStartpositon = 0
            self.shotDirection = keydown.key
            self.justShot = True
            dis.blit(bullet, self.startPosition)
        else:
            dis.blit(bullet, (self.x, self.y))
            if not self.check(bullet, shop) and not self.checkoutside():
                if self.shotDirection == 'd':
                    self.fromStartpositon = self.fromStartpositon + 100
                    self.x = self.x + 100
                    self.y = self.ye
                elif self.shotDirection == 'a':
                    self.fromStartpositon = self.fromStartpositon - 100
                    self.x = self.x - 100
                    self.y = self.ye
                elif self.shotDirection == 'w':
                    self.fromStartpositon = self.fromStartpositon - 100
                    self.y = self.y - 100
                    self.x = self.xe
                elif self.shotDirection == 's':
                    self.fromStartpositon = self.fromStartpositon + 100
                    self.y = self.y + 100
                    self.x = self.xe
            else:
                self.x = position[0]
                self.y = position[1]
                self.fromStartpositon = 0
                self.justShot = False
    def check(self, player, el2):
        if themap == 'start':
            rect2 = el2.get_rect(topleft=(500, 10))
            return not (
                self.x > rect2.right or
                self.x < rect2.left or
                self.y < rect2.top or
                self.y > rect2.bottom 
            )
        elif themap == 'shop':
            return False
    def checkoutside(self):
        return (
            self.x > dis_width or
            self.x < 0 or
            self.y < 0 or
            self.y > dis_height
        )
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
redstaffB = RedStaffBullet(position[0], position[1])
greenstaffB = GreenStaffBullet(position[0], position[1])
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
        global inmessage
        global buttonD2
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
            elif e == 'greenstaff':
                greenstaff2.draw()
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
            dis.blit(infoP, (dis_width - 170, 60))
            dis.blit(br, (dis_width - 150, 120))
            message('Gold: ' + str(gold), (dis_width - 140, 100), black)
            message('Health: ' + str(health), (dis_width - 150, 140), black)
            if redstaffB.justShot == True:
                redstaffB.shoot()
            if greenstaffB.justShot == True:
                greenstaffB.shoot()
            if buttonD == True:
                dis.blit(button, (dis_width / 5, dis_height - 200))
                inmessage = True
            elif buttonD2 == True:
                dis.blit(button2, (dis_width / 5, dis_height - 200))
                inmessage = True
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
            greenstaff2.draw()
            dis.blit(theimg, (position[0], position[1]))
            dis.blit(infoP, (dis_width - 170, 60))
            dis.blit(br, (dis_width - 150, 120))
            message('Gold: ' + str(gold), (dis_width - 140, 100), black)
            message('Health: ' + str(health), (dis_width - 150, 140), black)
            if redstaffB.justShot == True:
                redstaffB.shoot()
            if greenstaffB.justShot == True:
                greenstaffB.shoot()
            if buttonD == True:
                dis.blit(button, (dis_width / 5, dis_height - 200))
                inmessage = True
            elif buttonD2 == True:
                dis.blit(button2, (dis_width / 5, dis_height - 200))
                inmessage = True
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN and inmessage == False:
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
                        inmessage = False
                elif buttonD2 == True:
                    posX, posY = pygame.mouse.get_pos()
                    rect = button2.get_rect(topleft=(dis_width / 5, dis_height - 200))
                    def collide():
                        return not (
                            posY > rect.bottom or
                            posX < rect.left or
                            posY < rect.top or
                            posX > rect.right
                        )
                    if collide() == True:
                        buttonD2 = False
                        inmessage = False
                if e == 'redstaff' and inmessage == False:
                    redstaffB.shoot()
                if e == 'greenstaff' and inmessage == False:
                    greenstaffB.shoot()
                if themap == 'shop' and e != 'redstaff' and inmessage == False:
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
                            if gold > redstaff2.price or gold == redstaff2.price:
                                gold = gold - redstaff2.price
                                e = 'redstaff'
                                redstaff2.Used = True
                            else:
                                buttonD = True
                        else:
                            e = 'redstaff'
                            redstaff2.Used = True
                if themap == 'shop' and e != 'greenstaff' and inmessage == False:
                    posX, posY = pygame.mouse.get_pos()
                    rect = greenstaff.get_rect(topleft=(300, 100))
                    def collide():
                        return not (
                            posY > rect.bottom or
                            posX < rect.left or
                            posY < rect.top or
                            posX > rect.right
                        )
                    if collide() == True:
                        # buy the greenstaff
                        if greenstaff2.Used == False:
                            if gold > greenstaff2.price or gold == greenstaff2.price:
                                gold = gold - greenstaff2.price
                                e = 'greenstaff'
                                greenstaff2.Used = True
                            else:
                                buttonD2 = True
                        else:
                            e = 'greenstaff'
                            greenstaff2.Used = True
                if themap == 'shop' and inmessage == False and e != 'sword':
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
                        e = 'sword'
                if e == 'sword' and inmessage == False:
                    sword.hit()
                elif e == 'redstaff' and inmessage == False:
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
        if inmessage == False:
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
