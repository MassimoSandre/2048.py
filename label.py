from matplotlib.pyplot import title
import pygame

class Label:
    def __init__(self, pos, size, title, value, title_font, title_font_size, value_font, value_font_size) -> None:
        self.__posx, self.__posy = pos
        self.__width,self.__height = size
        self.__title = title
        self.__value = value

        pygame.font.init()
        self.__title_font = pygame.font.SysFont(title_font,title_font_size)
        self.__value_font = pygame.font.SysFont(value_font,value_font_size)
    
    def set_value(self, new_value):
        self.__value = new_value

    def get_value(self):
        return self.__value

    def show(self, screen):
        fx,fy = self.__posx - self.__width//2, self.__posy - self.__height//2
    
        pygame.draw.rect(screen, (187,173,160), pygame.Rect((fx,fy), (self.__width, self.__height)), 0, 4)        

        
        title_surface = self.__title_font.render(str(self.__title), False,(238,223,199))
        value_surface = self.__value_font.render(str(self.__value), False,(255,255,255))

        dx1 = title_surface.get_rect().width//2
        dy1 = title_surface.get_rect().height//2
        
        dx2 = value_surface.get_rect().width//2
        dy2 = value_surface.get_rect().height//2
        

        screen.blit(title_surface, (self.__posx-dx1, self.__posy-dy1 -self.__height//5))
        screen.blit(value_surface, (self.__posx-dx2, self.__posy-dy2 +self.__height//5))