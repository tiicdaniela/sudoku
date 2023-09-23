import sudokuGenerator
import board
import pygame
import math, random
import sys


def draw_game_start(screen):
    # initializes fonts
    font = pygame.font.Font('fonts/light.ttf', 25)

    # background image
    color = (255, 255, 255)
    screen.fill(color)
    background = pygame.image.load('background.png')
    screen.blit(background, (0, 0))

    # initializes and draws the texts
    list = ['easy', 'medium', 'hard']
    list_position = 0
    difficulty = 0

    difficulty_surface = font.render(list[list_position], 0, (105, 105, 105))
    difficulty_rectangle = difficulty_surface.get_rect(
        center=(720 // 2, 400))
    screen.blit(difficulty_surface, difficulty_rectangle)

    # initializes buttons with text
    left_text = font.render("<", 0, (105, 105, 105))
    newGame_text = font.render("new game", 0, (105, 105, 105))
    right_text = font.render(">", 0, (105, 105, 105))

    # initializes the buttons background color
    left_surface = pygame.Surface((left_text.get_size()[0] + 20, left_text.get_size()[1] + 20))
    left_surface.fill((255, 255, 255))
    left_surface.blit(left_text, (10, 10))
    newGame_surface = pygame.Surface((newGame_text.get_size()[0] + 20, newGame_text.get_size()[1] + 20))
    newGame_surface.fill((255, 255, 255))
    newGame_surface.blit(newGame_text, (10, 10))
    right_surface = pygame.Surface((right_text.get_size()[0] + 20, right_text.get_size()[1] + 20))
    right_surface.fill((255, 255, 255))
    right_surface.blit(right_text, (10, 10))

    # initializes buttons rectangles
    left_rectangle = left_surface.get_rect(
        center=(720 // 2 - 150, 400))
    newGame_rectangle = newGame_surface.get_rect(
        center=(720 // 2, 475))
    right_rectangle = right_surface.get_rect(
        center=(720 // 2 + 150, 400))

    # draws the buttons rectangles
    screen.blit(left_surface, left_rectangle)
    screen.blit(newGame_surface, newGame_rectangle)
    screen.blit(right_surface, right_rectangle)

    # loop to determine game mode selected
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if left_rectangle.collidepoint(event.pos):
                    if list_position == -3:
                        list_position = 0
                        difficulty = 0
                    else:
                        list_position -= 1
                        difficulty -= 1
                    screen.fill(color)
                    background = pygame.image.load('background.png')
                    screen.blit(background, (0, 0))

                    difficulty_surface = font.render(list[list_position], 0, (105, 105, 105))
                    difficulty_rectangle = difficulty_surface.get_rect(
                        center=(720 // 2, 400))
                    screen.blit(difficulty_surface, difficulty_rectangle)
                    screen.blit(left_surface, left_rectangle)
                    screen.blit(newGame_surface, newGame_rectangle)
                    screen.blit(right_surface, right_rectangle)

                elif right_rectangle.collidepoint(event.pos):
                    if list_position == 2:
                        list_position = 0
                        difficulty = 0
                    else:
                        list_position += 1
                        difficulty += 1
                    screen.fill(color)
                    background = pygame.image.load('background.png')
                    screen.blit(background, (0, 0))

                    difficulty_surface = font.render(list[list_position], 0, (105, 105, 105))
                    difficulty_rectangle = difficulty_surface.get_rect(
                        center=(720 // 2, 400))
                    screen.blit(difficulty_surface, difficulty_rectangle)
                    screen.blit(left_surface, left_rectangle)
                    screen.blit(newGame_surface, newGame_rectangle)
                    screen.blit(right_surface, right_rectangle)

                elif newGame_rectangle.collidepoint(event.pos):
                    return difficulty
        pygame.display.update()


def win_screen(screen):
    # loads background image
    background = pygame.image.load('background.png')
    screen.blit(background, (0, 0))

    # creates font size
    game_font = pygame.font.Font('fonts/regular.ttf', 95)
    # creates text
    win_text = game_font.render('Game Won!', 0, (0, 0, 0))
    win_rectangle = win_text.get_rect(
        center=(720 // 2, 800 // 2 - 150))
    screen.blit(win_text, win_rectangle)
    # creates exit button
    exit_font = pygame.font.Font('fonts/thin.ttf', 45)
    exit_text = exit_font.render('exit', 0, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill((255, 165, 0))
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(
        center=(720 // 2, 1000 // 2))
    screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    return False
        pygame.display.update()


def lose_screen(screen):
    # loads background image
    #background = pygame.image.load('background.png')
    #screen.blit(background, (0, 0))

    # generates Game Over text
    font = pygame.font.Font('fonts/regular.ttf', 95)
    lose_text = font.render('Game Over :(', 0, (0, 0, 0))
    lose_rectangle = lose_text.get_rect(
        center=(720 // 2, 800 // 2 - 150))
    screen.blit(lose_text, lose_rectangle)

    # generates restart button
    font = pygame.font.Font('fonts/thin.ttf', 45)
    restart_text = font.render("restart", 0, (255, 255, 255))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill((255, 165, 0))
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = restart_surface.get_rect(
        center=(720 // 2, 1000 // 2))
    screen.blit(restart_surface, restart_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    return draw_game_start(screen)
        pygame.display.update()


def solve_sudoku(board):
    def is_valid(num, row, col):
        # checks row and column
        for i in range (9):
            if board[row][i] == num or board[i][col] == num:
                return False
        # checks 3x3 box
        start_row, start_col =  3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def solve():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(num, row, col):
                            board[row][col] = num
                            if solve():
                                return True
                            # backtrack
                            board[row][col] = 0
                    return False
        return True

    if solve():
        return board
    else:
        return None


def main():
    pygame.init()
    pygame.display.set_caption('Sudoku')
    width = 720
    height = 800
    screen = pygame.display.set_mode((width, height))
    difficulty = draw_game_start(screen)
    sudoku_board = board.Board(width, height-80, screen, difficulty)

    clock = pygame.time.Clock()
    running = True

    sudoku_board.draw()

    while running is True:
        og_board = sudoku_board.original_board
        # initializes button fonts and size
        font = pygame.font.Font('fonts/thin.ttf', 45)
        # initializes button text
        back_text = font.render(" ", 0, (255, 255, 255))
        restart_text = font.render(" ", 0, (255, 255, 255))
        exit_text = font.render(" ", 0, (255, 255, 255))
        # initializes the buttons background color
        back_surface = pygame.Surface((back_text.get_size()[0] + 20, back_text.get_size()[1] + 20), pygame.SRCALPHA)
        back_surface.blit(back_text, (10, 10))
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20),
                                         pygame.SRCALPHA)
        restart_surface.blit(restart_text, (10, 10))
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20), pygame.SRCALPHA)
        exit_surface.blit(exit_text, (10, 10))
        # initializes buttons rectangles
        back_rectangle = back_surface.get_rect(
            center=(240, 1525 // 2))
        restart_rectangle = restart_surface.get_rect(
            center=(360, 1525 // 2))
        exit_rectangle = exit_surface.get_rect(
            center=(480, 1525 // 2))
        # draws the buttons rectangles
        screen.blit(back_surface, back_rectangle)
        screen.blit(restart_surface, restart_rectangle)
        screen.blit(exit_surface, exit_rectangle)

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # statements to determine if buttons where pressed
                if back_rectangle.collidepoint(event.pos):
                    difficulty = draw_game_start(screen)
                    sudoku_board = board.Board(width, height - 80, screen, difficulty)
                    sudoku_board.draw()
                elif restart_rectangle.collidepoint(event.pos):
                    sudoku_board.reset_to_original()
                elif exit_rectangle.collidepoint(event.pos):
                    running = False

                x, y = pygame.mouse.get_pos()
                row, col = sudoku_board.click(x, y)
                if row is not None:
                    sudoku_board.select(row, col)
                else:
                    sudoku_board.draw()
            elif event.type == pygame.KEYDOWN:
                try:
                    if event.key == pygame.K_LEFT:
                        col = col - 1
                        sudoku_board.select(row, col)
                    elif event.key == pygame.K_RIGHT:
                        col = col + 1
                        sudoku_board.select(row, col)
                    elif event.key == pygame.K_UP:
                        row = row - 1
                        sudoku_board.select(row, col)
                    elif event.key == pygame.K_DOWN:
                        row = row + 1
                        sudoku_board.select(row, col)
                    elif event.key == pygame.K_RETURN:
                        sudoku_board.place_number(sudoku_board.selected_cell.sketch_value)
                    elif event.key == pygame.K_BACKSPACE:
                        sudoku_board.clear()
                        sudoku_board.select(row, col)
                    else:
                        number = int(chr(event.key))
                        if 9 >= number >= 1:
                            sudoku_board.sketch(number)
                            sudoku_board.select(row, col)
                except ValueError:
                    pass
                except TypeError:
                    pass

                if sudoku_board.is_full() is True:

                    win = sudoku_board.check_board(og_board)
                    print(win)
                    if win is True:
                        # print("Game Won")
                        running = win_screen(screen)
                    else:
                        # print("Game Not Won")
                        #difficulty = lose_screen(screen)
                        #sudoku_board = board.Board(width, height - 80, screen, difficulty)
                        #sudoku_board.draw()
                        pass

        # flip() the display to put your work on screen
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == '__main__':
    main()
