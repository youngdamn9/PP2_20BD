import pygame
import time 
import random
pygame.init()

WIDTH, HEIGHT = 720, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('жулан')

font = pygame.font.Font('font.ttf', 60)
galava = pygame.image.load('pics/head.png')
food = pygame.image.load('pics/food.png')
window = 0

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = pygame.time.Clock()
wall = [[120, 120], [160, 120], [200, 120], [120, 160], [120, 200],
        [480, 120], [520, 120], [560, 120], [560, 160], [560, 200],
        [120, 400], [120, 440], [120, 480], [160, 480], [200, 480],
        [560, 400], [560, 440], [560, 480], [520, 480], [480, 480]]

button = [1, 2, 3, 4]
i, k = 1, ''
gamers, stage = 1, 1
def intro():
    global button, i, gamers, stage, k, window
    screen.blit(pygame.image.load('pics/intro.png'), (0, 0))
    if i == 1: pygame.draw.rect(screen, RED, pygame.Rect(100, 300, 200, 50), 5)
    else: pygame.draw.rect(screen, WHITE, pygame.Rect(100, 300, 200, 50), 5)
    if i == 2: pygame.draw.rect(screen, RED, pygame.Rect(420, 300, 200, 50), 5)
    else: pygame.draw.rect(screen, WHITE, pygame.Rect(420, 300, 200, 50), 5)
    if i == 3: pygame.draw.rect(screen, RED, pygame.Rect(100, 400, 200, 50), 5)
    else: pygame.draw.rect(screen, WHITE, pygame.Rect(100, 400, 200, 50), 5)
    if i == 4: pygame.draw.rect(screen, RED, pygame.Rect(420, 400, 200, 50), 5)
    else: pygame.draw.rect(screen, WHITE, pygame.Rect(420, 400, 200, 50), 5)

    key = pygame.key.get_pressed()
    if key[pygame.K_RETURN]: k = 'ENTER'
    if key[pygame.K_RIGHT] and i == 1: i = 2
    if key[pygame.K_DOWN] and i == 1: i = 3
    if key[pygame.K_LEFT] and i == 2: i = 1
    if key[pygame.K_DOWN] and i == 2: i = 4
    if key[pygame.K_RIGHT] and i == 3: i = 4
    if key[pygame.K_UP] and i == 3: i = 1
    if key[pygame.K_LEFT] and i == 4: i = 3
    if key[pygame.K_UP] and i == 4: i = 2

    screen.blit(font.render('PLAY', 0, WHITE), (165, 300))
    screen.blit(font.render('SCORES', 0, WHITE), (470, 300))
    screen.blit(font.render('PLAYERS: {}'.format(gamers), 0, WHITE), (125, 400))
    screen.blit(font.render('STAGE: {}'.format(stage), 0, WHITE), (460, 400))

    if i == 1 and k == 'ENTER':
        if stage == 1: window = 1
        else: window = 2
    if i == 3 and k == 'ENTER':
        if gamers == 1: gamers = 2
        else: gamers = 1
        k = ''
        time.sleep(0.2)
    if i == 4 and k == 'ENTER':
        if stage == 1: stage = 2
        else: stage = 1
        k = ''
        time.sleep(0.2)
    





snake_points = [[40, 160], [40, 120], [40, 80], [40, 40]]
key, timer = 'D', 0
dx, dy = 0, 0
appetit = False
speed, score = 30, 0
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        self.body = pygame.image.load('pics/body.png')
        self.head = pygame.image.load('pics/head.png')

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
            if score % 5 == 0: speed -= 3
            score += 1
            appetit = False

        
        for i in range(len(snake_points)):
            if i == 0: screen.blit(self.head, snake_points[i])
            else: screen.blit(self.body, snake_points[i])

snake_points2 = [[640, 160], [640, 120], [640, 80], [640, 40]]
key2 = 'D'
appetit2 = False
dx2, dy2 = 0, 0
speed2, score2 = 30, 0
class Snake_2(pygame.sprite.Sprite):
    def __init__(self):
        self.body = pygame.image.load('pics/body.png')
        self.head = pygame.image.load('pics/head.png')

    def move(self):
        global snake_points2, key2, galava
        keys2 = pygame.key.get_pressed()
        if keys2[pygame.K_a] and key2 != 'R':
            key2 = 'L'
            self.head = pygame.transform.rotate(galava, -90)
        elif keys2[pygame.K_d] and key2 != 'L' :
            key2 = 'R'
            self.head = pygame.transform.rotate(galava, 90)
        elif keys2[pygame.K_s] and key2 != 'U':
            key2 = 'D'
            self.head = pygame.transform.rotate(galava, 0)
        elif keys2[pygame.K_w] and key2 != 'D': 
            key2 = 'U'
            self.head = pygame.transform.rotate(galava, 180)
        

    def draw(self):
        global timer, snake_points2, speed2, appetit2, dx2, dy2, score2
        if timer % speed2 == 0:
            dx2, dy2 = snake_points2[-1][0], snake_points2[-1][1]
            if key2 == 'L':
                for i in range(len(snake_points2) - 1, 0, -1):
                    snake_points2[i][0] = snake_points2[i - 1][0]
                    snake_points2[i][1] = snake_points2[i - 1][1]
                snake_points2[0][0] -= 40
            elif key2 == 'R':
                for i in range(len(snake_points2) - 1, 0, -1):
                    snake_points2[i][0] = snake_points2[i - 1][0]
                    snake_points2[i][1] = snake_points2[i - 1][1]
                snake_points2[0][0] += 40
            elif key2 == 'D':
                for i in range(len(snake_points2) - 1, 0, -1):
                    snake_points2[i][0] = snake_points2[i - 1][0]
                    snake_points2[i][1] = snake_points2[i - 1][1]
                snake_points2[0][1] += 40
            elif key2 == 'U':
                for i in range(len(snake_points2) - 1, 0, -1):
                    snake_points2[i][0] = snake_points2[i - 1][0]
                    snake_points2[i][1] = snake_points2[i - 1][1]
                snake_points2[0][1] -= 40

        if appetit2 == True:
            snake_points2.append([dx2, dy2])
            if score2 % 5 == 0: speed2 -= 3
            score2 += 1
            appetit2 = False

        
        for i in range(len(snake_points2)):
            if i == 0: screen.blit(self.head, snake_points2[i])
            else: screen.blit(self.body, snake_points2[i])


