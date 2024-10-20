import unittest
import numpy as np
from skimage.io import imsave
import os
from utils.io import read_image, save_image

class TestImageIO(unittest.TestCase):

    def setUp(self):
        self.image = (np.random.rand(100, 100, 3) * 255).astype(np.uint8)  
        self.test_image_path = 'test_image.png'

    def test_read_image_valid(self):
        imsave(self.test_image_path, self.image)
        image = read_image(self.test_image_path)
        self.assertEqual(image.shape, self.image.shape)

    def test_read_image_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            read_image('invalid_path.png')

    def test_save_image_valid(self):
        try:
            save_image(self.image, self.test_image_path)
        except Exception as e:
            self.fail(f"save_image raised {type(e).__name__} unexpectedly!")

    def test_save_image_invalid(self):
        with self.assertRaises(ValueError):
            save_image(None, 'output_image.png')

    def tearDown(self):
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)

if __name__ == '__main__':
    unittest.main()
