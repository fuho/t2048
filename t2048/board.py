from random import randint, random

DEFAULT_WIDTH = 4
DEFAULT_HEIGHT = 4


class Board:
    def __init__(self, game, width=None, height=None, data=None):
        self.game = game
        self.width = width if width else DEFAULT_WIDTH
        self.height = height if height else DEFAULT_HEIGHT
        self.grid = [
            [(data[y][x] if data else 0) for y in range(self.height)]
            for x in range(self.width)
        ]

    @classmethod
    def from_grid(cls, data):
        width = len(data[0])
        height = len(data)
        return cls(None, width, height, data)

    def fold_selection(self, selection):
        """
        fold_selection([2,0,2,4,8]) ==> [16,0,0,0,0]
        :param selection: list of integers 
        :return: Folded selection 
        """
        if sum(selection) == 0:
            return selection
        left = None
        for i, v in enumerate(selection):
            if v == 0 and i < len(selection) - 1:
                return selection[:i] \
                       + self.fold_selection(selection[i + 1:]) \
                       + [0]
            if left == v:
                new_v = v*2
                if self.game:
                    self.game.score += new_v
                return selection[:i - 1] \
                       + self.fold_selection([new_v] + selection[i + 1:]) \
                       + [0]
            left = v
        return selection

    def get_column(self, x):
        return [self.grid[x][y] for y in range(self.height)]

    def get_row(self, y):
        return [self.grid[x][y] for x in range(self.width)]

    def set_column(self, x, selection):
        for y, v in enumerate(selection):
            self.grid[x][y] = v

    def set_row(self, y, selection):
        for x, v in enumerate(selection):
            self.grid[x][y] = v

    def fold_column(self, i, direction):
        """
        :param i: Column index 
        :param direction: Positive for down, negative for up
        """
        if not direction:
            return
        selection = self.get_column(i)
        if direction < 0:
            selection = selection[::-1]
        selection = self.fold_selection(selection)
        if direction < 0:
            selection = selection[::-1]
        self.set_column(i, selection)

    def fold_row(self, i, direction):
        """
        :param i: Row index 
        :param direction: Positive for left, negative for right
        """
        if not direction:
            return
        selection = self.get_row(i)
        if direction < 0:
            selection = selection[::-1]
        selection = self.fold_selection(selection)
        if direction < 0:
            selection = selection[::-1]
        self.set_row(i, selection)

    def fold_up(self):
        for x in range(self.width):
            self.fold_column(x, 1)

    def fold_down(self):
        for x in range(self.width):
            self.fold_column(x, -1)

    def fold_right(self):
        for y in range(self.height):
            self.fold_row(y, -1)

    def fold_left(self):
        for y in range(self.height):
            self.fold_row(y, 1)

    def introduce_tile(self):
        empties = self.get_empty_fields()
        if len(empties) < 1:
            return -1, -1, -1
        else:
            (x, y, _) = empties[randint(0, len(empties) - 1)]
        self.grid[x][y] = 2 if random() < 0.8 else 4  # mostly 2 sometimes 4
        return x, y, self.grid[x][y]

    def get_empty_fields(self):
        return [
            (x,y,self.grid[x][y])
            for x in range(self.width)
            for y in range(self.height)
            if not self.grid[x][y]
        ]

    def get_largest(self):
        return max([v for row in self.grid for v in row])

    def __getitem__(self, index):
        return self.grid[index]

    def __setitem__(self, index, value):
        self.grid[index] = value

    def __str__(self):
        result = "Grid{{{}}} {}x{}:".format(id(self), self.width, self.height)
        for y in range(self.height):
            result += "\n"
            for x in range(self.width):
                result += (
                    str(self.grid[x][y]) if self.grid[x][y] else "").rjust(6)
        return result

    def __repr__(self) -> str:
        return str(
            [
                [self.grid[x][y] for x in range(self.width)]
                for y in range(self.height)
            ]
        )

    def __eq__(self, o: object) -> bool:
        return self.__repr__() == o.__repr__()

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)

    def __hash__(self) -> int:
        return super().__hash__()

