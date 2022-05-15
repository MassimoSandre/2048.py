import pygame
from game import Game
from button import Button
from label import Label
import json

# window sizes
size = width, height = 550,660

# window's background color
bgcolor = (249,246,219)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('2048')
clock = pygame.time.Clock()
pygame.font.init()

# The font that will be used for button's text, labels' titles and values and for the game's digits
DEFAULT_FONT = "franklingothicmedium"

# Size and position of cells and board
CELL_SIZE = 96
CELL_MARGIN = 12
GAME_POS = (width-(CELL_SIZE*4 + CELL_MARGIN*5))//2,(height-(CELL_SIZE*4 + CELL_MARGIN*5))//2

# Size and position of the new game button
BTN_POS = width//2, height-(height-(CELL_SIZE*4 + CELL_MARGIN*5))//4
BTN_WIDTH = (CELL_SIZE*4 + CELL_MARGIN*5)
BTN_HEIGHT = min((height-(CELL_SIZE*4 + CELL_MARGIN*5))//2 - 20, 100)

# Size and positions of the labels
SCORE_LABEL_POS = GAME_POS[0] + (CELL_SIZE*4 + CELL_MARGIN*5)//4, (height-(CELL_SIZE*4 + CELL_MARGIN*5))//4
BEST_SCORE_LABEL_POS = GAME_POS[0] + 3*(CELL_SIZE*4 + CELL_MARGIN*5)//4, (height-(CELL_SIZE*4 + CELL_MARGIN*5))//4
LABEL_SIZE = int((CELL_SIZE*4 + CELL_MARGIN*5)//2 * 0.9), BTN_HEIGHT

# Game, Button and Label objects
game = Game(GAME_POS,CELL_SIZE, CELL_MARGIN, DEFAULT_FONT, 50)
new_game_btn = Button(pos=BTN_POS, width=BTN_WIDTH,height=BTN_HEIGHT,onclick=game.reset,value="New Game",font=DEFAULT_FONT, font_size=40)
score_label = Label(SCORE_LABEL_POS, LABEL_SIZE, "SCORE", 0, DEFAULT_FONT,20, DEFAULT_FONT,30)
best_score_label = Label(BEST_SCORE_LABEL_POS, LABEL_SIZE, "BEST", 0, DEFAULT_FONT,20, DEFAULT_FONT,30)

try:
    # Tries to open a file, if the file does not exist 
    # or if the content is corrupted, 
    # it will just assume the current highscore is 0
    f = open("data.dat","r")
    content = json.load(f)
    f.close()
    best_score_label.set_value(content["highscore"])
except:
    best_score_label.set_value(0)


running = True
up = down = right = left = False

while running:
    screen.fill(bgcolor)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # I check if the button is being clicked
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

    if new_game_btn.is_inside(pygame.mouse.get_pos()):
        pygame.mouse.set_cursor(*pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
    else:
        pygame.mouse.set_cursor(*pygame.cursors.arrow)

    # I get the current player's score and display it in the score label
    score = game.get_score()
    score_label.set_value(score)

    # If the current score is the highscore
    # I update the best score label and the highscore in the data file
    if best_score_label.get_value() < score:
        best_score_label.set_value(score)
        f = open("data.dat","w")
        json.dump({"highscore":score},f)
        f.close()

    # I display the game, the button and the labels
    game.show(screen)
    new_game_btn.show(screen, pygame.mouse.get_pos())
    score_label.show(screen)
    best_score_label.show(screen)

    pygame.display.update()
    clock.tick(60)