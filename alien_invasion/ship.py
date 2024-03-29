import pygame


class Ship():
    '''Клас для управления кораблем'''

    def __init__(self, ai_game):
        '''Инициализирует корабль и задает его начальную позицию'''
        self.screen = ai_game.screen
        self.screen_react = ai_game.screen.get_rect()

        #Загружает изображение коробля и получает прямоугольник
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        #Каждый новый корабль появляется у нижнего края
        self.rect.midbottom = self.screen_react.midbottom


    def blitme(self):
        '''Рисует корабль в текущей позиции'''
        self.screen.blit(self.image, self.rect)