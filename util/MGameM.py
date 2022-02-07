import math
import time
from abc import ABC

import pygame
from typing import List

from util.Color import name_to_list

import pymunk


# importing all necessary moduls

class Sprite:  # blueprint for super class handles all game objects to print and pymunk simulation
    def __init__(self, screen, name: str, def_cord: str = "bl"):

        """
        callable functions :
            *-> function must bee called

            *make_sprite
            add_to_space
            *draw_func

            do_kill
            if_of_screen
            debug_draw_rect
            slow_down
            set_do_slow_down
            rotate
            do_rotate

        :param screen: screen to draw sprite
        :param name: name to identify sprite in a list
        :param def_cord: define origin bl = bottem left | tl = top left
        """

        self.screen: Screen = screen
        self.name = name
        self.def_cord = def_cord
        self.dt = 1

        # vars for all objects
        self.type_: str = ""
        self.collisions_level: int = 0
        self.color: tuple = (0, 0, 0)
        self.draw_func = None  # draw the sprite to screen

        # for type = line and rect
        self.width: float = 0
        self.height: float = 0

        # for type = line
        self.point1: tuple or list or None = (0, 0)
        self.point2: tuple or list or None = (0, 0)

        # for type = img
        self.img: pygame.image = None
        self.file: str = ""
        self.img_size: int = 1

        # for type = circle
        self.radius: float = 0

        self.aa_lines_list: list = []
        self.aa_lines_list_ob: List["Sprite"] = []
        self.is_closed = False

        # physics stuff
        self.physics = False
        self.body_type = pymunk.Body.STATIC
        self.body: pymunk.Body = pymunk.Body(1, 1, body_type=self.body_type)
        self.shape: pymunk.shapes = pymunk.shapes
        self.elasticity = 0
        self.density = 1
        self.friction = 0
        self.auto_angel = [0, False]

        # set behavior
        self.do_slow_down = False
        self.debug_img_rot_draw = False  # type specific img
        self.kill = False

    def __str__(self):
        return f"Type: {self.type_}, name {self.name}, id:  {self}, \n"

    def do_kill(self):  # allows killing self if future necessary clear memory
        return self.kill

    def set_color(self, color: str or list, color_keys: list = ()):  # convert color for pygame using The Color module
        if self.type_ == "box":
            list(map(lambda line: line.set_color(color if not color_keys else
                                                 color_keys[self.aa_lines_list_ob.index(line)]), self.aa_lines_list_ob))
        else:
            self.color = color
            if type(color) == str:
                self.color = name_to_list(color)

    def add_to_space(self, space_):  # adds shape and body to simulation space for pymunk
        if self.type_ == "box":
            list(map(lambda line: line.add_to_space(space_), self.aa_lines_list_ob))
        else:
            space_.add(self.shape, self.body)

    def set_shape_props(self):  # set extra physic props to object
        self.shape.elasticity = self.elasticity
        self.shape.density = self.density
        self.shape.friction = self.friction
        self.shape.collision_type = self.collisions_level

    def if_of_screen(self):  # test if position of object is not in screen ( you can't see it any loger )
        return sum(self.body.position) >= self.screen.width + self.screen.height + 100 or sum(
            self.body.position) <= -100

    def make_sprite(self,
                    type_: str,
                    collisions_level: int = 0,
                    point1: list or tuple or None = None,
                    point2: list or tuple or None = None,
                    width: float = 0, height: float = 0,
                    radius: float = 0,
                    color: str or list or None = None,
                    file: str or None or pygame.image = None,
                    img_size: int = 1,
                    mass: int = 1,
                    moment: int = 1,
                    position: list or tuple = (0, 0),
                    velocity: list or tuple = (0, 0),
                    elasticity: float = 0,
                    physics: bool = False,
                    ken: bool = False,
                    density: float = 1,
                    friction: float = 0,
                    aa_lines_list: list or tuple = (),
                    is_closed: bool = False,
                    collisions_for_sep_aa_line: list or tuple = (),
                    color_for_aa_line: list or tuple = (), new_body=True):

        # super function makes sprite object (mistakes are often made)
        """
        :param type_: string type of object : img rect circle line box | not implemented jet: polygon ellipse
        :param collisions_level: int a real number for identifying object in physic simulation ( collision handler )
        :param point1: (int, int) point in  self.def_cord defined space used for type line
        :param point2: (int, int) point in  self.def_cord defined space used for type line
        :param width: int defined width of object
        :param height: int defined height of object
        :param radius: int defined radius of object
        :param color: (von 0 bis 255, von 0 bis 255,von 0 bis 255) defined color of object
        :param file: str or img the image witch should have been drawn on screen
        :param img_size: zoom in +1 or aut -1 normal image size = 1
        :param mass: float defined mass of object
        :param moment: float defined moment of object
        :param position: can bee (int or float, int or float) must bee bei initialising (int, int)
        :param velocity: float defined velocity of object
        :param elasticity: float defined elasticity of object
        :param physics: bool Body type = Statick (False) or Dynamic (True)
        :param ken: physics must bee True Body type = Kinematic (True) default False
        :param density: float defined density of object
        :param friction: float defined friction of object
        :param aa_lines_list: list of points to make a box object
        :param is_closed: connect the first and the last point of box oject
        :param collisions_for_sep_aa_line: set collisions_level for every single line
        :param color_for_aa_line: set color for every single line
        :param new_body: make new physic object default True
        :return: sprite object


        # for physics must be added to space

        self.add_to_space(space)

        # list(
        #    map(
        #        lambda sprite_: sprite_.add_to_space(space)
        #        , sprites
        #    )
        # )
        # lambda sprite: sprite.add_to_space(space) -> def _lambda_(sprite): sprite.add_to_space(space)


        # make circle

        ball = Sprite(screen, "ball")  # ball
        ball.make_sprite(type_="circle",
                     radius=10,
                     color="white",
                     collisions_level=1,
                     position=(screen.width / 2, screen.height / 2),
                     velocity=(240 * random.choice([-1, 1]), 240 * random.choice([-1, 1])),
                     mass=10,
                     moment=10,
                     elasticity=1, physics=True)


        # make rect

        rect = Sprite(screen, "rect1")  # rect
        rect.make_sprite("rect", width=80, height=80, elasticity=1,
                        position=(400, 400), color="Blue", physics=True,
                        velocity=(50. -50))


        # make img

        img = Sprite(screen, "img1")
        img.make_sprite("img", elasticity=1,
                        position=(400, 400), physics=True, velocity=(20, 10),
                        file="img/testIB.png")


        """

        self.set_color(color)
        if not self.type_:
            self.type_ = type_

        self.radius: float = radius
        self.width = width
        self.height = height
        self.collisions_level = collisions_level
        self.file = file
        self.img_size = img_size
        self.physics = physics
        self.elasticity = elasticity
        self.density = density
        self.friction = friction
        self.point1 = point1
        self.point2 = point2
        self.aa_lines_list = aa_lines_list
        self.is_closed = is_closed

        if new_body:
            if self.physics:

                self.body = pymunk.Body(mass, moment, body_type=pymunk.Body.DYNAMIC) if not ken else \
                    pymunk.Body(mass, moment, body_type=pymunk.Body.KINEMATIC)
            else:
                self.body = pymunk.Body(body_type=pymunk.Body.STATIC)

        self.body.position = position if position else self.body.position
        self.body.velocity = velocity if velocity and self.physics else self.body.velocity

        if type_ == "img":
            self.img_()
        if type_ == "rect":
            self.rect_()
        if type_ == "circle":
            self.circle_()
        if type_ == "polygon":
            self.polygon_()
        if type_ == "ellipse":
            self.ellipse_()
        if type_ == "arc":
            self.arc_()
        if type_ == "line":
            self.line_()
        if type_ == "box":
            self.aalines(collisions_for_sep_aa_line, color_for_aa_line)

        return self

    def rect_(self):

        self.shape = pymunk.Poly.create_box(self.body, (self.width, self.height))
        self.set_shape_props()

        def rectRotated(surface, color, pos, fill, border_radius, rotation_angle, rotation_offset_center=(0, 0),
                        nAntialiasingRatio=1):
            """ # https://stackoverflow.com/questions/36510795/rotating-a-rectangle-not-image-in-pygame @ Alexandre Mazel
            - rotation_angle: in degree
            - rotation_offset_center: moving the center of the rotation: (-100,0) will turn the rectangle around a point 100 above center of the rectangle,
                                                 if (0,0) the rotation is at the center of the rectangle
            - nAntialiasingRatio: set 1 for no antialising, 2/4/8 for better aliasing
            """
            nRenderRatio = nAntialiasingRatio

            sw = pos[2] + abs(rotation_offset_center[0]) * 2
            sh = pos[3] + abs(rotation_offset_center[1]) * 2

            surfcenterx = sw // 2
            surfcentery = sh // 2
            s = pygame.Surface((sw * nRenderRatio, sh * nRenderRatio))
            s = s.convert_alpha()
            s.fill((0, 0, 0, 0))

            rw2 = pos[2] // 2  # halfwidth of rectangle
            rh2 = pos[3] // 2

            pygame.draw.rect(s, color, ((surfcenterx - rw2 - rotation_offset_center[0]) * nRenderRatio,
                                        (surfcentery - rh2 - rotation_offset_center[1]) * nRenderRatio,
                                        pos[2] * nRenderRatio, pos[3] * nRenderRatio), fill * nRenderRatio,
                             border_radius=border_radius * nRenderRatio)
            s = pygame.transform.rotate(s, rotation_angle)
            if nRenderRatio != 1: s = pygame.transform.smoothscale(s, (
                s.get_width() // nRenderRatio, s.get_height() // nRenderRatio))
            incfromrotw = (s.get_width() - sw) // 2
            incfromroth = (s.get_height() - sh) // 2
            surface.blit(s, (pos[0] - surfcenterx + rotation_offset_center[0] + rw2 - incfromrotw,
                             pos[1] - surfcentery + rotation_offset_center[1] + rh2 - incfromroth))

        def draw_func():
            rectRotated(self.screen.surface, self.color, [self.body.position[0] - round(self.width / 2),
                                                          self.screen.height - self.body.position[1] - round(
                                                              self.height / 2), self.width, self.height], False, 0,
                        math.degrees(-self.body.angle))

        if not self.draw_func:
            self.draw_func = draw_func

    def debug_draw_rect(self, color=(150, 150, 150)):  # draw a rect from top left to bottem right ( is not the hitbox)
        pygame.draw.rect(self.screen.surface, color, (self.body.position[0] - round(self.width / 2),
                                                      self.screen.height - self.body.position[
                                                          1] - round(
                                                          self.height / 2), self.width, self.height))

    def speed_convert_img(self):
        self.img = self.img.convert()

    def set_do_slow_down(self, set_=False):
        self.do_slow_down = set_

    def slow_down(self, friction):  # self.do_slow_down must be True body slows down
        if self.do_slow_down:
            self.body.velocity = (self.body.velocity[0] / friction, self.body.velocity[1] / friction)

    def rotate(self, angle_rate, do=False):  # set rotation speed if do is True else set slowdown rate if do is False
        self.auto_angel = [angle_rate, do]

    def do_rotate(self, f=0.1):  # rotate object by self.rotate(...) must bee called in main game loop
        if self.auto_angel[1]:
            self.body.angle += self.auto_angel[0]
            if abs(self.body.angle) >= 2 * math.pi:
                self.body.angle = 0
        else:
            if abs(round(self.auto_angel[0] * 100)) == 10:
                self.auto_angel[0] = 0
            else:
                if self.auto_angel[0] < 0:
                    self.auto_angel[0] += f
                    self.body.angle += self.auto_angel[0]

                if self.auto_angel[0] > 0:
                    self.auto_angel[0] -= f
                    self.body.angle += self.auto_angel[0]

    def img_(self):
        self.img = self.file
        if type(self.file) == str:
            self.img = pygame.image.load(str(self.file)).convert_alpha()

        if not self.width:
            self.width = self.img.get_width()

        if not self.height:
            self.height = self.img.get_height()

        if self.img_size != 1:
            self.width, self.height = self.width * self.img_size, self.height * self.img_size
            self.img = pygame.transform.scale(self.img, (self.width, self.height))

        def draw_func():

            x, y = parser((self.body.position[0], self.body.position[1]), self.screen.height)
            image_rect = self.img.get_rect(
                topleft=(x - self.width / 2, y - self.height / 2))
            offset_center_to_pivot = pygame.math.Vector2(
                [x, y]) - image_rect.center

            # roatated offset from pivot to center
            rotated_offset = offset_center_to_pivot.rotate(-math.degrees(-self.body.angle))

            # roatetd image center
            rotated_image_center = (x - rotated_offset.x, y - rotated_offset.y)

            # get a rotated image
            rotated_image = pygame.transform.rotate(self.img, -math.degrees(-self.body.angle))
            rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

            # rotate and blit the image
            self.screen.surface.blit(rotated_image,
                                     rotated_image_rect)

            if self.debug_img_rot_draw:
                pygame.draw.rect(self.screen.surface, (255, 0, 0),
                                 (*rotated_image_rect.topleft, *rotated_image.get_size()),
                                 2)

        if not self.draw_func:
            self.draw_func = draw_func

        self.rect_()

    def circle_(self):

        self.shape = pymunk.Circle(self.body, self.radius)
        self.set_shape_props()

        def draw_func():
            pygame.draw.circle(self.screen.surface, self.color, parser(self.body.position, self.screen.height),
                               self.radius)

        if not self.draw_func:
            self.draw_func = draw_func

    def polygon_(self):
        raise NotImplementedError

    def ellipse_(self):
        raise NotImplementedError

    def arc_(self):
        raise NotImplementedError

    def line_(self):
        self.shape = pymunk.Segment(self.body, parser(self.point1, self.screen.height, def_cord=self.def_cord),
                                    parser(self.point2, self.screen.height, def_cord=self.def_cord), self.width / 2)

        self.set_shape_props()

        def draw_func_tl():
            x1, y1 = self.point1
            x2, y2 = self.point2
            pygame.draw.line(self.screen.surface, self.color, (x1, y1),
                             (x2, y2), int(self.width))

            pygame.draw.circle(self.screen.surface, self.color, (x1, y1), round(self.width / 2))
            pygame.draw.circle(self.screen.surface, self.color, (x2, y2), round(self.width / 2))

        def draw_func_bl():
            pygame.draw.line(self.screen.surface, self.color, parser(self.point1, self.screen.height, def_cord="tl"),
                             parser(self.point2, self.screen.height, def_cord="tl"), int(self.width))
            x1, y1 = parser(self.point1, self.screen.height, def_cord="tl")
            x2, y2 = parser(self.point2, self.screen.height, def_cord="tl")
            pygame.draw.circle(self.screen.surface, self.color, (x1, y1), round(self.width / 2))
            pygame.draw.circle(self.screen.surface, self.color, (x2, y2), round(self.width / 2))

        if not self.draw_func:
            self.draw_func = draw_func_tl if self.def_cord == "tl" else draw_func_bl

    def aalines(self, collisions_for_sep_aa_line, color_for_aa_line):

        if not collisions_for_sep_aa_line:
            collisions_for_sep_aa_line = [self.collisions_level] * (len(self.aa_lines_list) - 1)

        if not color_for_aa_line:
            color_for_aa_line = [self.color] * (len(self.aa_lines_list) - 1)

        start_point = self.aa_lines_list[0]
        for point in self.aa_lines_list[1:]:
            index = self.aa_lines_list.index(point)
            self.aa_lines_list_ob.append(Sprite.aa_lin(self, index, start_point, point,
                                                       collisions_for_sep_aa_line[index - 1],
                                                       color_for_aa_line[index - 1]))
            start_point = point

        if self.is_closed:
            self.aa_lines_list_ob.append(
                Sprite.aa_lin(self, self.aa_lines_list.index(self.aa_lines_list[-1]), start_point,
                              self.aa_lines_list[0], collisions_for_sep_aa_line[-1], color_for_aa_line[-1]))

        def draw_func():
            list(map(lambda line: line.draw_func(), self.aa_lines_list_ob))

        if not self.draw_func:
            self.draw_func = draw_func

    @classmethod
    def aa_lin(cls, aa_lines: ["Sprite"], id, start_point, end_point, collisions_level, color=(0, 0, 0)):
        line = Sprite(aa_lines.screen, f"{aa_lines.name}|aa_line{id}")
        line.make_sprite(type_="line", width=aa_lines.width, point1=start_point, point2=end_point, color=color,
                         collisions_level=collisions_level, elasticity=aa_lines.elasticity)

        return line


class Map:  # sorry not finished jet | Build on top fo Sprites
    """
    # in main loop -> map.draw()
    --------------------------------------
    statick | map = Map(screen, "statick", color="white")
    ---------------------------------------
    statick-img | map = Map(screen, "statick-img")

    map.load_statick_img("ID1", "img/test.png")
    map.load_statick_img("ID2", "img/test1.png")

    map.lode_new("ID1") or map.lode_new("ID2")
    ---------------------------------------
    dynamic-img | map = Map(screen, "dynamic-img")

    map.load_statick_img("ID1", "img/test.png")
    map.load_dynamic_img("ID3", "img/test.png", loop=(0, 1) -> move up | loop=(0, -1) -> move down |
                                              , loop=(1, 0) -> move right | loop=(-1, 0) -> move left |

    map.speed = [horizontal speed, vertical speed]

    """

    def __init__(self, screen, type_, color=(0, 0, 0)):  # types = statick statick-img dynamic-img

        if type(color) == str:
            color = name_to_list(color)
        self.images = {}
        self.camera_position = []
        self.loop = [0, 0]
        self.type = type_
        self.color = color
        self.screen = screen
        self.color_key = (0, 0, 0)
        self.id_ = 0
        self.speed = [-10, 0]

    def lode_new(self, id_):
        self.id_ = id_

    def load_statick_img(self, id_, file):
        self.lode_new(id_)
        self.images[self.id_] = Sprite(self.screen, f"Image-BG{id_}").make_sprite("img", file=file,
                                                                                  position=(self.screen.width / 2,
                                                                                            self.screen.height / 2))

    def load_dynamic_img(self, id_, file, loop=(1, 0)):
        self.lode_new(id_)
        img = file
        self.loop = loop
        if type(file) == str:
            img = pygame.image.load(str(file)).convert_alpha()

        self.load_map(["x", "x", "x"] if self.loop[0] else ["x", "\n", "x", "\n", "x"],
                      {"spec": {"map": (img.get_width() * (3 if self.loop[0] else 1),
                                        img.get_height() * (3 if self.loop[1] else 1)),
                                "wh": (img.get_width(), img.get_height())}, "x": img}, id_)

    def load_map(self, map_, spec, id_):  # map_ = ["x", "x", "x", "/n",
        #                                     "x", "x", "x", "/n",
        #                                     "x", "x", "x", "/n",
        # ] spec = {"spec": {"map": (width, height), "wh": ( width, height)}, "x": img} #3840 720 ####
        spec_wh = spec["spec"]
        print(spec_wh["map"][0], spec_wh["map"][1], "####")
        sprite = pygame.Surface((spec_wh["map"][0], spec_wh["map"][1]))
        sprite.set_colorkey(self.color_key)
        x, y = (0, 0)

        for ob in map_:
            if ob == "\n":
                x = 0
                y += spec_wh["wh"][1]
            else:
                print(x, y)
                sprite.blit(spec[ob], (x, y), (0, 0, spec_wh["wh"][0], spec_wh["wh"][0]))
                x += spec_wh["wh"][0]

        # in Image-BGimg1 Vec2d(5760.0, 360.0)s
        self.images[id_] = Sprite(self.screen, f"Image-BG{id_}").make_sprite("img", file=sprite,
                                                                             position=(self.screen.width / 2,
                                                                                       self.screen.height / 2),
                                                                             physics=False)
        self.loop = (self.screen.width / 2, self.screen.height / 2)

    def camera_to_pos(self, pos):
        self.images[self.id_].body.velocity = -abs(self.images[self.id_].body.position[0] - pos[0]), \
                                              -abs(self.images[self.id_].body.position[1] - pos[1])

    def draw(self):
        self.screen.surface.fill(self.color)
        if self.type == "statick-img":
            self.images[self.id_].draw_func()
        if self.type == "dynamic-img":

            print(self.images[self.id_].body.position[1], self.screen.height, self.speed[1] > 0)

            self.images[self.id_].body.position = [self.images[self.id_].body.position[0] + self.speed[0],
                                                   self.images[self.id_].body.position[1] + self.speed[1]]

            self.images[self.id_].draw_func()

            if self.images[self.id_].body.position[0] + self.images[self.id_].width / 2 >= self.screen.width + \
                    self.images[self.id_].width / 2 and self.speed[0] > 0:
                self.images[self.id_].body.position = 0, self.images[self.id_].body.position[1]

            if self.images[self.id_].body.position[0] + self.images[self.id_].width / 2 <= self.images[
                self.id_].width / 2 and self.speed[0] < 0:
                self.images[self.id_].body.position = self.screen.width, self.images[self.id_].body.position[1]

            if self.images[self.id_].body.position[1] >= self.screen.height and self.speed[1] > 0:
                self.images[self.id_].body.position = self.images[self.id_].body.position[0], 0

            if self.images[self.id_].body.position[1] <= 0 and self.speed[1] < 0:
                self.images[self.id_].body.position = self.images[self.id_].body.position[0], self.screen.height / 2


class Sheet:

    """
        sprite_sheet_data = {
        "width": 359,
        "height": 261,
        "default": (0, 0, 359, 261),
        "player": (32, 19, player_wh[0], player_wh[1]),
        "enemy1": (255, 118, e_type1_wh[0], e_type1_wh[1]),
        "enemy2": (254, 117, e_type2_wh[0], e_type2_wh[1])
    }

    sprite_sheet = Sheet("img/spaceWarAssets.png", sprite_sheet_data, color_key=(0, 0, 0)
    # color_key -> make color transparent
    player_sprite = Sprite(screen, "player")  # img

    img_file = sprite_sheet.make_new_sheet_img("player", img_size=0.3)

    player_sprite.make_sprite(type_="img", width=player_wh[0], height=player_wh[1], file=img_file, img_size=0.3),
    """

    def __init__(self, file, sprite_sheet_info, color_key=(0, 0, 0)):
        self.sprite_sheet_info = sprite_sheet_info
        self.color_key = color_key
        self.full_sheet_img = file
        if type(file) == str:
            self.full_sheet_img = pygame.image.load(str(file)).convert_alpha()

    def make_new_sheet_img(self, name, anker=(0, 0), img_size=1):
        _1, _2, width, height = self.sprite_sheet_info[name]
        sprite = pygame.Surface((width, height))
        sprite.set_colorkey(self.color_key)
        sprite.blit(self.full_sheet_img, anker, self.sprite_sheet_info[name])
        if img_size != 1:
            return pygame.transform.scale(sprite, (round(width * img_size), round(height * img_size)))
        return sprite


class Animation(Sheet, Sprite, ABC):  # extension for Sprite enables animated Sprite

    """
        sprite_sheet_data = {
        "0": (0, 0, 49, 49),
        "1": (51, 0, 49, 49),
        "2": (101, 0, 49, 49),
        "3": (151, 0, 49, 49),
        "4": (201, 0, 49, 49),
        "5": (251, 0, 49, 49),
    }

    sprite_sheet_data2 = {
        "0": (0, 51, 49, 49),
        "1": (51, 51, 49, 49),
        "2": (101, 51, 49, 49),
        "3": (151, 51, 49, 49),
        "4": (201, 51, 49, 49),
        "5": (251, 0, 49, 49),
    }
    alim1 = Animation(screen=screen, name="test", file="img/testAlim1.png", sprite_sheet_info=sprite_sheet_data,
                      color_key=(255, 255, 255))

    alim1.make_new_animation("a2", sprite_sheet_data2, size=4)

    alim1.make_new_animation("a1", sprite_sheet_data, size=4)
    alim1.debug_img_rot_draw = True
    alim1.load_animation("a1")
    alim1.make_sprite("img", elasticity=1,
                      position=(600, 400), physics=True, velocity=(20, 10),
                      file=alim1.stos[alim1.ac_alim][0][1])

    alim1.add_to_space(space)

    # like a normal sprite

    # self.next_step(FPS) must pe in main loop FPS to play the animation

    """

    def __init__(self, screen, name, file, sprite_sheet_info=None, def_cord="bl", color_key=(0, 0, 0)):
        Sheet.__init__(self, file, sprite_sheet_info, color_key)
        Sprite.__init__(self, screen, name + "|Animation", def_cord)
        self.step = 0
        self.keys = []
        self.stos = {"default": []}
        self.ac_alim = "default"
        self.pastime = 0

    def make_new_animation(self, name, sprite_sheet_info, size=1, anker=(0, 0)):
        self.sprite_sheet_info = sprite_sheet_info
        self.keys = list(self.sprite_sheet_info.keys())
        self.stos[name] = self.hot_lade(size, anker)
        self.load_animation(name)

    def load_animation(self, name):
        self.ac_alim = name

    def hot_lade(self, size, anker=(0, 0)):
        sto = {}
        for key, value in enumerate(self.keys):
            sto[key] = [value, self.make_new_sheet_img(value, anker=anker, img_size=size)]
        return sto

    def next_step(self, fps):
        if time.time() - self.pastime >= 1 / fps:
            if self.step >= len(self.stos[self.ac_alim]):
                self.step = 0
            self.img = self.stos[self.ac_alim][self.step][1]
            self.step += 1
            self.pastime = time.time()


class Mouse:  # for ui coming in future

    def __init__(self, screen, img_s: list or None = None):
        if img_s is None:
            mouse = Sprite(screen, "Mouse")
            mouse.make_sprite("rect", 0, 10, 10)
            self.mouse = mouse, mouse
        else:
            mouse = Sprite(screen, "Mouse")
            mouse.make_sprite("img", 0, 10, 10, file=img_s[0])

            mouse1 = Sprite(screen, "Mouse")
            mouse1.make_sprite("img", 0, 10, 10, file=img_s[1])
            self.mouse = mouse, mouse1
            pygame.mouse.set_visible(False)
        self.screen = screen

    def mouse_get_sprite(self):
        return self.mouse[0]

    def show_m(self, click: bool = False):
        self.mouse[0].body.position = pygame.mouse.get_pos()
        if self.mouse[0].type_ == "img":
            self.mouse[1].body.position = pygame.mouse.get_pos()
            if click:
                self.mouse[1].draw_func()
            else:
                self.mouse[0].draw_func()


class Screen:
    def __init__(self, width: int = 800, height: int = 600,
                 title: str = ""):
        surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.width = width
        self.height = height
        self.titel = title
        self.surface = surface


class Text:

    def __init__(self, screen: Screen):
        pygame.font.init()
        self.screen = screen.surface
        self.font: pygame.font.SysFont or None = None
        self.init = False

    def init_font(self, size=30, text_type='Arial.ttf'):
        self.font = pygame.font.SysFont(text_type, size)
        self.init = True

    def show(self, text, xy, color=(0, 0, 0)):
        assert self.init, "Pleas Init Font first, Text.init_font(size, systemFontName)"
        self.screen.blit(self.font.render(str(text), False, color), xy)


class Design:
    pass


def parser(point, screen_height, def_cord="tl"):
    if def_cord == "tl":
        return round(point[0]), screen_height - round(point[1])
    # if def_cord == "bl":
    return round(point[0]), round(point[1])


clock = pygame.time.Clock()
space = pymunk.Space()
