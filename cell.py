import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        # stores original value of cell
        self.original_value = value
        # sets displayed value of cell
        self.value = value
        # sets what row cell is in (Horizontal)
        self.row = row
        # sets what column cell is in (Vertical)
        self.col = col
        # screen variable from PyGame
        self.screen = screen
        # sets sketch value as None
        self.sketch_value = 0

    # method to set displayed value of cell
    def set_cell_value(self, value):
        self.value = value

    # method to set the sketch value
    def set_sketched_value(self, value):
        self.sketch_value = value
    """
    # method to draw cell
    def draw(self):
        if self.value != 0:
            font = pygame.font.Font('fonts/gilgan.ttf', 25)
            text = font.render(str(self.value), True, (105, 105, 105))
            self.screen.blit(text, ((self.row * 80) + 32, (self.col * 80) + 30))
        elif 9 >= self.sketch_value >= 1:
            font = pygame.font.Font('fonts/gilgan.ttf', 25)
            text = font.render(str(self.sketch_value), True, (105, 105, 105))
            self.screen.blit(text, ((self.row * 80) + 10, (self.col * 80) + 10))
    """

    def draw(self):
        if self.value != 0:
            font = pygame.font.Font('fonts/gilgan.ttf', 25)
            text = font.render(str(self.value), True, (105, 105, 105))
            self.screen.blit(text, ((self.row * 80) + 32, (self.col * 80) + 30))

        elif 9 >= self.sketch_value >= 1:
            font = pygame.font.Font('fonts/gilgan.ttf', 25)
            text = font.render(str(self.sketch_value), True, (105, 105, 105))
            self.screen.blit(text, ((self.row * 80) + 10, (self.col * 80) + 10))

    def set_red_highlight(self, value):
        self.red_highlight = value

    def __str__(self):
        return f'Cell(row={self.row}, col={self.col}, value={self.value})'