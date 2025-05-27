from Queen_init.queen_init import Queen

class Board:
    def __init__(self, size: int):
        self.size: int = size
        self.queens: list[Queen] = [] 

    def place_queen(self, queen: Queen) -> bool:
        if self.is_safe(queen.row, queen.col):
            self.queens.append(queen)
            return True
        return False

    def is_safe(self, row: int, col: int) -> bool:
        for q in self.queens:
            if q.row == row or q.col == col or abs(q.row - row) == abs(q.col - col):
                return False
        return True

    def remove_queen(self, row: int) -> None:
        self.queens = [q for q in self.queens if q.row != row]

    def display(self) -> None:
        board = [['.' for _ in range(self.size)] for _ in range(self.size)]
        for q in self.queens:
            board[q.row][q.col] = 'Q'
        for row in board:
            print(' '.join(row))
