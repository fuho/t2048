from unittest import TestCase

from t2048.t2048 import Grid


class TestGrid(TestCase):
    def setUp(self):
        super().setUp()
        self.data = [
            [0, 2, 2, 4, 0],
            [32, 4, 8, 8, 16],
            [32, 64, 4, 4, 16],
            [128, 2, 0, 4, 32],
        ]
        self.grid = Grid(5, 4, self.data)

    def test_repr(self):
        self.assertEqual(
            self.data.__repr__(),
            self.grid.grid.__repr__()
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

    def test_fold_column_left(self):
        data = [
            [2, 0, 2],
            [0, 2, 0],
            [4, 0, 0]
        ]
        self.grid = Grid(3, 3, data)
        self.grid.fold_row(0, -1)
        self.assertEqual(
            self.grid.grid.__repr__(),
            str([
                [4, 0, 0],
                [0, 2, 0],
                [4, 0, 0]
            ])
        )
