import sys

import pygame

class AlienInvasion:
    """клас для управления ресурсами и поведением игры"""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        # Назначает размер экрана
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        #назначаем цвет фона
        self.bg_color = (230,230,230)

    def run_game(self):
        """запуск основного цикла игры"""
        while True:
            # Отслежиавание событий клавиатуры игры.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # При каждом проходе цикла перерисовывается экран
            self.screen.fill(self.bg_color)

            # Отоброжение последнего прикосновения экрна.
            pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра и запуска игры
    ai = AlienInvasion()
    ai.run_game()