class AbstractRenderer(object):
    """Abstract renderer, takes grid in constructor"""

    def __init__(self, game):
        if not game:
            raise ReferenceError("`game` parameter required")
        self.game = game
        self.initialize()

    def initialize(self):
        raise NotImplementedError("initialize method not implemented")

    def render(self):
        raise NotImplementedError("render method not implemented")