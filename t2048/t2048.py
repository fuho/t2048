from random import randint, random

DEFAULT_WIDTH = 4
DEFAULT_HEIGHT = 4


class Grid:
    def __init__(self, width=None, height=None, data=None):
        self.width = width if width else DEFAULT_WIDTH
        self.height = height if height else DEFAULT_HEIGHT
        self.grid = [
            [(data[y][x] if data else 0) for y in range(self.height)]
            for x in range(self.width)
        ]

    def fold_selection(self, selection):
        """
        [2,0,2,4,8] - > [16,0,0,0,0]
        :param selection: 
        :return: Folded selection 
        """
        if sum(selection) == 0:
            return selection
        left = None
        for i, v in enumerate(selection):
            if v == 0 and i < len(selection) - 1:
                r = selection[:i] \
                    + self.fold_selection(selection[i + 1:]) \
                    + [0]
                return r
            if left == v:
                return selection[:i - 1] \
                       + self.fold_selection([v * 2] + selection[i + 1:]) \
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
        if direction > 0:
            selection = selection[::-1]
        selection = self.fold_selection(selection)
        if direction > 0:
            selection = selection[::-1]
        self.set_column(i, selection)

    def fold_row(self, i, direction):
        """
        :param i: Row index 
        :param direction: Positive for right, negative for left
        """
        if not direction:
            return
        selection = self.get_row(i)
        if direction > 0:
            selection = selection[::-1]
        selection = self.fold_selection(selection)
        if direction > 0:
            selection = selection[::-1]
        self.set_row(i, selection)

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
                    str(self.grid[x][y]) if self.grid[x][y] else "").rjust(5)
        return result + "\n"

    def __repr__(self) -> str:
        return str(
            [
                [self.grid[x][y] for x in range(self.width)]
                for y in range(self.height)
            ]
        )


class Game:
    def __init__(self, width=None, height=None, grid=None):
        self.width = width if width else DEFAULT_WIDTH
        self.height = height if height else DEFAULT_HEIGHT
        self.grid = grid if grid else Grid(self.width, self.height)
        self.new_game()

    def move(self, direction):
        """
        :param direction: A tuple of (x,y) where each can be -1,0,1 
        :return: Updated grid 
        """
        if direction == (0, 1):  # up
            for x in range(self.width):
                self.grid.fold_column(x, 1)
        if direction == (0, -1):  # down
            for x in range(self.width):
                self.grid.fold_column(x, -1)
        if direction == (1, 0):  # right
            for y in range(self.height):
                self.grid.fold_row(y, 1)
        if direction == (-1, 0):  # left
            for y in range(self.height):
                self.grid.fold_row(y, -1)

    def new_game(self):
        self.grid = Grid(self.width, self.height)
        for _ in range(2):
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            self.grid[x][
                y] = 2 if random() < 0.8 else 4  # mostly 2 sometimes 4


if __name__ == '__main__':
    game = Game(4, 4)
    data = [
        [0, 2, 2, 4, 8],
        [32, 4, 8, 8, 16],
        [32, 64, 4, 4, 16],
        [128, 2, 0, 4, 32],
    ]
    game.grid = Grid(5, 4, data)
    print(game.grid)
    print("Moving left")
    game.move((-1, 0))
    print(game.grid)
    print("Moving right")
    game.move((1, 0))
    print(game.grid)
    print("Moving down")
    game.move((0, -1))
    print(game.grid)
