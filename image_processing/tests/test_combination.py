import unittest
import numpy as np
from skimage import data
from processing.combination import find_difference, transfer_histogram

class TestImageProcessing(unittest.TestCase):
    
    def setUp(self):
        self.image1 = np.random.rand(100, 100, 3)
        self.image2 = np.random.rand(100, 100, 3)

    def test_transfer_histogram_invalid_inputs(self):
        with self.assertRaises(ValueError) as context:
            transfer_histogram(self.image1, None)
        self.assertEqual(str(context.exception), "Ambas as imagens devem ser fornecidas e não podem ser None.")

        with self.assertRaises(ValueError) as context:
            transfer_histogram(None, self.image2)
        self.assertEqual(str(context.exception), "Ambas as imagens devem ser fornecidas e não podem ser None.")

        with self.assertRaises(ValueError) as context:
            transfer_histogram("invalid", self.image2)
        self.assertEqual(str(context.exception), "Ambas as entradas devem ser arrays numpy.")

        with self.assertRaises(ValueError) as context:
            transfer_histogram(self.image1, "invalid")
        self.assertEqual(str(context.exception), "Ambas as entradas devem ser arrays numpy.")

if __name__ == '__main__':
    unittest.main()