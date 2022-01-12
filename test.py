import pygame
import random
from util.MGameM import Screen, Sprite, Text, Mouse, Background, clock, Physics
import time
import sys
import cProfile, pstats, io


def profile(fnc):
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue()[:2000])
        return retval

    return inner


def average(dt_l_):
    return sum(dt_l_) / len(dt_l_)


@profile
def live():
    print('Python %s on %s' % (sys.version, sys.platform))

    # Open a Window

    screen = Screen(width=1650, height=720, background='black', title=">Test<")

    # init test Background

    background = Background(screen, "img/testBG.png", wh=(1280, 720))

    # init test Mouse

    mouse = Mouse(screen, None)  # ["img/testMG1.png", "img/testMG1.png"])
    sprites = []

    # init test Sprites

    sprite1 = Sprite(screen, "sprite1")  # rect
    sprite2 = Sprite(screen, "sprite2")  # rect
    sprite3 = Sprite(screen, "sprite3")  # rect
    sprite4 = Sprite(screen, "sprite4")  # img

    sprite1.fx(random.randint(-6, 6))
    sprite1.fy(random.randint(-6, 6))

    sprite2.fx(random.randint(-6, 6))
    sprite2.fy(random.randint(-6, 6))

    sprite3.fx(random.randint(-6, 6))
    sprite3.fy(random.randint(-6, 6))

    sprite4.fx(random.randint(-6, 6))
    sprite4.fy(random.randint(-6, 6))

    sprite1.x = random.randint(6, 720)
    sprite1.y = random.randint(6, 720)
    sprite2.x = random.randint(6, 720)
    sprite2.y = random.randint(6, 720)
    sprite3.x = random.randint(6, 720)
    sprite3.y = random.randint(6, 720)
    sprite4.x = random.randint(6, 720)
    sprite4.y = random.randint(6, 720)

    sprite1.make_sprite("rect", -1, 80, 80, color="Blue")
    sprite2.make_sprite("rect", 1, 80, 80, color="Red")
    sprite3.make_sprite("circle", 1, radius=10, color="Green")
    sprite4.make_sprite("img", 1, 203, 46, file="img/testIB.png")

    sprites += [sprite1, sprite2, sprite3, sprite4]

    # init test Text:

    text = Text(screen)
    text.init_font(20)
    # main loop
    coll_count = 0
    fps = 10
    fs = ""
    dt_l = []
    for i in range(500):
        p = i * 100 / 500
        # print(f"{p}% step {step} | 3 dt: {dt} ")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.surface.fill(screen.background)

        if p > 0:
            if p % 5 == 0 and p < 20:
                text.init_font(size=i)
            text.show(f"TeStInG ´tEx*t {p}%", (screen.width / 2 - 200, screen.height / 2), (255, 255, 255))

        if p > 10:
            move_x = False
            move_y = False
            speed_x = 150
            speed_y = 150
            if p > 15:
                move_x = True
                move_y = False
                speed_x = 150
                speed_y = 150
            if p > 20:
                move_x = True
                move_y = False
                speed_x = - 150
                speed_y = 150
            if p > 30:
                move_x = False
                move_y = True
                speed_x = 150
                speed_y = -150
            if p > 35:
                move_x = False
                move_y = True
                speed_x = 150
                speed_y = 150
            if p > 40:
                move_x = False
                move_y = False
                speed_x = 150
                speed_y = 150
            background.show(move_x=move_x, speed_x=speed_x, move_y=move_y, speed_y=speed_y)
            if p < 50:
                text.show(f"Testing background {i * 100 / 500}%", (screen.width / 2, 45),
                          (255, int(255 % i / 255), 255))

        if p > 50:
            step = f"testing sprite 3"

            Physics.collision(sprites)

            def f(sprite):
                sprite.move(1)
                sprite.draw_func()

                if Physics.border_left_collision(sprite, screen):
                    sprite.mx *= -1

                if Physics.border_right_collision(sprite):
                    sprite.mx *= -1

                if Physics.border_top_collision(sprite):
                    sprite.my *= -1

                if Physics.border_bottom_collision(sprite, screen):
                    sprite.my *= -1

                if sprite.collision_list:
                    sprite4.x = random.randint(6, 720)
                    sprite4.y = random.randint(6, 720)
                    sprite.set_color(
                        random.choice(["black", "red", "green", "blue", "yellow", "purple", "azul", "white"]))

            list(map(f, sprites))

            text.show(f"Testing sprite collision {p}%", (0, 80), (255, 255, 255))

        mouse.show_m(False)
        pygame.display.update()
    pygame.quit()


