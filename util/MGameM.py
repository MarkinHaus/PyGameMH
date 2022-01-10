import pygame

from util.Color import name_to_list
from math import sqrt


class Sprite:
    def __init__(self, screen, name: str):
        self.screen: Screen = screen
        self.name = name
        self.type_: str = ""
        self.width: float = 0
        self.height: float = 0
        self.x: float = 0
        self.y: float = 0

        self.mx: float = 0
        self.my: float = 0

        self.collisions_level: int = 0
        self.collision_list: list = []
        self.color: tuple = (0, 0, 0)
        self.border_offset: int = 5
        self.draw_func = None
        self.collision_func = None
        self.img: pygame.image = None
        self.rect: pygame.Rect = pygame.Rect(0, 0, 0, 0)

        self.file: str = ""
        self.img_size: int = 1
        self.radius: float = 0

    def __str__(self):
        return f"Type: {self.type_}, width {self.width}, height {self.height}, x {self.x}, y {self.y} \n"

    def set_color(self, color: str or list):
        self.color = color
        if type(color) == str:
            self.color = name_to_list(color)

    def make_sprite(self, type_: str, collisions_level: int, width: float = 0, height: float = 0, radius: float = 0,
                    color: str or list or None = None, file: str or None = None, img_size: int = 1) -> None:
        self.set_color(color)
        if not self.type_:
            self.type_ = type_
        self.radius: float = radius
        self.width = width
        self.height = height
        self.collisions_level = collisions_level
        self.file = file
        self.img_size = img_size

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
        if type_ == "lines":
            self.lines_()
        if type_ == "aaline":
            self.aalines()

    def move(self, dt: float):
        self.x += self.mx * dt
        self.y += self.my * dt
        self.rect = pygame.Rect((self.x, self.y, self.width, self.height))
        # self.rect.move_ip(int(self.x), int(self.y))

    def fx(self, x: int):
        self.mx = x

    def fy(self, y: int):
        self.my = y

    def add_col_sprite(self, sprite, point: list):
        self.collision_list.append([sprite, point])

    def rect_(self):
        self.rect = pygame.Rect((self.x, self.y, self.width, self.height))

        def draw_func():
            pygame.draw.rect(self.screen.surface, self.color, self.rect)

        def collision_func(sprite):
            if self.collisions_level == sprite.collisions_level or sprite.collisions_level == -1:
                if sprite.type_ in ["rect", "img"]:
                    if pygame.Rect.colliderect(sprite.rect, self.rect):
                        self.add_col_sprite(sprite, [self.x - self.width / 2, self.y - self.height / 2])
                elif sprite.type_ == "circle":
                    x_l = list(range(0, int(self.width)))
                    y_l = list(range(0, int(self.height)))
                    outline_rect = list(map(lambda x: [x, self.y], x_l)) + list(map(lambda y: [self.x, y], y_l))
                    # compute_dist
                    g = list(map(lambda x: sqrt((sprite.x - x[0]) ** 2 +
                                                (sprite.y - x[1]) ** 2), outline_rect))
                    if min(g) <= sprite.radius:
                        self.add_col_sprite(sprite, outline_rect[g.index(min(g))])
                else:
                    raise NotImplementedError(f"type {sprite.type_} not implemented")

        if not self.draw_func:
            self.draw_func = draw_func
        if not self.collision_func:
            self.collision_func = collision_func

    def img_(self):

        self.img = pygame.image.load(str(self.file)).convert_alpha()

        if not self.width:
            self.width = self.img.get_width()

        if not self.height:
            self.height = self.img.get_height()

        if self.img_size != 1:
            self.img = pygame.transform.scale(self.img, self.img_size)

        def draw_func():
            self.screen.surface.blit(self.img, (self.x, self.y))

        if not self.draw_func:
            self.draw_func = draw_func

        self.make_sprite('rect', self.collisions_level, width=self.width, height=self.height)

    def circle_(self):

        def draw_func():
            pygame.draw.circle(self.screen.surface, self.color, (self.x, self.y), self.radius)

        def collision_func(sprite):
            if self.collisions_level == sprite.collisions_level or sprite.collisions_level == -1:
                if sprite.type_ == "circle":
                    dist = sqrt((self.x - sprite.x) ** 2 + (self.y - sprite.y) ** 2)
                    if dist <= self.radius + sprite.radius:
                        self.add_col_sprite(sprite, [sprite.x - sprite.width / 2, sprite.y - sprite.height / 2])
                elif sprite.type_ in ["rect", "img"]:
                    x_l = list(range(int(sprite.x), int(sprite.x) + int(sprite.width)))
                    y_l = list(range(int(sprite.y), int(sprite.y) + int(sprite.height)))
                    outline_rect = list(map(lambda x: [x, sprite.y], x_l)) + list(map(lambda y: [sprite.x, y], y_l)) + \
                                   list(map(lambda x: [x, sprite.y + sprite.height], x_l)) + \
                                   list(map(lambda y: [sprite.x + sprite.width, y], y_l))
                    # compute_dist
                    g = list(map(lambda x: sqrt((self.x - x[0]) ** 2 +
                                                (self.y - x[1]) ** 2), outline_rect))
                    for p in outline_rect:
                        pygame.draw.rect(self.screen.surface, (255, 0, 255), (p[0], p[1], 2, 2))

                    if min(g) <= self.radius:
                        self.add_col_sprite(sprite, outline_rect[g.index(min(g))])
                else:
                    raise NotImplementedError(f"type {sprite.type_} not implemented")

        if not self.draw_func:
            self.draw_func = draw_func
        if not self.collision_func:
            self.collision_func = collision_func

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
        self.img = Sprite(screen, "Background")
        self.img.make_sprite("img", -1, wh[0], wh[1], file=image_n, img_size=img_size)
        self.img2 = Sprite(screen, "Background2")
        self.img2.make_sprite("img", -1, wh[0], wh[1], file=image_n, img_size=img_size)
        self.screen = screen

        self.x = 0
        self.y = 0

    def show(self, move_x: bool = False, speed_x: int = 15, move_y: bool = False, speed_y: int = 15, dt: float = 1):
        if move_x:
            self.y = 0
            self.x += speed_x
            self.img.x = self.x
            self.img.move(dt)

            self.img2.x = self.x - self.img.width
            self.img2.move(dt)

            if self.x >= self.img.width:
                self.x = 0
            if self.x < 0:
                self.x = self.img.width
        else:
            self.img.x = 0
            self.img2.x = self.img.x

        if move_y:
            self.x = 0
            self.y += speed_y
            self.img.y = self.y
            self.img.move(dt)

            self.img2.y = self.y - self.img.height
            self.img2.move(dt)

            if self.y >= self.img.height:
                self.y = 0
            if self.y < 0:
                self.y = self.img.height
        else:
            self.img.y = 0
            self.img2.y = self.img.y
        self.screen.surface.blit(self.img.img, (self.x, self.y))
        self.screen.surface.blit(self.img2.img, (self.img2.x, self.img2.y))


