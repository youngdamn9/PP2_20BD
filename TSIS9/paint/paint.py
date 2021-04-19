import pygame

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Paint')
font = pygame.font.Font('font.ttf', 60)


RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
color = (0, 0, 0)

last_pos = (0, 0)
drawing = False
size = 5

def menu():
    key = pygame.key.get_pressed()
    

def Line(screen, start, end, size, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), size)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), size)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
            if event.key == pygame.K_b:
                color = BLUE
            if event.key == pygame.K_g:
                color = GREEN
            if event.key == pygame.K_UP:
                size += 1
            if event.key == pygame.K_DOWN:
                size -= 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, color, event.pos, size)
            drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                Line(screen, last_pos, event.pos, size, color)
            last_pos = event.pos
    pygame.display.flip()
