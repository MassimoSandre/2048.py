import pygame
from game import Game

size = width, height = 800,800

bgcolor = 0,0,0

screen = pygame.display.set_mode(size)
pygame.display.set_caption('2048')
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('arial',30)


game = Game((100,100),64, 8, font)

running = True

up = down = right = left = False

while running:
    screen.fill(bgcolor)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not up:
                game.make_move("up")
            elif event.key == pygame.K_RIGHT and not right:
                game.make_move("right")
            elif event.key == pygame.K_DOWN and not down:
                game.make_move("down")
            elif event.key == pygame.K_LEFT and not left:    
                game.make_move("left")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
            elif event.key == pygame.K_RIGHT:
                right = False
            elif event.key == pygame.K_DOWN:
                down = False
            elif event.key == pygame.K_LEFT:
                left = False

    if game.check_game_over():
        print("Game over")

    game.show(screen)
    pygame.display.update()
    clock.tick(60)