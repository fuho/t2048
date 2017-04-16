from abstract_renderer import AbstractRenderer


class SimpleTextRenderer(AbstractRenderer):

    def initialize(self):
        pass

    def render(self):
        print(
            "Moves: {}".format(self.game.moves).ljust(15)
            + "Score: {}".format(self.game.score).rjust(10)
        )
        print(self.game.board)