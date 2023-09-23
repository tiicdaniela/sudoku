import math, random
"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/
"""
random.seed()


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = int(math.sqrt(row_length))
        templist = []
        for i in range(9):
            temprow = []
            for j in range(9):
                temprow.append(0)
            templist.append(temprow)
        self.board = templist

    def get_board(self):
        return self.board

    def print_board(self):
        pass

    def valid_in_row(self, row, num):
        for i in self.board[row]:
            if i == num:
                return False
        return True

    def valid_in_col(self, col, num):
        for row in self.board:
            if row[int(col)] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        row_index = row_start - 1
        for row in range(self.box_length):
            row_index += 1
            col_index = col_start - 1
            for col in range(self.box_length):
                col_index += 1
                if self.board[row_index][col_index] == num:
                    return False

        return True

    def is_valid(self, row, col, num):
        # floors row and col to get only whole number intervals of 3 which is the start position of the box
        if self.valid_in_box((row // 3) * 3, (col // 3) * 3, num):
            if self.valid_in_row(row, num):
                if self.valid_in_col(col, num):
                    return True
        return False

    def fill_box(self, row_start, col_start):
        numbers = [num for num in range(1, 10)]
        row_index = row_start
        # creates a list of numbers 1-9 to be modified for eliminating duplicates
        for row in self.board[row_start:(row_start + 3)]:
            col_index = col_start
            for col in self.board[row_index][col_start:(col_start + 3)]:
                not_used = False
                while not_used is False:  # makes sure random integer is included in list of available digits
                    random_digit = random.randint(1, 9)
                    if random_digit in numbers:
                        not_used = True
                numbers.remove(random_digit)
                row[col_index] = random_digit
                col_index += 1
            row_index += 1

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        for i in range(self.removed_cells):
            coords_valid = False
            while not coords_valid:
                coords = (random.randint(0, self.row_length - 1),
                          random.randint(0,
                                         # generates a tuple of random coordinates within the board
                                         self.row_length - 1))
                # checks for removing an already removed cell
                if self.board[coords[0]][coords[1]] != 0:
                    coords_valid = True
            self.board[coords[0]][coords[1]] = 0


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
