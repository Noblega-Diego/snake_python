from pygame.font import SysFont
from pygame import Surface
from pygame.event import Event
import pygame
class Ui:

    def __init__(self, superficie:Surface):
        self.__puntuacion = 0
        self.font = SysFont("Ubuntu", 20)
        self.__textpygame = self.font.render("Score: {}".format(self.__puntuacion), False,(0,0,0))
        self.__superficie = superficie;

    def draw(self):
        self.__superficie.blit(self.__textpygame, (20, self.__superficie.get_height() - 30))

    def set_puntuacio(self, puntuacion):
        self.__puntuacion = puntuacion
        self.__textpygame = self.font.render("Score: {}".format(self.__puntuacion), False,(0,0,0))

    def get_puntuacion(self):
        return self.__puntuacion

class Menu:

    def __init__(self, superficie:Surface):
        self.font = SysFont("Ubuntu", 20)

    def detectEvet(self,event:Event):
        print(event.type)
