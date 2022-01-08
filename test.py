import pygame
import random
from util.MGameM import Screen, Sprite, Text, Mouse, Background, clock, Physics

if __name__ == '__main__':

    # Ein Fenster öffnen

    screen = Screen(width=1650, height=720, background='black')

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
    for i in range(1000):
        dt = clock.tick(25) / 10
        p = i * 100 / 1000
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
    pygame.quit()
