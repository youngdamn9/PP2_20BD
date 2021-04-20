import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Paint')

SIZE = 3
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

background = pygame.Surface((800, 600))
background = background.convert()
background.fill(WHITE)

color = (0, 0, 0)
start_pos = (0, 0)
font = pygame.font.Font('font.ttf', 40)


menu_ = True
plus = False
minus = False
rect_ = False
ellipse_ = False
while True:
    while menu_:
        for i in pygame.event.get():
            mainScreenPressed = pygame.key.get_pressed()
            if i.type == QUIT or mainScreenPressed[K_q]:
                exit()
            screen.fill(BLACK)

            font = pygame.font.Font('font.ttf', 70)
            screen.blit(font.render("1 - Black color", 0, WHITE), (80, 120))
            screen.blit(font.render("2 - Red color", 0, WHITE), (80, 160))
            screen.blit(font.render("3 - Green color", 0, WHITE), (80, 200))
            screen.blit(font.render("4 - Blue color", 0, WHITE), (80, 240))
            screen.blit(font.render("5 - Yellow color", 0, WHITE), (80, 280))
            screen.blit(font.render("E - Eraser", 0, WHITE), (400, 120))
            screen.blit(font.render("R - Rectangle", 0, WHITE), (400, 160))
            screen.blit(font.render("O - Ellipse", 0, WHITE), (400, 200))
            screen.blit(font.render("S - Save Image", 0, WHITE), (400, 240))
            screen.blit(font.render("L - Load Image", 0, WHITE), (400, 280))
            screen.blit(font.render("Tap to SPACE for drawing", 0, WHITE), (170, 520))
            pygame.display.flip()
            if mainScreenPressed[K_SPACE]:
                menu_ = False
                font = pygame.font.Font('font.ttf', 40)

    key = pygame.key.get_pressed()
    if key[K_1]: color = BLACK
    elif key[K_2]: color = RED
    elif key[K_3]: color = GREEN
    elif key[K_4]: color = BLUE
    elif key[K_5]: color = YELLOW
    elif key[K_e]:
        color = WHITE
    elif key[K_LSHIFT]:
        color = BLACK
        menu_ = True
    elif key[K_s]:
        pygame.image.save(background, 'image.png')
    elif key[K_l]:
        background = pygame.image.load('image.png')
        color = BLACK
    elif key[K_z]:
        rect_ = False
        ellipse_ = False
    if plus:
        SIZE += 1
        plus = False
    if minus:
        if SIZE != 1: SIZE -= 1
        minus = False
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == pygame.MOUSEMOTION:
            end_pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if not rect_ and not ellipse_:
                    pygame.draw.line(background, color, start_pos, end_pos, SIZE)
            start_pos = end_pos
        if event.type == pygame.MOUSEBUTTONDOWN and (rect_ or ellipse_):
            last_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP and rect_:
            pos = pygame.mouse.get_pos()
            pygame.draw.rect(background, color, (last_pos[0], last_pos[1], pos[0] - last_pos[0], pos[1] - last_pos[1]))

        if event.type == pygame.MOUSEBUTTONUP and ellipse_:
            pos = pygame.mouse.get_pos()
            pygame.draw.ellipse(background, color, (last_pos[0], last_pos[1], pos[0] - last_pos[0], pos[1] - last_pos[1]))

        if event.type == pygame.KEYDOWN and event.key == K_UP: plus = True
        if event.type == pygame.KEYDOWN and event.key == K_DOWN: minus = True
        if event.type == pygame.KEYDOWN and event.key == K_r: rect_, ellipse_ = True, False
        if event.type == pygame.KEYDOWN and event.key == K_o: rect_, ellipse_ = False, True

    screen.blit(background, (0, 0))
    screen.blit(font.render("Tap to SHIFT to see painting options", 0, BLACK), (10, 560))
    if color == WHITE:
        screen.blit(font.render("Using ERASER", 0, BLACK), (520, 560))
    else:
        screen.blit(font.render("Color :", 0, BLACK), (520, 560))
        pygame.draw.rect(screen, color, (600, 570, 60, 20))

    pygame.display.flip()