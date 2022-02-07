import math

import pygame
import random
from util.MGameM import Screen, Sprite, Text, Mouse, Map, clock, space, Animation
import time
import sys


def average(dt_l_):
    return sum(dt_l_) / len(dt_l_)


def live(cap=True):
    # Open a Window

    screen = Screen(width=1250, height=720, title=">Test<")

    # init test Background

    background_map = Map(screen, "dynamic-img", color=(155, 5, 155))  # statick statick-img dynamic-img
    background_map.load_dynamic_img("img1", "img/testBG.png", (200, 0))
    # init test Mouse

    mouse = Mouse(screen, None)  # ["img/testMG1.png", "img/testMG1.png"])
    sprites = []
    sprite_sheet_data = {
        "0": (1, 0, 49, 49),
        "1": (51, 0, 49, 49),
        "2": (101, 0, 49, 49),
        "3": (151, 0, 49, 49),
        "4": (201, 0, 49, 49),
        "5": (251, 0, 49, 49),
    }

    sprite_sheet_data2 = {
        "0": (1, 51, 49, 49),
        "1": (51, 51, 49, 49),
        "2": (101, 51, 49, 49),
        "3": (151, 51, 49, 49),
        "4": (201, 51, 49, 49),
        "5": (251, 51, 49, 49),
    }
    alim1 = Animation(screen=screen, name="test", file="img/testAlim1.png", sprite_sheet_info=sprite_sheet_data,
                      color_key=(0, 0, 0))

    alim1.make_new_animation("a2", sprite_sheet_data2, size=4)

    alim1.make_new_animation("a1", sprite_sheet_data, size=2)
    alim1.debug_img_rot_draw = True
    alim1.load_animation("a2")
    alim1.make_sprite("img", elasticity=1,
                      position=(600, 400), physics=True, velocity=(20, 10),
                      file=alim1.stos[alim1.ac_alim][0][1])

    alim1.add_to_space(space)

    # init test Sprites

    sprite1 = Sprite(screen, "sprite1")  # rect
    sprite2 = Sprite(screen, "sprite2")  # rect
    sprite3 = Sprite(screen, "sprite3")  # rect
    sprite4 = Sprite(screen, "sprite4")  # img

    sprite1.make_sprite("rect", width=80, height=80, elasticity=1,
                        position=(random.randint(60, 720), random.randint(60, 720)), color="Blue", physics=True,
                        velocity=(random.randint(-100, 100), random.randint(-100, 100)))
    sprite2.make_sprite("rect", width=80, height=80, elasticity=1,
                        position=(random.randint(60, 720), random.randint(60, 720)), color="Red", physics=True,
                        velocity=(random.randint(-100, 100), random.randint(-100, 100)))
    sprite3.make_sprite("circle", radius=20, elasticity=1, position=(random.randint(60, 720), random.randint(60, 720)),
                        color="Green", physics=True, velocity=(random.randint(-10, 10), random.randint(-10, 10)))
    sprite4.make_sprite("img", elasticity=1,
                        position=(400, 400), physics=True, velocity=(20, 10),
                        file="img/testIB.png")

    sprite1.add_to_space(space)
    sprite2.add_to_space(space)
    sprite3.add_to_space(space)
    sprite4.add_to_space(space)

    points = [(25, 25), (25, screen.height - 25), (screen.width - 25, screen.height - 25), (screen.width - 25, 25)]
    border = Sprite(screen, "border_l").make_sprite(type_="box", width=15, aa_lines_list=points,
                                                    collisions_for_sep_aa_line=(2, 4, 3, 4), is_closed=True
                                                    # color_for_aa_line=((255, 255, 0),(255, 0, 255),(255, 0, 0),
                                                    # (255, 0, 0))
                                                    , color="white", elasticity=1,
                                                    physics=False)  # line

    border.add_to_space(space)

    sprites += [sprite1, sprite2, sprite3, sprite4, border]

    # init test Text:

    text = Text(screen)
    text.init_font(20)
    # main loop
    coll_count = 0
    turns = 1000
    fps = 15
    fs = ""
    dt_l = []

    for i in range(turns):
        dt = clock.tick(fps) / 10 if cap else 0.8
        # print(dt)
        space.step(1 / dt)
        p = i * 100 / turns
        # print(f"{p}% step {step} | 3 dt: {dt} ")
        if p > 0.5:
            dt_l.append(dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        background_map.draw()

        if p > 0:
            if p % 5 == 0 and p < 20:
                text.init_font(size=i)
            text.show(f"TeStInG ´tEx*t {p}%", (screen.width / 2 - 200, screen.height / 2), (255, 255, 255))
            if p > 40:
                background_map.speed = [-50, 0]
            # background.show()  # move_x=move_x, speed_x=speed_x, move_y=move_y, speed_y=speed_y)
            if p < 50:
                text.show(f"Testing background {i * 100 / 500}%", (screen.width / 2, 45),
                          (255, int(255 % i / 255), 255))

        if p > 50:
            text.show(f"Testing sprite collision {p}%", (0, 80), (255, 255, 255))

        # background.show()

        def f(sprite):
            sprite.draw_func()

        list(map(f, sprites))

        alim1.next_step(6)
        alim1.draw_func()


        mouse.show_m(False)
        pygame.display.update()

    dt_l = dt_l[:3]
    if cap:
        print(fs)
        print(f"Done : Performance"
              f" avg = {average(dt_l):.2f} \nfps cap : {fps} \nAchieved fps : {turns / (time.time() - t1)} \nof by : "
              f"{fps - turns / (time.time() - t1)}")
    else:
        print("\n")
        print(f"max fps : {turns / (time.time() - t1)}")


if __name__ == '__main__':
    print('Python %s on %s \n' % (sys.version, sys.platform))

    t1 = time.time()
    live()
    print(f"time {time.time() - t1}")

    t1 = time.time()
    live(False)
    print(f"time {time.time() - t1}")

    exit(0)

"""
Done 1 : Performance withe FPS 50, 0.057, max = 2.10, avg = 2.04,
Done 2 : Performance withe FPS 50, 0.000, max = 2.10, avg = 2.10
time 20.69895911216736


Done 1 : Performance withe FPS 25, 0.053, max = 4.10, avg = 4.05,
Done 2 : Performance withe FPS 25, 0.000, max = 4.10, avg = 4.10 
fps cap : 25 
Achieved fps : 24.535677243772177 
of by : 0.4643227562278227
time 40.83750057220459


max fps : 223.82922160998285
time 4.519689083099365


libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
Done 1 : Performance withe FPS 25, 9.718, max = 13.80, avg = 4.08,
Done 2 : Performance withe FPS 25, 0.133, max = 4.20, avg = 4.07 
fps cap : 25 
Achieved fps : 24.164071718536967 
of by : 0.8359316225786877
time 41.41173505783081
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile


max fps : 31.62380955806132
time 31.668455123901367
"""
