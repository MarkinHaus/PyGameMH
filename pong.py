from util.MGameM import Screen, Sprite, Text, Mouse, Physics, clock  # import custom
import random
import pygame


def functional():
    # Open a Window
    screen = Screen(width=1236, height=512, background='black', title="Pong")

    # init Sprites blueprint
    sprites = []
    game_pad_width = 30
    game_pad_height = 120
    sprite1 = Sprite(screen, "player1")  # rect
    sprite2 = Sprite(screen, "player2")  # rect
    sprite3 = Sprite(screen, "circle")  # ball

    # ball starting conditions
    sprite3.fx(4)
    sprite3.fy(0)

    # players starting conditions
    of_x = 10
    sprite1.x = 10
    sprite1.y = screen.height / 2 - game_pad_width - of_x

    sprite2.x = screen.width - game_pad_width - of_x
    sprite2.y = screen.height / 2 - game_pad_width - of_x

    sprite3.x = screen.width / 2
    sprite3.y = screen.height / 2

    # construct sprites
    sprite1.make_sprite("rect", 1, game_pad_width, game_pad_height, color="blue")
    sprite2.make_sprite("rect", 1, game_pad_width, game_pad_height, color="white")
    sprite3.make_sprite("circle", 1, radius=10, color="white")

    # add sprites to sprites array
    sprites += [sprite1, sprite2, sprite3]

    # init Text
    text = Text(screen)

    # init Mouse
    mouse = Mouse(screen, None)

    cp = []

    # init player Life
    life_pl1 = 3
    life_pl2 = 3

    # tm = 0
    # tf = 0
    # tm_ = 0
    # tf_ = 0

    run = True
    while run:

        screen.surface.fill(screen.background)

        def f(sprite):
            sprite.move(dt)
            sprite.draw_func()

        # using clock to cap fps
        dt = clock.tick(25) / 10
        # dt control movement speed

        # starting event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

                # print(f"tf = {tf}, tm = {tm} m/f = {tm/tf}")

                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:

                # if game is not over
                if not life_pl1 <= 0 and not life_pl2 <= 0:

                    if event.key == pygame.K_w:
                        sprite1.fy(-4)

                    if event.key == pygame.K_s:
                        sprite1.fy(4)

                    if event.key == pygame.K_UP:
                        sprite2.fy(-4)

                    if event.key == pygame.K_DOWN:
                        sprite2.fy(4)

        Physics.collision(sprites)

        if Physics.border_top_collision(sprite1):
            sprite1.my *= -1

        if Physics.border_bottom_collision(sprite1, screen):
            sprite1.my *= -1

        if Physics.border_top_collision(sprite2):
            sprite2.my *= -1

        if Physics.border_bottom_collision(sprite2, screen):
            sprite2.my *= -1

        if Physics.border_top_collision(sprite3):
            sprite3.my *= -1

        if Physics.border_bottom_collision(sprite3, screen):
            sprite3.my *= -1

        if Physics.border_left_collision(sprite3, screen):
            screen.surface.fill(sprite1.color)
            life_pl2 -= 1
            sprite3.x = screen.width / 2
            sprite3.y = screen.height / 2
            sprite3.fy(random.randint(-2, 2))

        if Physics.border_right_collision(sprite3):
            screen.surface.fill(sprite2.color)
            life_pl1 -= 1
            sprite3.x = screen.width / 2
            sprite3.y = screen.height / 2
            sprite3.fy(random.randint(-2, 2))

        # t1 = time.time()
        list(map(f, sprites))
        # tm_ += 1
        # tm += (time.time()-t1)/tm_

        # t1 = time.time()
        # for sprite in sprites:
        #     sprite.move(dt)
        #     sprite.draw_func()
        # tf_ += 1
        # tf += (time.time()-t1)/tf_

        text.show(f"PL2 Life {life_pl2}", (screen.width - 150, 30), (255, 255, 255))
        text.show(f"PL1 Life {life_pl1}", (20, 30), (255, 255, 255))

        if bool(sprite3.collision_list):
            if sprite3.collision_list[0][0] == sprite2:
                sprite3.x = sprite2.x - (game_pad_width + of_x + 1)
                sprite3.fy(sprite2.my * (4 - life_pl2) / 2)
                sprite3.mx *= -1
            # cp.append((sprite3.x, sprite3.y))
            # cp.append((sprite3.collision_list[0][1]))
            sprite3.set_color(random.choice(["red", "blue", "yellow", "purple", "azul", "white"]))

        if bool(sprite3.collision_list):
            if sprite3.collision_list[0][0] == sprite1:
                sprite3.x = sprite1.x + (game_pad_width + of_x + 1)
                sprite3.fy(sprite1.my * (4 - life_pl1) / 2)
                sprite3.mx *= -1
            # cp.append((sprite3.x, sprite3.y))
            # cp.append((sprite3.collision_list[0][1]))
            sprite3.set_color(random.choice(["red", "blue", "yellow", "purple", "azul", "white"]))

        if life_pl1 <= 0:
            sprite1.my *= -0.25
            sprite2.my *= -0.25
            text.show(f"!!!PL2 WIN!!! Starting in {abs(int(-life_pl1 * 100 / 250))}",
                      (screen.width / 2 - 100, screen.height / 2 - 50), (255, 255, 255))
            sprite3.x = screen.width / 2
            sprite3.y = screen.height / 2
            if life_pl1 == 0:
                life_pl1 = -250
            life_pl1 += 1
            if life_pl1 == -1:
                life_pl1 = 3
                life_pl2 = 3
                sprite3.fx(random.randint(-2, 2))
                sprite3.fy(random.randint(-2, 2))

        if life_pl2 <= 0:
            sprite1.my *= -0.25
            sprite2.my *= -0.25
            text.show(f"!!!PL1 WIN!!! Starting in {abs(int(-life_pl2 * 100 / 250))}",
                      (screen.width / 2 - 100, screen.height / 2 - 50), (255, 255, 255))
            sprite3.x = screen.width / 2
            sprite3.y = screen.height / 2
            if life_pl2 == 0:
                life_pl2 = -250
            life_pl2 += 1
            if life_pl2 == -1:
                life_pl1 = 3
                life_pl2 = 3
                sprite3.fx(random.randint(-2, 2))
                sprite3.fy(random.randint(-2, 2))

        # for p in cp:
        #     pygame.draw.rect(screen.surface, (255, 0, 255), (p[0], p[1], 2, 2))

        mouse.show_m(False)
        pygame.display.update()


if __name__ == '__main__':
    # starting Game
    functional()
