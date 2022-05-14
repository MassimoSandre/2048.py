import pygame
from game import Game
from button import Button

size = width, height = 550,660

bgcolor = (249,246,219)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('2048')
clock = pygame.time.Clock()
pygame.font.init()
digits_font = pygame.font.SysFont("franklingothicmedium",50)
btn_font = pygame.font.SysFont("franklingothicmedium",40)


CELL_SIZE = 96
CELL_MARGIN = 12
GAME_POS = (width-(CELL_SIZE*4 + CELL_MARGIN*5))//2,(height-(CELL_SIZE*4 + CELL_MARGIN*5))//2

BTN_POS = width//2, height-(height-(CELL_SIZE*4 + CELL_MARGIN*5))//4
BTN_WIDTH = (CELL_SIZE*4 + CELL_MARGIN*5)
BTN_HEIGHT = min((height-(CELL_SIZE*4 + CELL_MARGIN*5))//2 - 20, 100)

game = Game(GAME_POS,CELL_SIZE, CELL_MARGIN, digits_font)
new_game_btn = Button(pos=BTN_POS, width=BTN_WIDTH,height=BTN_HEIGHT,onclick=game.reset,value="New Game",font=btn_font)

running = True

up = down = right = left = False

while running:
    screen.fill(bgcolor)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if new_game_btn.is_inside(event.pos):
                    new_game_btn.click()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not up:
                game.make_move("up")
            elif event.key == pygame.K_RIGHT and not right:
                game.make_move("right")
            elif event.key == pygame.K_DOWN and not down:
                game.make_move("down")
            elif event.key == pygame.K_LEFT and not left:    
                game.make_move("left")

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
            elif event.key == pygame.K_RIGHT:
                right = False
            elif event.key == pygame.K_DOWN:
                down = False
            elif event.key == pygame.K_LEFT:
                left = False


    game.show(screen)
    new_game_btn.show(screen, pygame.mouse.get_pos())
    pygame.display.update()
    clock.tick(60)