fx, fy = random.randrange(40, WIDTH - 60, 40), random.randrange(40, HEIGHT - 100, 40)
class Food(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('pics/food.png')
        self.x = random.randrange(40, WIDTH - 60, 40)
        self.y = random.randrange(40, HEIGHT - 100, 40)

    def spawn(self):
        global snake_points, appetit, appetit2
        screen.blit(self.image, [self.x, self.y])
        if self.x == snake_points[0][0] and self.y == snake_points[0][1]:
            appetit = True
            while [self.x, self.y] in snake_points or [self.x, self.y] in snake_points2 or [self.x, self.y] in wall:
                self.x = random.randrange(40, WIDTH - 60, 40)
                self.y = random.randrange(40, HEIGHT - 100, 40)
        if self.x == snake_points2[0][0] and self.y == snake_points2[0][1]:
            appetit2 = True
            while [self.x, self.y] in snake_points or [self.x, self.y] in snake_points2 or [self.x, self.y] in wall:
                self.x = random.randrange(40, WIDTH - 60, 40)
                self.y = random.randrange(40, HEIGHT - 100, 40)



def draw_score():
    font = pygame.font.Font('font.ttf', 70)
    screen.blit(font.render('SCORE: {}'.format(score), 0, WHITE), (20, HEIGHT - 60))
    if gamers == 2: screen.blit(font.render('SCORE 2nd: {}'.format(score2), 0, WHITE), (470, HEIGHT - 60))
        

def crush_test():
    global window
    if snake_points[0][0] < 40 or snake_points[0][0] > WIDTH - 80: window = -1
    if snake_points[0][1] < 40 or snake_points[0][1] > HEIGHT - 140: window = -1
    if snake_points2[0][0] < 40 or snake_points2[0][0] > WIDTH - 80: window = -1
    if snake_points2[0][1] < 40 or snake_points2[0][1] > HEIGHT - 140: window = -1
    if snake_points[0] in snake_points[1:]: window = -1
    if snake_points2[0] in snake_points2[1:]: window = -1
    if snake_points[0] in snake_points2: window = -1
    if snake_points2[0] in snake_points: window = -1
    if window == 2 and snake_points[0] in wall: window = -1
    if window == 2 and snake_points2[0] in wall: window = -1

def game_over():
    screen.blit(pygame.image.load('pics/gameover.png'), (0, 0))
    font = pygame.font.Font('font.ttf', 200)
    screen.blit(font.render('GAME OVER', 0, BLACK), (105, 195))
    screen.blit(font.render('GAME OVER', 0, WHITE), (100, 200))
    pygame.draw.rect(screen, WHITE, (100, 340, 520, 10))
    font = pygame.font.Font('font.ttf', 100)
    if gamers == 1:
        screen.blit(font.render('YOUR SCORE: {}'.format(score), 0, WHITE), (180 ,360))
    if gamers == 2:
        screen.blit(font.render('1st SCORE: {}'.format(score), 0, WHITE), (200 ,360))
        screen.blit(font.render('2nd SCORE: {}'.format(score2), 0, WHITE), (180 ,440))

s1 = Snake()
s2 = Snake_2()
food = Food()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if window == 0:
        intro()

    elif window == 1:
        timer += 1
        screen.blit(pygame.image.load('pics/stage_1.png'), (0, 0))
        food.spawn()
        s1.move()
        s1.draw()
        if gamers == 2:
            s2.move()
            s2.draw()
        draw_score()
        crush_test()

    elif window == 2:
        timer += 1
        screen.blit(pygame.image.load('pics/stage_2.png'), (0, 0))
        food.spawn()
        s1.move()
        s1.draw()
        if gamers == 2:
            s2.move()
            s2.draw()
        draw_score()
        crush_test()

    elif window == -1:
        game_over()

    pygame.display.update()