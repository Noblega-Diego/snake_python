from .serpiente import Serpiente
from .apple import Apple
import pygame
from random import Random
from .menu import Ui

class Game:
    def __init__(self):
        pygame.init()
        self.__superficie = pygame.display.set_mode((500,500))
        self.snake = Serpiente(self.__superficie,1)
        self.apple = Apple(self.__superficie)
        self.snake.draw()
        self.ui = Ui(self.__superficie)
        self.clock = pygame.time.Clock()

    def __set_manzana_random_pos(self):
        random = Random()
        pos_x = random.randint(0, 11) * 40
        pos_y = random.randint(0, 11) * 40
        self.apple.set_pos((pos_x, pos_y))
        print(self.apple.get_pos())

    def detect_colision(self):
        posSnake = self.snake.get_pos()
        posApple = self.apple.get_pos()
        if((posSnake[1] +20 < posApple[1] + 40 and posSnake[1] +20 > posApple[1]) and (posSnake[0] +20 < posApple[0] + 40 and posSnake[0] +20 > posApple[0])):
            return True
        return False

    def __draw(self):
        self.__superficie.fill((200, 200, 200))
        self.apple.draw()
        self.snake.move()
        self.snake.draw()
        self.ui.draw()
        pygame.display.update()

    def run(self):
        vandera = True
        self.__set_manzana_random_pos()
        while vandera:
            self.clock.tick(30)
            for event in pygame.event.get():
                # con type verificamos que tipo de evento se lanzo podemos tener QUIT,KEYDOWN
                if event.type == pygame.KEYDOWN:
                    # para verificar que letra se lanzo tenemos key
                    if event.key == pygame.K_ESCAPE:
                        vandera = False
                    if event.key == pygame.K_LEFT:
                        self.snake.move_left()
                    if event.key == pygame.K_RIGHT:
                        self.snake.move_rigth()
                    if event.key == pygame.K_UP:
                        self.snake.move_up()
                    if event.key == pygame.K_DOWN:
                        self.snake.move_down()
                elif event.type == pygame.QUIT:
                    vandera = False
            if (self.snake.detect_colision()):
                self.snake.reset()
                self.ui.set_puntuacio(0)
                print("colisiono con cuerpo")


            if (self.detect_colision()):
                self.snake.add__cola()
                self.__set_manzana_random_pos()
                puntuacion = self.ui.get_puntuacion()
                self.ui.set_puntuacio(puntuacion + self.apple.value)
                print("colision")

            self.__draw()