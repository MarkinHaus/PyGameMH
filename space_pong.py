from util.MGameM import Screen, Sprite, Text, Mouse, Physics, clock  # import custom
import random
import pygame
import time


def functional():
    # Open a Window
    screen = Screen(width=862, height=674, background='black')

    # init Sprites blueprint
    player_sprites = []
    game_pad_height = 30
    game_pad_width = 120
    player = Sprite(screen, "player")  # rect
    ball = Sprite(screen, "circle")  # ball

    # ball starting conditions
    ball.fx(0)
    ball.fy(2)

    # players starting conditions
    of_y = 10
    player.x = screen.width / 2 - game_pad_width / 2
    player.y = screen.height - game_pad_height - of_y

    ball.x = screen.width / 2
    ball.y = screen.height / 2 - 200

    # construct sprites

    player.make_sprite("rect", -1, game_pad_width, game_pad_height, color="blue")

    ball.make_sprite("circle", 1, radius=10, color="white")

    # add sprites to sprites array
    player_sprites += [player, ball]
    sprites = []

    # top

    em_sprites = list(range(14))

    def helper_1(num):
        s = Sprite(screen, f"E{num}")  # rect
        s.make_sprite("rect", 1, 50, 30, color="white")
        s.x = 10 * num + 50 * num + 20
        s.y = 100
        return s

    sprites = list(map(helper_1, em_sprites))

    # init Text

    text = Text(screen)

    # init Mouse
    mouse = Mouse(screen, None)

    # init player Life
    points = 0

    run = True
    while run:

        screen.surface.fill(screen.background)

        def f1(sprite):
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

                if event.key == pygame.K_a:
                    player.fx(-4)
                if event.key == pygame.K_d:
                    player.fx(4)

        Physics.collision(player_sprites)

        if Physics.border_top_collision(ball):
            ball.my *= -1

        if Physics.border_left_collision(ball, screen):
            ball.mx *= -1

        if Physics.border_right_collision(ball):
            ball.mx *= -1

        if Physics.border_left_collision(player, screen):
            player.mx *= -0.5
            player.x = screen.width - (of_y / 2 + player.width )

        if Physics.border_right_collision(player):
            player.mx *= -0.5
            player.x = of_y / 2

        if Physics.border_bottom_collision(ball, screen):
            ball.x = screen.width / 2
            ball.y = screen.height / 2 - 200

        if bool(ball.collision_list):
            if ball.collision_list[0][0] == player:
                ball.my *= -1
                ball.fx(player.mx + ball.mx)
        # t1 = time.time()
        list(map(f1, player_sprites))
        # tm_ += 1
        # tm += (time.time()-t1)/tm_

        #if player.collision_list:
        #    print("in")
        #    ball.my *= -1

        # t1 = time.time()
        for sprite in sprites:
            sprite.move(dt)
            sprite.draw_func()
            sprite.collision_func(ball)
            if len(sprite.collision_list) >= 1:
                sprite.collision_list = []
                sprites.remove(sprite)
                print(sprite.name)
                ball.my *= -1
        # tf_ += 1
        # tf += (time.time()-t1)/tf_

        text.show(f"Points {points}", (20 - 150, 30), (255, 255, 255))

        if len(sprites) <= 0:
            text.show(f"END {points}", (20 - 150, 30), (255, 255, 255))
            pygame.time.wait(1000)

        # for p in cp:
        #     pygame.draw.rect(screen.surface, (255, 0, 255), (p[0], p[1], 2, 2))

        mouse.show_m(False)
        pygame.display.update()


if __name__ == '__main__':
    # starting Game
    functional()
