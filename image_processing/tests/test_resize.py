import unittest
import numpy as np
from skimage import data
from processing.transformation import resize_image 

class TestImageResize(unittest.TestCase):

    def setUp(self):
        self.image = data.astronaut()  
        self.image_shape = self.image.shape

    def test_resize_image_valid(self):
        proportion = 0.5
        resized_image = resize_image(self.image, proportion)
        self.assertEqual(resized_image.shape[0], round(self.image_shape[0] * proportion))
        self.assertEqual(resized_image.shape[1], round(self.image_shape[1] * proportion))

    def test_resize_image_invalid_proportion(self):
        with self.assertRaises(ValueError):
            resize_image(self.image, 1.5)

    def test_resize_image_invalid_type(self):
        with self.assertRaises(TypeError):
            resize_image("not_an_image", 0.5)

    def test_resize_image_zero_proportion(self):
        resized_image = resize_image(self.image, 0)
        self.assertEqual(resized_image.shape, (0, 0, 3)) 

    def test_resize_image_one_proportion(self):
        resized_image = resize_image(self.image, 1)
        self.assertTrue(np.array_equal(resized_image, self.image))  

if __name__ == '__main__':
    unittest.main()
