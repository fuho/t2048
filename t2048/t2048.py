from game import Game, MOVE_DIRECTIONS


def main():
    game = Game(4, 4)

    game.start()
    print(" START GAME ".center(25, "*"))
    game.render()

    for n in range(2000000):
        if game.state == "GAME OVER":
            break
        move_direction = MOVE_DIRECTIONS[n % 4]
        print("*" * 25)
        print("Moving {}".format(move_direction[0]))
        game.move(move_direction)
    print("=" * 25)
    print("GAME OVER".center(20, "#"))
    print("TOTAL MOVES: {}".format(game.moves).rjust(25))
    print("TOTAL SCORE: {}".format(game.score).rjust(25))


if __name__ == '__main__':
    main()
