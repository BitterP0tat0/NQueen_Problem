class Queen:
    def __init__(self, row: int, col: int, name: str) -> None:
        self.name = name
        self.row = row
        self.col = col
        self.is_alive = True

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_row(self) -> int:
        return self.row

    def set_row(self, row: int) -> None:
        self.row = row

    def get_col(self) -> int:
        return self.col

    def set_col(self, col: int) -> None:
        self.col = col
