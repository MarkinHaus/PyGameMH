import math
import time
from abc import ABC

import pygame
from typing import List

from util.Color import name_to_list

import pymunk

"""
class Sprite:  # blueprint for super class handles all game objects to print and pymunk simulation
    def __init__(self, screen: Screen, name: str, def_cord: str = "bl"):

        
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


self.screen: Screen
self.name: str
self.def_cord: str
self.dt: int 

# vars for all objects
self.type_: str 
self.collisions_level: int 
self.color: tuple
self.draw_func: python function  # draw the sprite to screen

# for type = line and rect
self.width: float
self.height: float

# for type = line
self.point1: tuple or list or None
self.point2: tuple or list or None

# for type = img
self.img: pygame.image
self.file: str
self.img_size: int

# for type = circle
self.radius: float

self.aa_lines_list: list
self.aa_lines_list_ob: List["Sprite"]
self.is_closed: bool

# physics stuff
self.physics: bool
self.body_type: int
self.body: pymunk.Body
self.shape: pymunk.shapes
self.elasticity: float
self.density: float
self.friction: float
self.auto_angel: list[int, bool]

# set behavior
self.do_slow_down: bool
self.debug_img_rot_draw: bool  # type specific img
self.kill: bool

__str__(self) -> str:
do_kill(self) -> bool:  # allows killing self if future necessary clear memory
set_color(self, color: str or list or tuple, color_keys: list = ()):  # convert color for pygame using The Color module
add_to_space(self, space_: pymunk.Space):  # adds shape and body to simulation space for pymunk
set_shape_props(self):  # set extra physic props to object
if_of_screen(self):  # test if position of object is not in screen ( you can't see it any loger )
make_sprite(self,
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
    color_for_aa_line: list or tuple = (), new_body=True) -> Sprite:
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

draw_func():
rect_(self):
debug_draw_rect(self, color: list or tuple or str=(150, 150, 150)):  # draw a rect from top left to bottem right ( is not the hitbox)
speed_convert_img(self):
set_do_slow_down(self, set_: bool=False):
slow_down(self, friction: float):  # self.do_slow_down must be True body slows down
rotate(self, angle_rate: float, do: bool=False):  # set rotation speed if do is True else set slowdown rate if do is False
do_rotate(self, f: float=0.1):  # rotate object by self.rotate(...) must bee called in main game loop
img_(self):
circle_(self):
line_(self):
aalines(self, collisions_for_sep_aa_line: list, color_for_aa_line: list):
@classmethod
aa_lin(cls, aa_lines: Sprite, id: int, start_point: tuple or list, end_point: tuple or list, collisions_level: int, color: tuple or list or str=(0, 0, 0)) -> Sprite:


class Map:

__init__(self, screen: Screen, type_: str, color: tuple or list or str=(0, 0, 0)):  # types = statick statick-img dynamic-img

self.images: dict
self.camera_position: list
self.loop: list
self.type: str
self.color: tuple or list or str
self.screen: Screen
self.color_key: tuple or list
self.id_: int
self.speed: list

lode_new(self, id_: int):
load_statick_img(self, id_: int, file: str or pygame.image):
load_dynamic_img(self, id_: int, file: str or pygame.image, loop: tuple or list=(1, 0)):
load_map(self, map_: list, spec: dict, id_: int):  # map_ = ["x", "x", "x", "/n",
    #                                                            "x", "x", "x", "/n",
    #                                                            "x", "x", "x", "/n"]
    # spec = {"spec": {"map": (width, height), "wh": ( width, height)}, "x": img}
camera_to_pos(self, pos: tuple or list):
draw(self):


class Sheet:


__init__(self, file: str or pygame.image, sprite_sheet_info: dict, color_key: tuple or list=(0, 0, 0)):

self.sprite_sheet_info: dict
self.color_key: tuple or list
self.full_sheet_img: pygame.image

make_new_sheet_img(self, name: str, anker: tuple or list=(0, 0), img_size: int=1) -> pygame.Surface:


class Animation(Sheet, Sprite, ABC):  # extension for Sprite enables animated Sprite

__init__(self, screen: Screen, name: str, file: str or pygame.sprite, sprite_sheet_info: dict or None, def_cord: str, color_key: tuple or list):

#Sheet.__init__(self, file, sprite_sheet_info, color_key)
#Sprite.__init__(self, screen, name + "|Animation", def_cord)

self.step: int
self.keys: list
self.stos: dict
self.ac_alim: str
self.pastime: int

make_new_animation(self, name: str, sprite_sheet_info: dict, size: int=1, anker: tuple or list=(0, 0)):
load_animation(self, name: str):
hot_lade(self, size: float, anker: tuple or list=(0, 0)) -> dict:
next_step(self, fps: float):



class Screen:

__init__(self, width: int = 800, height: int = 600,title: str = ""):

self.width: int
self.height: int
self.titel: str
self.surface: pygame.display


class Text:

__init__(self, screen: Screen):

self.screen: Screen
self.font: int
self.init: bool

init_font(self, size: int, text_type: str='Arial.ttf'):
show(self, text: str, xy: tuple or list, color: tuple or list=(0, 0, 0)):

"""

