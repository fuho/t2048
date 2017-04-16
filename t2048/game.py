from board import Board
from renderer.text_simple import SimpleTextRenderer

UP = ("UP", 0, 1)
DOWN = ("DOWN", 0, -1)
LEFT = ("LEFT", -1, 0)
RIGHT = ("RIGHT", 1, 0)

MOVE_DIRECTIONS = (UP, RIGHT, DOWN, LEFT)


class Game:
    def __init__(self, width=None, height=None):
        self.moves = 0
        self.score = 0
        self.board = Board(self, width, height)
        self.state = "NOT_STARTED"

    def move(self, direction):
        """
        :param direction: A tuple of (name, x,y) where x,y can be ,-1,0,1 
        """
        self.moves += 1
        if direction == UP:
            self.board.fold_up()
        if direction == DOWN:
            self.board.fold_down()
        if direction == RIGHT:
            self.board.fold_right()
        if direction == LEFT:
            self.board.fold_left()
        (_, _, value) = self.board.introduce_tile()
        if value < 0:
            self.finish()
        self.render()

    def start(self):
        # Place two tiles
        for _ in range(2):
            (x, y, value) = self.board.introduce_tile()
        # Set up renderer
        self.renderer = SimpleTextRenderer(self)
        self.state = "READY"

    def finish(self):
        self.state = "GAME OVER"

    def render(self):
        self.renderer.render()
