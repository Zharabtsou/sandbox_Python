import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """клас для управления ресурсами и поведением игры"""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()
        # Назвачает размеры экрана из файла настроек
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        #назначаем цвет фона
        self.bg_color = (self.settings.bg_color)

        self.ship = Ship(screen)

    def run_game(self):
        """запуск основного цикла игры"""
        while True:
            # Отслежиавание событий клавиатуры игры.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # При каждом проходе цикла перерисовывается экран
            self.screen.fill(self.bg_color)
            self.ship.blitme()

            # Отоброжение последнего прикосновения экрна.
            pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра и запуска игры
    ai = AlienInvasion()
    ai.run_game()