def st(cap=True):

    # Open a Window

    screen = Screen(width=1650, height=720, background='black', title=">Test<")

    # init test Background

    background = Background(screen, "img/testBG.png", wh=(1280, 720))

    # init test Mouse

    mouse = Mouse(screen, None)  # ["img/testMG1.png", "img/testMG1.png"])
    sprites = []

    # init test Sprites

    sprite1 = Sprite(screen, "sprite1")  # rect
    sprite2 = Sprite(screen, "sprite2")  # rect
    sprite3 = Sprite(screen, "sprite3")  # rect
    sprite4 = Sprite(screen, "sprite4")  # img

    sprite1.fx(random.randint(-6, 6))
    sprite1.fy(random.randint(-6, 6))
    sprite2.fx(random.randint(-6, 6))
    sprite2.fy(random.randint(-6, 6))
    sprite3.fx(random.randint(-6, 6))
    sprite3.fy(random.randint(-6, 6))
    sprite4.fx(random.randint(-6, 6))
    sprite4.fy(random.randint(-6, 6))

    sprite1.x = random.randint(6, 720)
    sprite1.y = random.randint(6, 720)
    sprite2.x = random.randint(6, 720)
    sprite2.y = random.randint(6, 720)
    sprite3.x = random.randint(6, 720)
    sprite3.y = random.randint(6, 720)
    sprite4.x = random.randint(6, 720)
    sprite4.y = random.randint(6, 720)

    sprite1.make_sprite("rect", -1, 80, 80, color="Blue")
    sprite2.make_sprite("rect", 1, 80, 80, color="Red")
    sprite3.make_sprite("circle", 1, radius=10, color="Green")
    sprite4.make_sprite("img", 1, 203, 46, file="img/testIB.png")

    sprites += [sprite1, sprite2, sprite3, sprite4]

    # init test Text:

    text = Text(screen)

    # main loop
    fps = 25
    turns = 1000
    fs = ""
    dt_l = []
    for i in range(turns):
        dt = clock.tick(fps) / 10 if cap else 1
        p = i * 100 / turns
        if p > 0.5:
            dt_l.append(dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.surface.fill(screen.background)

        if p > 0:
            if p < 10:
                text.init_font(i)
            text.show(f"TeStInG ´tEx*t {p}%", (screen.width / 2 - 200, screen.height / 2), (255, 255, 255))

        if p > 10:
            move_x = False
            move_y = False
            speed_x = 15
            speed_y = 15
            if p > 15:
                move_x = True
                move_y = False
                speed_x = 15
                speed_y = 15
            if p > 20:
                move_x = True
                move_y = False
                speed_x = - 15
                speed_y = 15
            if p > 30:
                move_x = False
                move_y = True
                speed_x = 15
                speed_y = -15
            if p > 35:
                move_x = False
                move_y = True
                speed_x = 15
                speed_y = 15
            if p > 40:
                move_x = False
                move_y = False
                speed_x = 15
                speed_y = 15
            background.show(move_x=move_x, speed_x=speed_x, move_y=move_y, speed_y=speed_y)
            if p < 50:
                text.show(f"Testing background {i * 100 / 500}%", (screen.width / 2, 45),
                          (255, int(255 % i / 255), 255))

                fs = f"Done 1 : Performance withe FPS {fps}, {max(dt_l) - average(dt_l):.3f}, max = {max(dt_l):.2f}," \
                     f" avg = {average(dt_l):.2f},"
        if p > 50:
            step = f"testing sprite 3"

            Physics.collision(sprites)

            def f(sprite):
                sprite.move(dt)
                sprite.draw_func()

                if Physics.border_left_collision(sprite, screen):
                    sprite.mx *= -1

                if Physics.border_right_collision(sprite):
                    sprite.mx *= -1

                if Physics.border_top_collision(sprite):
                    sprite.my *= -1

                if Physics.border_bottom_collision(sprite, screen):
                    sprite.my *= -1

                if sprite.collision_list:
                    sprite4.x = random.randint(6, 720)
                    sprite4.y = random.randint(6, 720)
                    sprite.set_color(
                        random.choice(["black", "red", "green", "blue", "yellow", "purple", "azul", "white"]))

            list(map(f, sprites))

            text.show(f"Testing sprite collision {p}%", (0, 80), (255, 255, 255))

        mouse.show_m(False)
        pygame.display.update()

    dt_l = dt_l[:3]
    if cap:
        print(fs)
        print(f"Done 2 : Performance withe FPS {fps}, {max(dt_l) - average(dt_l):.3f}, max = {max(dt_l):.2f},"
              f" avg = {average(dt_l):.2f} \nfps cap : {fps} \nAchieved fps : {turns/(time.time() - t1)} \nof by : "
              f"{fps - turns/(time.time() - t1)}")
    else:
        print("\n")
        print(f"max fps : {turns/(time.time() - t1)}")
    pygame.quit()


if __name__ == '__main__':

    print('Python %s on %s \n' % (sys.version, sys.platform))

    t1 = time.time()
    st()
    print(f"time {time.time() - t1}")

    t1 = time.time()
    st(False)
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
