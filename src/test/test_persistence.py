import unittest
import numpy as np
import pyrootutils


root = pyrootutils.setup_root(
    search_from=__file__,
    indicator=[".git", "pyproject.toml"],
    pythonpath=True,
    dotenv=True,
)

from src.persistence import Persistence


class TestPersistence(unittest.TestCase):
    def test_persistence_one_data(self):
        data = [[6, 9, 7, 4, 5, 7, 8, 2, 1, 2]]
        persistence = Persistence()
        res = persistence.fit_transform(data)

        gt = np.asarray([[1.0, 9], [4.0, 8.0], [6.0, 9.0]])
        self.assertTrue(np.array_equal(res[0], gt))

    def test_persistence_several(self):
        data = [[6, 9, 7, 4, 5, 7, 8, 2, 1, 2], [0, 0, 3, 8, 7, 5, 5, 0, 4, 3]]
        persistence = Persistence()
        res = persistence.fit_transform(data)

        gt = np.asarray(
            [[[1.0, 9], [4.0, 8.0], [6.0, 9.0]], [[0.0, 8.0], [0.0, 8.0], [3.0, 4.0]]]
        )
        self.assertTrue(np.array_equal(res, gt))


if __name__ == "__main__":
    unittest.main()
