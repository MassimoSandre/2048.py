""" 
Label module

The Label class allows to create, draw and handle labels.
Each label has as a static title and a dinamic content (value) 

    Usage example:

    label = Label(pos, size, title, value, title_font, title_font_size, value_font, value_font_size)
    label.set_value(new_value)
    label.show(surface)
"""

import pygame

class Label:
    """
    A class designed to display labels

    Attributes:
        __posx: An integer, representing the absolute position (in pixel) on the x-axis of the center of the label
        __posy: An integer, representing the absolute position (in pixel) on the y-axis of the center of the label
        __width: An integer, representing the width of the label
        __height: An integer, representing the height of the label
        __title: A string that will be displayed as title in the label
        __value: A string that will be displayed as content in the label
        __title_font: A pygame font used to write the title string displayed on the label
        __value_font: A pygame font used to write the content string displayed on the label
    """
    def __init__(self, pos:tuple, size:tuple, title:str, value:str, title_font:str, title_font_size:int, value_font:str, value_font_size:int) -> None:
        """
        Inits Label

        Args:
            pos: A tuple of 2 integers, representing the absolute position (in pixel) of the center of the label
            size: A tuple of 2 integers, representing the size (in pixel) of the label
            title: A string that will be displayed as title in the label
            value: A string that will be displayed as content in the label
            title_font: A string representing a valid pygame font used to write the title string displayed on the label
            title_font_size: An integer representing the font size for the title
            value_font: A string representing a valid pygame font used to write the content string displayed on the label
            value_font_size: An integer representing the font size for the content
        """
        self.__posx, self.__posy = pos
        self.__width,self.__height = size
        self.__title = title
        self.__value = value

        pygame.font.init()
        self.__title_font = pygame.font.SysFont(title_font,title_font_size)
        self.__value_font = pygame.font.SysFont(value_font,value_font_size)
    
    def set_value(self, new_value:str) -> None:
        """
        Sets the content's value

        Args:
            new_value: A string that will be displayed as content in the label
        """
        self.__value = new_value

    def get_value(self) -> str:
        """
        Returns the current content's value

        Returns:
            The current content's value
        """
        return self.__value

    def show(self, screen:pygame.Surface) -> None:
        """
        Shows the label

        Args:
            screen: The pygame surface where the button will be drawn
        """

        # I calculate the position of the top left corner of the label
        fx,fy = self.__posx - self.__width//2, self.__posy - self.__height//2
    
        pygame.draw.rect(screen, (187,173,160), pygame.Rect((fx,fy), (self.__width, self.__height)), 0, 4)        

        # I create and display the surfaces for title and value of the label
        title_surface = self.__title_font.render(str(self.__title), False,(238,223,199))
        value_surface = self.__value_font.render(str(self.__value), False,(255,255,255))

        dx1 = title_surface.get_rect().width//2
        dy1 = title_surface.get_rect().height//2
        
        dx2 = value_surface.get_rect().width//2
        dy2 = value_surface.get_rect().height//2
        
        screen.blit(title_surface, (self.__posx-dx1, self.__posy-dy1 -self.__height//5))
        screen.blit(value_surface, (self.__posx-dx2, self.__posy-dy2 +self.__height//5))