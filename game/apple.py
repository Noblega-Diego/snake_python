import pygame
from pygame import Surface
class Apple:
    def __init__(self, superficie:Surface, pos:tuple= (0,0)):
        self.__superficie = superficie
        self.__x = pos[0]
        self.__y = pos[0]
        self.block = pygame.image.load("resources/apple.jpg")
        self.value = 100

    def draw(self):
        self.__superficie.blit(self.block,(self.__x, self.__y))

    def set_pos(self,pos:tuple):
        self.__x = pos[0]
        self.__y = pos[1]

    def get_pos(self):
        return (self.__x,self.__y)

