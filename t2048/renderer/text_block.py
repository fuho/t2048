from abstract_renderer import AbstractRenderer

WALL = "░"


class SimpleBlockRenderer(AbstractRenderer):
    def initialize(self):
        pass

    def render(self):
        print(
            "Moves: {}".format(self.game.moves).ljust(15)
            + "Score: {}".format(self.game.score).rjust(10)
        )
        self.print_board()

    def print_board(self):
        b = self.game.board
        l = len(str(b.get_largest())) + 2
        line_length = (l+1) * b.width + 1
        for y in range(b.height):
            print(WALL * line_length)
            row = ""
            for x in range(b.width):
                row += "░{}".format(str(b[x][y]).center(l))
            print(row + WALL)
        print(WALL * line_length)
