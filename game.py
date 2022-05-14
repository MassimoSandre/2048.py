import random
import pygame


class Game:
    def __init__(self, position, cell_size, margin, font) -> None:
        self.__pos = position
        self.__cell_size = cell_size
        self.__margin = margin
        self.__font = font
        
        self.reset()

    def reset(self):
        self.__score = 0

        self.__board = [[0 for _ in range(4)] for _ in range(4)]

        self.__animating = 0
        self.__animation_time = 6
        self.__animation_info = []

        self.__spawning = []
        self.__spawning_time = 6

        self.__time_since_game_over = 0

        p1 = (random.randint(0,3),random.randint(0,3))
        p2 = (random.randint(0,3),random.randint(0,3))
        while p1 == p2:
            p2 = (random.randint(0,3),random.randint(0,3))
        i,j = p1
        self.__board[i][j] = 2
        i,j = p2
        self.__board[i][j] = 2


    def make_move(self, move):
        if not self.is_legal_move(move):
            return
        self.__animation_info = []
        self.__animating = self.__animation_time
        if move == "up":
            for j in range(4):
                last_valid = 0
                for i in range(4):
                    if self.__board[i][j] != 0:
                        if i != last_valid:
                            if self.__board[last_valid][j] == 0:
                                self.__animation_info.append(((i,j),(last_valid,j), self.__board[i][j]))
                                self.__board[last_valid][j] = self.__board[i][j]
                                self.__board[i][j] = 0
                                
                            elif self.__board[last_valid][j] == self.__board[i][j]:
                                self.__animation_info.append(((i,j),(last_valid,j), self.__board[i][j]))
                                self.__spawning.append((last_valid,j,0))
                                self.__board[last_valid][j] *= 2
                                self.__score += self.__board[last_valid][j]
                                
                                last_valid +=1
                                self.__board[i][j] = 0
                            else:
                                last_valid +=1
                                self.__animation_info.append(((i,j),(last_valid,j), self.__board[i][j]))
                                
                                self.__board[last_valid][j], self.__board[i][j] = self.__board[i][j], self.__board[last_valid][j]

                        else:
                            self.__animation_info.append(((i,j),(i,j), self.__board[i][j]))

        elif move == "right":
            for i in range(4):
                last_valid = 0
                for j in range(4):
                    if self.__board[i][3-j] != 0:
                        if j != last_valid:
                            if self.__board[i][3-last_valid] == 0:
                                self.__animation_info.append(((i,3-j),(i,3-last_valid), self.__board[i][3-j]))
                                self.__board[i][3-last_valid] = self.__board[i][3-j]
                                self.__board[i][3-j] = 0
                                
                            elif self.__board[i][3-last_valid] == self.__board[i][3-j]:
                                self.__animation_info.append(((i,3-j),(i,3-last_valid), self.__board[i][3-j]))
                                self.__spawning.append((i,3-last_valid,0))
                                self.__board[i][3-last_valid] *= 2
                                self.__score += self.__board[i][3-last_valid] 
                                
                                last_valid +=1
                                self.__board[i][3-j] = 0
                            else:
                                last_valid +=1
                                self.__animation_info.append(((i,3-j),(i,3-last_valid), self.__board[i][3-j]))
                                self.__board[i][3-last_valid], self.__board[i][3-j] = self.__board[i][3-j], self.__board[i][3-last_valid]

                        else:
                            self.__animation_info.append(((i,3-j),(i,3-j), self.__board[i][3-j]))

        elif move == "down":
            for j in range(4):
                last_valid = 0
                for i in range(4):
                    if self.__board[3-i][j] != 0:
                        if i != last_valid:
                            if self.__board[3-last_valid][j] == 0:
                                self.__board[3-last_valid][j] = self.__board[3-i][j]
                                self.__animation_info.append(((3-i,j),(3-last_valid,j), self.__board[3-i][j]))
                                self.__board[3-i][j] = 0
                                
                            elif self.__board[3-last_valid][j] == self.__board[3-i][j]:
                                self.__animation_info.append(((3-i,j),(3-last_valid,j), self.__board[3-i][j]))
                                self.__spawning.append((3-last_valid,j,0))
                                self.__board[3-last_valid][j] *= 2
                                self.__score += self.__board[3-last_valid][j] 
                                
                                last_valid +=1
                                self.__board[3-i][j] = 0
                            else:
                                last_valid +=1
                                self.__animation_info.append(((3-i,j),(3-last_valid,j), self.__board[3-i][j]))
                                self.__board[3-last_valid][j], self.__board[3-i][j] = self.__board[3-i][j], self.__board[3-last_valid][j]
                        
                        else:
                            self.__animation_info.append(((3-i,j),(3-i,j), self.__board[3-i][j]))
                    
        elif move == "left":
            for i in range(4):
                last_valid = 0
                for j in range(4):
                    if self.__board[i][j] != 0:
                        if j != last_valid:
                            if self.__board[i][last_valid] == 0:
                                self.__animation_info.append(((i,j),(i,last_valid), self.__board[i][j]))
                                self.__board[i][last_valid] = self.__board[i][j]
                                self.__board[i][j] = 0
                                
                            elif self.__board[i][last_valid] == self.__board[i][j]:
                                self.__animation_info.append(((i,j),(i,last_valid), self.__board[i][j]))
                                self.__spawning.append((i,last_valid,0))
                                self.__board[i][last_valid] *= 2
                                self.__score += self.__board[i][last_valid]
                                
                                last_valid +=1
                                self.__board[i][j] = 0
                            else:
                                last_valid +=1
                                self.__animation_info.append(((i,j),(i,last_valid), self.__board[i][j]))
                                self.__board[i][last_valid], self.__board[i][j] = self.__board[i][j], self.__board[i][last_valid]

                        else:
                            self.__animation_info.append(((i,j),(i,j), self.__board[i][j]))


        self.__next_turn()

    def __next_turn(self):
        free_cells = []
        for i in range(4):
            for j in range(4):
                if self.__board[i][j] == 0:
                    free_cells.append((i,j))

        if free_cells != []:
            i,j = random.choice(free_cells)
            self.__board[i][j] = 2
            self.__spawning.append((i,j,0))
            

    def is_legal_move(self, move):
        if move == "up":
            for j in range(4):
                i = 0
                gap = False
                while i < 4:
                    if self.__board[i][j] == 0:
                        gap = True
                    elif gap:
                        return True
                    if i < 3:
                        if self.__board[i][j] == self.__board[i+1][j]:
                            return True
                    i+=1

        elif move == "right":
            for j in range(4):
                i = 0
                gap = False
                while i < 4:
                    if self.__board[j][3-i] == 0:
                        gap = True
                    elif gap:
                        return True
                    if i < 3:
                        if self.__board[j][3-i] == self.__board[j][3-(i+1)]:
                            return True
                    i+=1

        elif move == "down":
            for j in range(4):
                i = 0
                gap = False
                while i < 4:
                    if self.__board[3-i][j] == 0:
                        gap = True
                    elif gap:
                        return True
                    if i < 3:
                        if self.__board[3-i][j] == self.__board[3-(i+1)][j]:
                            return True
                    i+=1
            
        elif move == "left":
            for j in range(4):
                i = 0
                gap = False
                while i < 4:
                    if self.__board[j][i] == 0:
                        gap = True
                    elif gap:
                        return True
                    if i < 3:
                        if self.__board[j][i] == self.__board[j][i+1]:
                            return True
                    i+=1
            

        return False

    def check_game_over(self):
        if self.is_legal_move("up"):
            return False
        if self.is_legal_move("right"):
            return False
        if self.is_legal_move("down"):
            return False
        if self.is_legal_move("left"):
            return False
        return True

    def get_score(self):
        return self.__score

    def show(self, screen):
        color = {
            0: (205,193,180),
            2: (238,228,218),
            4: (238,225,201),
            8: (243,178,122),
            16: (246,150,100),
            32: (247,124,95),
            64: (247,95,59),
            128: (237,208,115),
            256: (237,204,98),
            512: (237,200,80),
            1024: (237,197,63),
            2048: (237,194,46),
            4096: (60,58,50),
            8192: (60,58,50),
            16384: (60,58,50),
            32768: (60,58,50),
            65536: (60,58,50),
            65536: (60,58,50)
        }
        pygame.draw.rect(screen, (187,173,160), pygame.Rect(self.__pos, [self.__margin*5 + self.__cell_size*4]*2),0,5)

        if not self.__animating:
            for i in range(4):
                for j in range(4):
                    if self.__board[i][j] != 0:

                        is_spawning = False
                        for e in self.__spawning:
                            ti,tj,tt = e
                            if (ti,tj) == (i,j):
                                is_spawning = True
                                break
                        
                        if not is_spawning:
                            pygame.draw.rect(screen, color[self.__board[i][j]], pygame.Rect((self.__pos[0]+self.__margin*(j+1)+self.__cell_size*j, self.__pos[1]+self.__margin*(i+1)+self.__cell_size*i),[self.__cell_size]*2),0,3)
                        else:
                            ds = 0.4/self.__spawning_time * tt
                            
                            actual_cell_size = (ds+0.7)*self.__cell_size
                            actual_cell_size = int(actual_cell_size)
                            delta = (actual_cell_size-self.__cell_size)//2
                            pygame.draw.rect(screen, color[self.__board[i][j]], pygame.Rect((self.__pos[0]+self.__margin*(j+1)+self.__cell_size*j -delta, self.__pos[1]+self.__margin*(i+1)+self.__cell_size*i - delta),[actual_cell_size]*2),0,3)

                            if tt == self.__spawning_time:
                                self.__spawning.remove((i,j,tt))
                            else:
                                self.__spawning[self.__spawning.index((i,j,tt))] = (i,j,tt+1)
                                

                        text_color = (119,110,101)
                        if self.__board[i][j] > 4:
                            text_color = (249,246,242)
                        
                        cx,cy=(self.__pos[0]+self.__margin*(j+1)+self.__cell_size*j, self.__pos[1]+self.__margin*(i+1)+self.__cell_size*i)
                        cx += self.__cell_size//2
                        cy += self.__cell_size//2

                        text_surface = self.__font.render(str(self.__board[i][j]),False,text_color)

                        r = text_surface.get_rect()

                        dx = r.width//2
                        dy = r.height//2

                        screen.blit(text_surface, (cx-dx,cy-dy))
                    else:
                        pygame.draw.rect(screen, color[0], pygame.Rect((self.__pos[0]+self.__margin*(j+1)+self.__cell_size*j, self.__pos[1]+self.__margin*(i+1)+self.__cell_size*i),[self.__cell_size]*2),0,3)

        else:
            for i in range(4):
                for j in range(4):
                    pygame.draw.rect(screen, color[0], pygame.Rect((self.__pos[0]+self.__margin*(j+1)+self.__cell_size*j, self.__pos[1]+self.__margin*(i+1)+self.__cell_size*i),[self.__cell_size]*2),0,3)
            for info in self.__animation_info:

                
                p1,p2,v = info
                i1,j1 = p1
                i2,j2 = p2
                
                cx1,cy1 = self.__margin*(j1+1) + self.__cell_size*j1, self.__margin*(i1+1) + self.__cell_size*i1
                cx2,cy2 = self.__margin*(j2+1) + self.__cell_size*j2, self.__margin*(i2+1) + self.__cell_size*i2

                dx,dy = cx1-cx2, cy1-cy2

                ax,ay = self.__pos
                ax+=cx2
                ay+=cy2
                ax+=int(dx*(self.__animating/self.__animation_time))
                ay+=int(dy*(self.__animating/self.__animation_time))

                pygame.draw.rect(screen, color[v], pygame.Rect((ax,ay),[self.__cell_size]*2),0,3)

                ax += self.__cell_size//2
                ay += self.__cell_size//2

                text_color = (119,110,101)
                if v > 4:
                    text_color = (249,246,242)

                text_surface = self.__font.render(str(v),False,text_color)

                r = text_surface.get_rect()

                dx = r.width//2
                dy = r.height//2

                screen.blit(text_surface, (ax-dx,ay-dy))
                
            self.__animating -=1

        if self.check_game_over():
            image = pygame.Surface([self.__margin*5 + self.__cell_size*4]*2, pygame.SRCALPHA,32)
            pygame.draw.rect(image, (187,173,160),pygame.Rect((0,0), [self.__margin*5 + self.__cell_size*4]*2),0,5)
            image = image.convert_alpha()
            image.set_alpha(min(self.__time_since_game_over,150))
            screen.blit(image,self.__pos)

            text_surface = self.__font.render(str("Game over!"), False,(119,111,102))
            text_surface = text_surface.convert_alpha()
            text_surface.set_alpha(min(255,self.__time_since_game_over))
            dx = text_surface.get_rect().width//2
            dy = text_surface.get_rect().height//2

            screen.blit(text_surface, (self.__pos[0] + (self.__cell_size*2+ 5/2*self.__margin) -dx, self.__pos[1]+(self.__cell_size*2+ 5/2*self.__margin)-dy))

            if self.__time_since_game_over < 255:
                self.__time_since_game_over += 5

        
        

        