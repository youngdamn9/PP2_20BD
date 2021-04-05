import pygame
import math
pygame.init()

width, height = 600, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('sin & cos')

white, black = (255, 255, 255), (0, 0, 0)
red, blue = (255, 0, 0), (0, 0, 255)

font = pygame.font.SysFont('bookantiqua', 12)

nums = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']
radians = ['-3π', ' 5π', '-2π', '-3π', '-π', '-π', '  0', ' π', '  π', '3π', '2π', '5π', '3π']

run = True
while run:
    screen.fill(white)
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
    
    pygame.draw.rect(screen, black, pygame.Rect(40, 40, width - 80, height - 120), 2)
    pygame.draw.line(screen, black, (300, 40), (300, height - 80), 2)
    pygame.draw.line(screen, black, (40, 220), (width - 40, 220), 2)
    for step in range(60, 600, 80):
        pygame.draw.line(screen, black, (step, 40), (step, height - 80))
    for step in range(60, 400, 40):
        pygame.draw.line(screen, black, (40, step), (width - 40, step))
    for step in range(60, 541, 10):
        pygame.draw.line(screen, black, (step, 40), (step, 45))
        pygame.draw.line(screen, black, (step, height - 85), (step, height - 80))
        if (step - 20) % 20 == 0:
            pygame.draw.line(screen, black, (step, 40), (step, 50))
            pygame.draw.line(screen, black, (step, height - 90), (step, height - 80))
        if (step - 20) % 40 == 0:
            pygame.draw.line(screen, black, (step, 40), (step, 55))
            pygame.draw.line(screen, black, (step, height - 95), (step, height - 80))
    for step in range(60, 381, 10):
        pygame.draw.line(screen, black, (40, step), (45, step))
        pygame.draw.line(screen, black, (width - 45, step), (width - 40, step))
        if (step - 20) % 20 == 0:
            pygame.draw.line(screen, black, (40, step), (50, step))
            pygame.draw.line(screen, black, (width - 50, step), (width - 40, step))
    pygame.draw.line(screen, white, (380, 61), (380, 99))

    y = 52
    for i in nums:
        screen.blit(font.render(i, 1, black), (10, y))
        y += 40
    x = 50
    for i in range(len(radians)):
        if i % 2 == 0:
            screen.blit(font.render(radians[i], 1, black), (x, height - 78))
        else:
            screen.blit(font.render(radians[i], 1, black), (x, height - 80))
            pygame.draw.line(screen, black, (x, height - 65), (x + 15, height - 65))
            screen.blit(font.render('2', 1, black), (x + 5, height - 65))
        x += 40

    font = pygame.font.SysFont('bookantiqua', 18)
    screen.blit(font.render('sin x', 1, black), (360, 60))
    screen.blit(font.render('cos x', 1, black), (360, 75))
    screen.blit(font.render('X', 1, black), (295, 430))
    pygame.draw.line(screen, red, (410, 72), (435, 72), 2)
    for i in range(410, 435, 9): pygame.draw.line(screen, blue, (i, 87), (i + 7, 87), 2)
    font = pygame.font.SysFont('bookantiqua', 12)

    points_sin, points_cos, n = [], [], 6
    for x in range(0, 481):
        y = int(math.sin(float(x) / 480 * n * math.pi) * 160 + 220)
        points_sin.append((x  + 60, y))
    for x in range(0, 481):
        y = int(math.cos(float(x) / 480 * n * math.pi) * 160 + 220)
        points_cos.append((x  + 60, y))
    pygame.draw.aalines(screen, red, 0, points_sin)
    for i in range(0, len(points_cos) - 1, 2):
        pygame.draw.aaline(screen, blue, points_cos[i], points_cos[i + 1])

    pygame.display.flip()