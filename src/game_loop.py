# Runs the main game loop. events actions etc.
import pygame

class Game_loop:
    def __init__(self, sudoku, renderer, clock):
        self.sudoku = sudoku
        self.renderer = renderer
        self._mouse_x = -1
        self._mouse_y = -1
        self.clock = clock

    def start(self):
        while True:
            if self._handle_events() == False:
                break

            current_time = self._clock.get_ticks()
            self._renderer.render(self._mouse_x, self._mouse_y, 0, current_time, False)

            if self.sudoku.player_board == self.sudoku.board:
                endtime = self._clock.get_ticks()
                self._renderer.render(self._mouse_x, self._mouse_y, 0, endtime, True)

            self._clock.tick(60)

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                self._mouse_x = (position[0]-20)//56
                self._mouse_y = (position[1]-60)//56
            if event.type == pygame.KEYDOWN:
                if 0 < event.key-48 < 10 and -1<self._mouse_x<9 and -1<self._mouse_y<9:
                    result = self.sudoku.make_move(self._mouse_y, self._mouse_x, event.key-48)
                    if result != 0:
                        if result == 1:
                            self._renderer.render(self._mouse_x, self._mouse_y, 1, current_time, False)
                        elif result == 2:
                            self._renderer.render(self._mouse_x, self._mouse_y, 2, current_time, False)
                        pygame.time.delay(800)
                        pygame.event.wait()