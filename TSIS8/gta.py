import pygame
import random
import time
pygame.init()

width, height = 500, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('GTA VI')
FPS = pygame.time.Clock()

car_x, car_y = 137, 520
ecar_x, ecar_y = 0, 0
speed = 8
road = pygame.image.load('road.png')
gameover = pygame.image.load('gameover.png')
coin = pygame.image.load('coin.png')
cnt_coin = pygame.image.load('cnt_coin.png')

font = pygame.font.SysFont('bookantiqua', 35)

class Car(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('car.png')
        self.surf = pygame.Surface((car_x, car_y))

    def move(self):
        global car_x, car_y, speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x >= 22:
            car_x -= speed
        elif keys[pygame.K_RIGHT] and car_x <= 390:
            car_x += speed
        
    def draw(self):
        screen.blit(self.image, (car_x, car_y))
    

class Enemy_car(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('enemy_car.png')
        self.surf = pygame.Surface((90, 170))
        self.spawn = [[20, -200], [142, -200], [273, -200], [387, -200]]
        self.spawn_point = random.randint(0, 3)
        self.speedometer = [6, 9, 12, 14, 16]
        self.speed = random.randint(0, 4)
    def move(self):
        global ecar_x, ecar_y
        self.spawn[self.spawn_point][1] += self.speedometer[self.speed]
        if self.spawn[self.spawn_point][1] >= height + 100:
            self.spawn[self.spawn_point][1] = -200
            self.spawn_point = random.randint(0, 3)
            self.speed = random.randint(0, 4)
        ecar_x = self.spawn[self.spawn_point][0]
        ecar_y = self.spawn[self.spawn_point][1]
    def draw(self):
        global ecar_x, ecar_y
        screen.blit(self.image, self.spawn[self.spawn_point])

bg_y = 0
def background():
    global bg_y, speed
    screen.blit(road, (0, bg_y))
    screen.blit(road, (0, bg_y - height))
    if bg_y >= height: bg_y -= height
    bg_y += speed

spawn = [random.randint(20, 430), -60]
cnt = 0
def draw_coin():
    global spawn, cnt
    global car_x, car_y
    screen.blit(coin, (spawn[0], spawn[1]))
    if spawn[1] > height: spawn = [random.randint(20, 430), -60]
    if car_x - 45 < spawn[0] < car_x + 90 and car_y - 45 < spawn[1] < car_y + 170:
        cnt += 1
        spawn = [random.randint(20, 430), -60]
    spawn[1] += 6
    screen.blit(cnt_coin, (10, 10))
    screen.blit(font.render(str(cnt), 1, (255, 255, 0)), (45, 5))

def crush_test():
    global ecar_x, ecar_y
    global car_x, car_y
    if ecar_x - 85 < car_x < ecar_x + 85 and car_y < ecar_y < car_y + 170:
        return True

car = Car()
enemy_car = Enemy_car()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if crush_test():
        screen.blit(gameover, (0, 0))
        screen.blit(font.render('COINS : ' + str(cnt), 1, (255, 255, 0)), (150, 500))
    else:
        background()
        draw_coin()
        car.move()
        enemy_car.move()
        car.draw()
        enemy_car.draw()
    pygame.display.update()
    FPS.tick(60)