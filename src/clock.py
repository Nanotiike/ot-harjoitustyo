import pygame

class Clock:
    # Handles the timer for the game
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        self._clock.tick(fps)

    def get_ticks(self):
        return pygame.time.get_ticks()
