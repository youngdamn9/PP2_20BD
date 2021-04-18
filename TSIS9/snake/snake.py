import pygame
import time 
import random
pygame.init()

WIDTH, HEIGHT = 720, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('жулан')

speed = 30
font = pygame.font.Font('font.ttf', 70)
galava = pygame.image.load('head.png')
food = pygame.image.load('food.png')
window = 0
button, button_s = 1, 1
intro_helper = 'menu'
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = pygame.time.Clock()
wall = [[120, 120], [160, 120], [200, 120], [120, 160], [120, 200],
        [480, 120], [520, 120], [560, 120], [560, 160], [560, 200],
        [120, 400], [120, 440], [120, 480], [160, 480], [200, 480],
        [560, 400], [560, 440], [560, 480], [520, 480], [480, 480]]
score = 0

def intro():
    global window, button, button_s, intro_helper
    screen.blit(pygame.image.load('intro.png'), (0, 0))
    if intro_helper == 'menu':
        if button == 1: screen.blit(font.render('PLAY', 0, RED), (320, 250))
        else: screen.blit(font.render('PLAY', 0, WHITE), (320, 250))
        if button == 2: screen.blit(font.render('SCORES', 0, RED), (300, 350))
        else: screen.blit(font.render('SCORES', 0, WHITE), (300, 350))
        if button == 3: screen.blit(font.render('EXIT', 0, RED), (320, 447))
        else: screen.blit(font.render('EXIT', 0, WHITE), (320, 447))

    key, k = pygame.key.get_pressed(), ''
    if key[pygame.K_RETURN]: k = 'ENTER'

    if key[pygame.K_DOWN] and button != 3:
        button += 1
        time.sleep(0.2)
    elif key[pygame.K_UP] and button != 1:
        button -= 1
        time.sleep(0.2)

    if button == 1 and key[pygame.K_RETURN]:
        intro_helper, k = 'stages', ''
        button = 0
        time.sleep(0.2)
    #elif button == 2 and 
        
    if intro_helper == 'stages':
        if button_s == 1: screen.blit(font.render('STAGE 1', 0, RED), (295, 250))
        else: screen.blit(font.render('STAGE 1', 0, WHITE), (295, 250))
        if button_s == 2: screen.blit(font.render('STAGE 2', 0, RED), (295, 350))
        else: screen.blit(font.render('STAGE 2', 0, WHITE), (295, 350))
        if button_s == 3: screen.blit(font.render('BACK', 0, RED), (315, 447))
        else: screen.blit(font.render('BACK', 0, WHITE), (315, 447))

        if key[pygame.K_DOWN] and button_s != 3:
            button_s += 1
            time.sleep(0.1)
        elif key[pygame.K_UP] and button_s != 1:
            button_s -= 1
            time.sleep(0.1)

        if button_s == 1 and k == 'ENTER': window = 1
        elif button_s == 2 and k == 'ENTER': window = 2
        elif button_s == 3 and k == 'ENTER':
            intro_helper = 'menu'
            button, button_s = 1, 1
            time.sleep(0.1)

    elif button == 2 and key[pygame.K_RETURN]:
        exit()
    elif button == 3 and key[pygame.K_RETURN]:
        exit()