class Mouse:

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
        mx, my = pygame.mouse.get_pos()
        self.mouse[0].fx(mx)
        self.mouse[0].fy(my)
        if self.mouse[0].type_ == "img":
            self.mouse[1].fx(mx)
            self.mouse[1].fy(my)
            if click:
                self.mouse[1].draw_func()
            else:
                self.mouse[0].draw_func()


class Screen:
    def __init__(self, width: int = 800, height: int = 600, background: str = 'black', title: str = ""):
        if type(background) == str:
            background = name_to_list(background)

        surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.width = width
        self.height = height
        self.background = background
        self.titel = title
        self.surface = surface


class Text:

    def __init__(self, screen: Screen):
        pygame.font.init()
        self.screen = screen.surface

    def show(self, text, xy, color=(0, 0, 0), size=30, text_type='Arial.ttf'):
        self.screen.blit(pygame.font.SysFont(text_type, size)
                         .render(str(text), False, color), xy)


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
        # sprite.mx *= -1
        return sprite.x + sprite.width >= screen.width

    @staticmethod
    def border_right_collision(sprite: Sprite):
        # sprite.mx *= -1
        return sprite.x <= 0

    @staticmethod
    def border_top_collision(sprite: Sprite):
        # sprite.my *= -1
        return sprite.y <= 0

    @staticmethod
    def border_bottom_collision(sprite: Sprite, screen: Screen):
        # sprite.my *= -1
        return sprite.y + sprite.height >= screen.height

    @staticmethod
    def border_collision(sprite, screen: Screen):
        return [Physics.border_left_collision(sprite=sprite, screen=screen),
                Physics.border_right_collision(sprite=sprite),
                Physics.border_top_collision(sprite=sprite),
                Physics.border_bottom_collision(sprite=sprite, screen=screen)]

    @staticmethod
    def collision(all_sprite, type_="simpel"):
        if type_ == "simpel":
            for sprite in all_sprite:
                sprite.collision_list = []
                for sprite_ in all_sprite:
                    if sprite != sprite_:
                        sprite.collision_func(sprite_)
        else:
            raise NotImplementedError


clock = pygame.time.Clock()
