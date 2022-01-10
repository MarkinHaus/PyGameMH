import unittest
from util.MGameM import Sprite, Screen
import random


class TestScreen(unittest.TestCase):

    def test_screen(self):
        s = Screen()
        self.assertEqual(type(s), Screen)  # add assertion here


class TestSprite(unittest.TestCase):
    s = Screen()
    rect = Sprite(s, "")
    circle = Sprite(s, "")

    def test_color(self):
        f = ["black", "red", "green", "blue", "yellow", "purple", "azul", "white"]
        c = [[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [255, 0, 255], [0, 255, 255],
             [255, 255, 255]]

        self.rect.set_color((0, 0, 0))
        self.assertEqual(self.rect.color, (0, 0, 0))

        for i in range(len(f)):
            self.rect.set_color(f[i])
            self.assertEqual(self.rect.color, c[i])

    def test_make_rect(self):
        self.assertIsNone(self.rect.make_sprite("rect", -1, 10, 10,
                                                      color="white"))

    def test_make_circle(self):
        self.assertIsNone(self.circle.make_sprite("circle", 1, radius=10, color="white"))

    def test_collision_rect_circle(self):
        self.rect.make_sprite("rect", 1, 10, 10,
                              color="white")
        self.circle.make_sprite("circle", 0, radius=10, color="white")
        self.circle.type_ = "error"

        self.rect.x = 50
        self.rect.y = 50
        self.assertIsNone(self.rect.move(0))

        self.circle.x = 50
        self.circle.y = 50
        self.assertIsNone(self.circle.move(0))
        self.circle.move(0)

        self.rect.collision_func(self.rect)

        self.assertTrue(bool(self.rect.collision_list))

        self.rect.collision_list = []

        self.rect.collision_func(self.circle)

        self.assertFalse(bool(self.rect.collision_list))

        self.circle.collisions_level = 1

        self.assertRaises(NotImplementedError, self.rect.collision_func, self.circle)

        self.circle.type_ = "circle"

        self.assertIsNone(self.rect.collision_func(self.circle))




if __name__ == '__main__':
    unittest.main()
