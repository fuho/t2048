from grid import Grid


class Game:
    def __init__(self, width=None, height=None):
        self.moves = 0
        self.grid = Grid(width, height)
        self.state = "NOT_STARTED"

    def move(self, direction):
        """
        :param direction: A tuple of (x,y) where each can be -1,0,1 
        :return: Updated grid 
        """
        if direction == (0, 1):  # up
            for x in range(self.grid.width):
                self.grid.fold_column(x, 1)
        if direction == (1, 0):  # right
            for y in range(self.grid.height):
                self.grid.fold_row(y, 1)
        if direction == (0, -1):  # down
            for x in range(self.grid.width):
                self.grid.fold_column(x, -1)
        if direction == (-1, 0):  # left
            for y in range(self.grid.height):
                self.grid.fold_row(y, -1)
        (_, _, value) = self.grid.introduce_tile()
        self.moves += 1
        if value < 0:
            self.finish()

    def start(self):
        for _ in range(2):
            (x, y, value) = self.grid.introduce_tile()
        self.state = "READY"

    def finish(self):
        self.state = "GAME OVER"


def main():
    game = Game(4, 4)
    # data = [
    #     [0, 2, 2, 4, 8],
    #     [32, 4, 8, 8, 16],
    #     [32, 64, 4, 4, 16],
    #     [128, 2, 0, 4, 32],
    # ]
    # game.grid = Grid.fromGrid(data)
    game.start()
    print(game.grid)
    dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    for n in range(2000000):
        game.move(dir[n % 4])
        print(
            "Moves: {}".format(n).ljust(15)
            + "Score: {}".format(game.grid.score).rjust(10)
        )
        if game.state == "GAME OVER":
            break
        print(game.grid)
    print("GAME OVER".center(20, "#"))
    print("TOTAL MOVES: {}".format(game.moves).rjust(20))
    print("TOTAL SCORE: {}".format(game.grid.score).rjust(20))


if __name__ == '__main__':
    main()
