import pygame
import random
from util.MGameM import Screen, Sprite, Text, Mouse, Background, clock, Physics
import sys


def average(dt_l_):
    return sum(dt_l_) / len(dt_l_)


if __name__ == '__main__':

    print('Python %s on %s' % (sys.version, sys.platform))

    # Ein Fenster öffnen

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
    step = "0"
    coll_count = 0
    fps = 60
    fs = ""
    dt_l = []
    for i in range(1000):
        dt = clock.tick(fps) / 10
        p = i * 100 / 1000
        if p > 0.5:
            dt_l.append(dt)
        print(f"{p}% step {step} | 3 dt: {dt} ")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.surface.fill(screen.background)

        if p > 0:
            step = f"testing Text size : {int(i / 10)} 1"
            text.show(f"TeStInG ´tEx*t {p}%", (screen.width / 2 - 200, screen.height / 2), (255, 255, 255), i)

        if p > 10:
            step = f"testing background 2"
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

    print(fs)
    print(f"Done 2 : Performance withe FPS {fps}, {max(dt_l) - average(dt_l):.3f}, max = {max(dt_l):.2f},"
          f" avg = {average(dt_l):.2f}")
    pygame.quit()


"""
# i7-6800k GTX 1080
Done 1 Performance withe FPS 600, 1.100, max = 2.30, avg = 1.20,
Done 2 Performance withe FPS 600, 2.629, max = 4.10, avg = 1.47

Done 1 : Performance withe FPS 60, 1.198, max = 2.90, avg = 1.70,
Done 2 : Performance withe FPS 60, 1.396, max = 3.10, avg = 1.70

Done 1 : Performance withe FPS 25, 0.049, max = 4.10, avg = 4.05,
Done 2 : Performance withe FPS 25, 0.050, max = 4.10, avg = 4.05

Done 1 : Performance withe FPS 60, 7.580, max = 10.10, avg = 2.52,
Done 2 : Performance withe FPS 60, 11.107, max = 14.40, avg = 3.29
"""