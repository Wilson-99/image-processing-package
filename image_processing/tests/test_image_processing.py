import unittest
import numpy as np
from utils.plot import plot_image, plot_histogram

class TestImageProcessing(unittest.TestCase):

    def setUp(self):
        self.image = np.random.rand(100, 100, 3) 

    def test_plot_image(self):
        try:
            plot_image(self.image)
        except Exception as e:
            self.fail(f"plot_image raised {type(e).__name__} unexpectedly!")

    def test_plot_image_invalid_input(self):
        with self.assertRaises(ValueError):
            plot_image(None)

    def test_plot_histogram(self):
        try:
            plot_histogram(self.image)
        except Exception as e:
            self.fail(f"plot_histogram raised {type(e).__name__} unexpectedly!")

    def test_plot_histogram_invalid_input(self):
        with self.assertRaises(ValueError):
            plot_histogram(None)

if __name__ == '__main__':
    unittest.main()