snake_points = [[40, 160], [40, 120], [40, 80], [40, 40]]
key, timer = 'D', 0
dx, dy = 0, 0
appetit = False
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        self.body = pygame.image.load('body.png')
        self.head = pygame.image.load('head.png')

    def move(self):
        global snake_points, key, galava
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and key != 'R':
            key = 'L'
            self.head = pygame.transform.rotate(galava, -90)
        elif keys[pygame.K_RIGHT] and key != 'L' :
            key = 'R'
            self.head = pygame.transform.rotate(galava, 90)
        elif keys[pygame.K_DOWN] and key != 'U':
            key = 'D'
            self.head = pygame.transform.rotate(galava, 0)
        elif keys[pygame.K_UP] and key != 'D': 
            key = 'U'
            self.head = pygame.transform.rotate(galava, 180)
        

    def draw(self):
        global timer, appetit, snake_points, dx, dy, speed, score
        if timer % speed == 0:
            dx, dy = snake_points[-1][0], snake_points[-1][1]
            if key == 'L':
                for i in range(len(snake_points) - 1, 0, -1):
                    snake_points[i][0] = snake_points[i - 1][0]
                    snake_points[i][1] = snake_points[i - 1][1]
                snake_points[0][0] -= 40
            elif key == 'R':
                for i in range(len(snake_points) - 1, 0, -1):
                    snake_points[i][0] = snake_points[i - 1][0]
                    snake_points[i][1] = snake_points[i - 1][1]
                snake_points[0][0] += 40
            elif key == 'D':
                for i in range(len(snake_points) - 1, 0, -1):
                    snake_points[i][0] = snake_points[i - 1][0]
                    snake_points[i][1] = snake_points[i - 1][1]
                snake_points[0][1] += 40
            elif key == 'U':
                for i in range(len(snake_points) - 1, 0, -1):
                    snake_points[i][0] = snake_points[i - 1][0]
                    snake_points[i][1] = snake_points[i - 1][1]
                snake_points[0][1] -= 40
        if appetit == True:
            snake_points.append([dx, dy])
            if len(snake_points) % 5 == 0: speed -= 3
            score += 1
            appetit = False

        
        for i in range(len(snake_points)):
            if i == 0: screen.blit(self.head, snake_points[i])
            else: screen.blit(self.body, snake_points[i])


fx, fy = random.randrange(40, WIDTH - 60, 40), random.randrange(40, HEIGHT - 100, 40)
class Food(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('food.png')
        self.x = random.randrange(40, WIDTH - 60, 40)
        self.y = random.randrange(40, HEIGHT - 100, 40)

    def spawn(self):
        global snake_points, appetit, score
        screen.blit(self.image, [self.x, self.y])
        if self.x == snake_points[0][0] and self.y == snake_points[0][1]:
            appetit = True
            while [self.x, self.y] in snake_points or [self.x, self.y] in wall:
                self.x = random.randrange(40, WIDTH - 60, 40)
                self.y = random.randrange(40, HEIGHT - 100, 40)

def draw_score():
    font = pygame.font.Font('font.ttf', 70)
    screen.blit(font.render('SCORE: {}'.format(score), 0, WHITE), (20, HEIGHT - 60))
        

def crush_test():
    global window
    if snake_points[0][0] < 40 or snake_points[0][0] > WIDTH - 80: window = -1
    if snake_points[0][1] < 40 or snake_points[0][1] > HEIGHT - 140: window = -1
    if snake_points[0] in snake_points[1:]: window = -1
    if window == 2 and snake_points[0] in wall: window = -1

def game_over():
    screen.blit(pygame.image.load('gameover.png'), (0, 0))
    font = pygame.font.Font('font.ttf', 200)
    screen.blit(font.render('GAME OVER', 0, BLACK), (105, 195))
    screen.blit(font.render('GAME OVER', 0, WHITE), (100, 200))
    pygame.draw.rect(screen, WHITE, (100, 340, 520, 10))
    font = pygame.font.Font('font.ttf', 100)
    screen.blit(font.render('YOUR SCORE: {}'.format(score), 0, WHITE), (180 ,360))

ss = Snake()
food = Food()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if window == 0:
        intro()

    elif window == 1:
        timer += 1
        screen.blit(pygame.image.load('stage_1.png'), (0, 0))
        food.spawn()
        ss.move()
        ss.draw()
        draw_score()
        crush_test()

    elif window == 2:
        timer += 1
        screen.blit(pygame.image.load('stage_2.png'), (0, 0))
        food.spawn()
        ss.move()
        ss.draw()
        draw_score()
        crush_test()

    elif window == -1:
        game_over()

    pygame.display.update()