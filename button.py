""" 
Button module

The Button class allows to create, draw and handle buttons 

    Usage example:

    button = Button(pos=pos,width=width,height=height)
    button.show(screen, mousepos)
"""

import pygame

class Button:
    """
    A class designed to solve standard sudoku

    Attributes:
        __pos: A tuple of 2 integers, representing the absolute position (in pixel) of the center of the button
        __width: An integer, representing the width of the button
        __height: An integer, representing the height of the butotn
        __onclick: A function that will be called when the button is clicked
        disabled: A boolean, representing if the button is disabled or not
        __value: A string that will be displayed on the button
        __font: A pygame font used to write the string displayed on the button
        __over_time: An integer, representing the amount of time the mouse cursor has been over the button
    """

    def __init__(self,*, pos, width:int, height:int, onclick=None, disabled:bool=False, value:str="",  font:pygame.font.Font=None) -> None:
        """
        Inits Button

        Args:
            pos: A tuple of 2 integers, representing the absolute position (in pixel) of the center of the button
            width: An integer, representing the width of the button
            height: An integer, representing the height of the butotn
            onclick: A function that will be called when the button is clicked
            disabled: A boolean, representing if the button is disabled or not
            value: A string that will be displayed on the button
            font: A pygame font used to write the string displayed on the button
        """
        self.__pos = pos
        self.__width = width
        self.__height = height
        self.__onclick = onclick
        self.disabled = disabled
        
        self.__value = value
        self.__font = font

        self.__over_time = 0
    
    def is_inside(self, pos) -> bool:
        """
        Checks whether an absolute position lays inside the button

        Args:
            pos: A tuple of 2 integers, representing an absolute position

        Returns:
            True if the position pos lays inside the button, False if not    
        """
        fx,fy = self.__pos[0] - self.__width//2, self.__pos[1] - self.__height//2
        tx,ty = pos
        if tx < fx:
            return False
        if tx > fx + self.__width:
            return False
        if ty < fy:
            return False
        if ty > fy + self.__height:
            return False

        return True


    def enable(self) -> None:
        """
        Enables the button

        set the attribute disabled to False
        """
        self.disabled = False

    def disable(self) -> None:
        """
        Disables the button

        set the attribute disabled to True
        """
        self.disabled = True

    def click(self) -> None:
        """
        Call the onclick function of the button
        """
        self.__onclick()

    def show(self, screen:pygame.Surface, mousepos) -> None:
        """
        Shows the button

        Args:
            screen: The pygame surface where the button will be drawn
            mousepos: A tuple of 2 integers representing the absolute position of the mouse
        """
        fx,fy = self.__pos[0] - self.__width//2, self.__pos[1] - self.__height//2

        if self.disabled:
            pygame.draw.rect(screen, (100,100,100), pygame.Rect((fx,fy), (self.__width, self.__height)), 0, 4)
        else:
            
            pygame.draw.rect(screen, (max(100, 143-self.__over_time),max(100, 122-self.__over_time),max(100, 102-self.__over_time)), pygame.Rect((fx,fy), (self.__width, self.__height)), 0, 4)

            if self.is_inside(mousepos):
                self.__over_time = min(16, self.__over_time+2)
            else:
                self.__over_time = max(0, self.__over_time-2)

        if self.__value != "" and self.__font != None:
            text_surface = self.__font.render(str(self.__value), False,(249,246,219))

            dx = text_surface.get_rect().width//2
            dy = text_surface.get_rect().height//2

            screen.blit(text_surface, (self.__pos[0]-dx, self.__pos[1]-dy))