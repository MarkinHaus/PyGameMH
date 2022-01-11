import pygame

from util.Color import name_to_list
from math import sqrt


class Sprite:
    def __init__(self, screen, name: str):
        pass  # Takes a MGame Screen to show the sprite and tak a name

    def __str__(self):
        return # returns information string : f"Type: {self.type_}, width {self.width}, height {self.height},
        # x {self.x}, y {self.y} \n"

    def set_color(self, color: str or list):
        pass  # takes a color string or a list.

    def make_sprite(self, type_: str, collisions_level: int, width: float = 0, height: float = 0, radius: float = 0,
                    color: str or list or None = None, file: str or None = None, img_size: int = 1) -> None:
        pass # make sprite of type_ type
        # if type_ == "img":
        #     self.img_()
        # if type_ == "rect":
        #     self.rect_()
        # if type_ == "circle":
        #     self.circle_()
        # if type_ == "polygon":
        #     self.polygon_()
        # if type_ == "ellipse":
        #     self.ellipse_()
        # if type_ == "arc":
        #     self.arc_()
        # if type_ == "line":
        #     self.line_()
        # if type_ == "lines":
        #     self.lines_()
        # if type_ == "aaline":
        #     self.aalines()

    def move(self, dt: float):
        pass  # takes a dt in milliseconds (display between 2 Frames synchronized to the fps and clock speed) move sprite

    def fx(self, x: float):
        pass  # set peed in x

    def fy(self, y: float):
        pass  # set peed in y

    def add_col_sprite(self, sprite, point: list):
        pass  # use collision_func to test for a collision

    def rect_(self):

        # make a rect

        def draw_func():
            pass  # set draw_func

        def collision_func(sprite):
            pass  # set collision_func

    def img_(self):

        # make a img

        def draw_func():
            pass  # set draw_func

        def collision_func(sprite):
            pass  # set collision_func

    def circle_(self):

        # make a circle

        def draw_func():
            pass  # set draw_func

        def collision_func(sprite):
            pass  # set collision_func

    def polygon_(self):
        raise NotImplementedError

    def ellipse_(self):
        raise NotImplementedError

    def arc_(self):
        raise NotImplementedError

    def line_(self):
        raise NotImplementedError

    def lines_(self):
        raise NotImplementedError

    def aalines(self):
        raise NotImplementedError


class Background:

    def __init__(self, screen, image_n, wh=(0, 0), img_size=1):
        pass

    def show(self, move_x: bool = False, speed_x: int = 15, move_y: bool = False, speed_y: int = 15, dt: float = 1):
        pass


class Mouse:

    def __init__(self, screen, img_s: list or None = None):
        pass

    def mouse_get_sprite(self) -> Sprite:
        pass

    def show_m(self, click: bool = False):
        pass


class Screen:
    def __init__(self, width: int = 800, height: int = 600, background: str = 'black', title: str = ""):
        pass


class Text:

    def __init__(self, screen: Screen):
        pass

    def init_font(self, size=30, text_type='Arial.ttf'):
        pass

    def show(self, text, xy, color=(0, 0, 0)):
        assert self.init, "Pleas Init Font first, Text.init_font(size, systemFontName)"
        pass


class Design:
    pass


# for event in pygame.event.get():
#    if event.type == pygame.QUIT:
#        pygame.quit()
#    if event.type == pygame.WINDOWLEAVE:
#        org = [0, 0]
#        tblr = [0, 0, 0, 0]

#    if event.type == pygame.MOUSEBUTTONDOWN:
#        # if event.button == : 0 to 5 / 3
#        pass

#    if event.type == pygame.KEYDOWN:
#
#        #if pygame.key.get_pressed()[pygame.K_w]
#
#        pass


class Physics:
    @staticmethod
    def border_left_collision(sprite: Sprite, screen: Screen):
        pass

    @staticmethod
    def border_right_collision(sprite: Sprite):
        pass

    @staticmethod
    def border_top_collision(sprite: Sprite):
        pass
    @staticmethod
    def border_bottom_collision(sprite: Sprite, screen: Screen):
        pass

    @staticmethod
    def border_collision(sprite, screen: Screen):
        return [Physics.border_left_collision(sprite=sprite, screen=screen),
                Physics.border_right_collision(sprite=sprite),
                Physics.border_top_collision(sprite=sprite),
                Physics.border_bottom_collision(sprite=sprite, screen=screen)]

    @staticmethod
    def collision(all_sprite, type_="simpel"):
        if type_ == "simpel":
            pass


clock = pygame.time.Clock()
