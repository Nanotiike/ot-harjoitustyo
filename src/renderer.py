# Draws the screen and all that are in it. handles changes to the screen
import pygame

class Renderer:
    def __init__(self, screen, font, sudoku):
        self.screen = screen
        self.font = font
        self.sudoku = sudoku

    def render_backround(self, x, y):
        self.screen.fill((212, 235, 242))
        pygame.draw.rect(self.screen, (255, 255, 255), (20, 60, 504, 504))
        if -1<x<9 and -1<y<9:
            pygame.draw.rect(self.screen, (190, 190, 190), (20+x*56, 60+y*56, 56, 56))
        pygame.draw.rect(self.screen, (0, 0, 0), (20, 60, 504, 504), 3)
        i = 1
        while (i*56)<504:
            line_width = 3 if i%3 > 0 else 7
            pygame.draw.line(self.screen, (0, 0, 0), (20+i*56, 60), (20+i*56, 564), line_width)
            pygame.draw.line(self.screen, (0, 0, 0), (20, 60+i*56), (524, 60+i*56), line_width)
            i+=1
        pygame.draw.rect(self.screen, (255, 255, 255), (20, 574, 504, 70))
        pygame.draw.rect(self.screen, (0, 0, 0), (20, 574, 504, 70), 3)

    def render_writing(self):
        font = pygame.font.SysFont(self.font, 30)
        for i in range(9):
            for j in range(9):
                if self.sudoku.player_board[i][j] != 0:
                    text = font.render(str(self.sudoku.player_board[i][j]), True, (0, 0, 0))
                    self.screen.blit(text, (20+j*56+20, 60+i*56+12))
        text = font.render("Mistakes: "+str(self.sudoku.mistakes), True, (0, 0, 0))
        self.screen.blit(text, (200, 10))
        font = pygame.font.SysFont(self.font, 20)
        text = font.render("Press your mouse key on a square to select it and then", True, (0, 0, 0))
        self.screen.blit(text, (25, 579))
        text = font.render("press a number from 1 to 9 to enter a number.", True, (0, 0, 0))
        self.screen.blit(text, (25, 604))

    def render_wrong_number(self):
        font = pygame.font.SysFont(self.font, 20)
        pygame.draw.rect(self.screen, (255, 255, 255), (172, 287, 200, 50))
        pygame.draw.rect(self.screen, (0, 0, 0), (172, 287, 200, 50), 3)
        text = font.render("Wrong number!", True, (0, 0, 0))
        self.screen.blit(text, (202, 299))

    def render_already_filled(self):
        font = pygame.font.SysFont(self.font, 20)
        pygame.draw.rect(self.screen, (255, 255, 255), (97, 287, 350, 50))
        pygame.draw.rect(self.screen, (0, 0, 0), (97, 287, 350, 50), 3)
        text = font.render("That square already has a number!", True, (0, 0, 0))
        self.screen.blit(text, (117, 299))

    def render_win_screen(self, time):
        pygame.draw.rect(self.screen, (255, 255, 255), (97, 212, 350, 200))
        pygame.draw.rect(self.screen, (0, 0, 0), (97, 212, 350, 200), 3)
        font = pygame.font.SysFont(self.font, 70)
        text = font.render("You Win!", True, (0, 0, 0))
        self.screen.blit(text, (132, 224))
        font = pygame.font.SysFont(self.font, 20)
        text = font.render("Time: "+str(round(time, 2))+"s", True, (0, 0, 0))
        self.screen.blit(text, (227, 324))
        text = font.render("Mistakes: "+str(self.sudoku.mistakes), True, (0, 0, 0))
        self.screen.blit(text, (227, 349))
        pygame.display.flip()

    def render(self, x, y, input, time, win):  
        self.render_backround(x, y)
        self.render_writing()
        if input == 1:
            self.render_wrong_number()
        elif input == 2:
            self.render_already_filled()
        if win == True:
            self.render_win_screen(time)
        pygame.display.flip()
        