from unittest import TestCase

from t2048.t2048 import Grid


class TestGridBasics(TestCase):
    def setUp(self):
        super().setUp()
        self.data = [
            [0, 2, 2],
            [32, 4, 8],
            [32, 64, 4],
            [128, 2, 0]
        ]
        self.grid = Grid.fromGrid(self.data)

    def test_width(self):
        self.assertEqual(self.grid.width, 3)

    def test_height(self):
        self.assertEqual(self.grid.height, 4)

    def test_cell_access(self):
        self.assertEqual(self.grid.grid[0][3], 128)

    def test_eq(self):
        a = [[2, 4],
             [8, 16]]
        b = [[2, 4],
             [8, 16]]
        self.assertEqual(Grid.fromGrid(a), Grid.fromGrid(b))

    def test_neq(self):
        a = [[2, 6],
             [8, 16]]
        b = [[2, 4],
             [8, 16]]
        self.assertNotEqual(Grid.fromGrid(a), Grid.fromGrid(b))

    def test_hash(self):
        a = [[2, 6],
             [8, 16]]
        b = [[2, 6],
             [8, 16]]
        self.assertEqual(
            Grid.fromGrid(a).__hash__(),
            Grid.fromGrid(b).__hash__()
        )


class TestGridMethods(TestCase):
    def setUp(self):
        super().setUp()
        self.data = [
            [0, 2, 2, 4, 0],
            [32, 4, 8, 8, 16],
            [32, 64, 4, 4, 16],
            [128, 2, 0, 4, 32],
        ]
        self.grid = Grid.fromGrid(self.data)

    def test_repr(self):
        grid = [[1, 2], [3, 4]]
        self.assertEqual(
            Grid.fromGrid(grid).__repr__(),
            grid.__repr__()
        )
        grid = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]
        self.assertEqual(
            Grid.fromGrid(grid).__repr__(),
            grid.__repr__()
        )

    def test_get_column(self):
        self.assertListEqual(self.grid.get_column(0), [0, 32, 32, 128])
        self.assertListEqual(self.grid.get_column(1), [2, 4, 64, 2])

    def test_get_row(self):
        self.assertListEqual(self.grid.get_row(0), [0, 2, 2, 4, 0])
        self.assertListEqual(self.grid.get_row(1), [32, 4, 8, 8, 16])

    def test_fold_selection(self):
        self.assertListEqual(
            self.grid.fold_selection([0, 2, 2, 4, 0]),
            [8, 0, 0, 0, 0]
        )
        self.assertListEqual(
            self.grid.fold_selection([32, 4, 8, 8, 16]),
            [32, 4, 32, 0, 0]
        )

    def test_fold_row_left(self):
        grid = [[2, 2],
                [8, 8]]
        grid = Grid.fromGrid(grid)
        grid.fold_row(0, -1)
        self.assertEqual(
            grid.__repr__(),
            [[4, 0],
             [8, 8]].__repr__()
        )

    def test_fold_row_right(self):
        grid = [[2, 2],
                [8, 8]]
        grid = Grid.fromGrid(grid)
        grid.fold_row(0, 1)
        self.assertEqual(
            grid.__repr__(),
            [[0, 4],
             [8, 8]].__repr__()
        )
