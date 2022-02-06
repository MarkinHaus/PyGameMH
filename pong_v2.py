from util.MGameM import Screen, Sprite, Text, Mouse, clock, space, Map
import random
import pygame


def add_ball(screen_):
    bb = Sprite(screen_, f"deed")
    bb.make_sprite(type_="circle", radius=15, color="red", collisions_level=1,
                   position=(screen_.width / 2, screen_.height / 2),
                   velocity=(200 * random.choice([-1, 1]), 200 * random.choice([-1, 1])),
                   mass=10,
                   moment=10,
                   elasticity=1.2, physics=True)
    bb.add_to_space(space)
    return bb


def functional():

    # game modi

    rotation = False
    ball_color = False
    beast_mode = ball_color and False

    # Open a Window -
    screen = Screen(width=1236, height=512, title="Pong")

    background_map = Map(screen, "statick", color=(0, 0, 0))  # statick statick-img dynamic-img

    # init Sprites
    game_pad_width = 30
    game_pad_height = 120
    of_x = 10


    # -------------------player1----------------#
    player1 = Sprite(screen, "player1")  # rect
    player1.make_sprite(type_="rect", width=game_pad_width, height=game_pad_height, color="blue",
                        position=(60, screen.height / 2 - game_pad_width - of_x),
                        velocity=(0, -200),
                        mass=10,
                        moment=1,
                        density=1,
                        elasticity=1.8 if beast_mode else 1, physics=True)

    # -------------------player2----------------#
    player2 = Sprite(screen, "player2")  # rect
    player2.make_sprite(type_="rect", width=game_pad_width, height=game_pad_height, color="white",
                        position=(screen.width - 60, screen.height / 2 - game_pad_width - of_x),
                        velocity=(0, 200),
                        mass=10,
                        moment=1,
                        elasticity=1.8 if beast_mode else 1, physics=True)

    # -------------------ball----------------#
    ball = Sprite(screen, "ball")  # ball
    ball.make_sprite(type_="circle", radius=10, color="white", collisions_level=1,
                     position=(screen.width / 2, screen.height / 2),
                     velocity=(240 * random.choice([-1, 1]), 240 * random.choice([-1, 1])),
                     mass=10,
                     moment=10,
                     elasticity=1.2 if beast_mode else 1.7, physics=True)

    # -------------------border----------------#

    points = [(25, 25), (25, screen.height - 25), (screen.width - 25, screen.height - 25), (screen.width - 25, 25)]

    # border_l = Sprite(screen, "border_l").make_sprite(type_="line", width=5, point1=points[0], point2=points[1],
    #                                                  collisions_level=2, color="white",
    #                                                  physics=False)  # line
    # border_r = Sprite(screen, "border_r").make_sprite(type_="line", width=5, point1=points[1], point2=points[2],
    #                                                  collisions_level=3, color="white",
    #                                                  physics=False)  # line
    # border_t = Sprite(screen, "border_t").make_sprite(type_="line", width=5, point1=points[2], point2=points[3],
    #                                                  collisions_level=4, color="white",
    #                                                  physics=False)  # line
    # border_b = Sprite(screen, "border_b").make_sprite(type_="line", width=5, point1=points[3], point2=points[0],
    #                                                  collisions_level=4, color="white",
    #                                                  physics=False)  # line

    border = Sprite(screen, "border_l").make_sprite(type_="box", width=15, aa_lines_list=points,
                                                    collisions_for_sep_aa_line=(2, 4, 3, 4), is_closed=True
                                                    # color_for_aa_line=((255, 255, 0),(255, 0, 255),(255, 0, 0),
                                                    # (255, 0, 0))
                                                    , color="white", elasticity=.5 if beast_mode else 0.4,
                                                    physics=False)  # line

    # -------------------init player Life----------------#
    life_pl1 = [3]
    life_pl2 = [3]

    # -------------------add game manics----------------#

    def reset():
        ball.body.position = (screen.width / 2, screen.height / 2)
        ball.body.velocity = (400 * random.choice([-1, 1]), 400 * random.choice([-1, 1]))
        border.set_color("white")

    def pl1_loose_one_live(arbiter, space_, data):
        life_pl1[0] -= 1
        reset()
        return False

    ball_collision_border_l_handler = space.add_collision_handler(1, 2)
    ball_collision_border_l_handler.pre_solve = pl1_loose_one_live

    def pl2_loose_one_live(arbiter, space_, data):
        life_pl2[0] -= 1
        reset()
        return False

    ball_collision_border_r_handler = space.add_collision_handler(1, 3)
    ball_collision_border_r_handler.pre_solve = pl2_loose_one_live

    # -------------------init Text----------------#
    text = Text(screen)
    text.init_font()

    # -------------------init Mouse----------------#
    mouse = Mouse(screen, None)

    # -------------------make sprite array----------------#
    sprites = [player1, player2, ball, border]  # _l, border_r, border_t, border_b]

    # -------------------ADDING OBJECTS IN TO WORLD----------------#

    # player1.add_to_space(space)
    # player2.add_to_space(space)
    # ball.add_to_space(space)
    # border_l.add_to_space(space)
    # # ...

    list(map(lambda sprite: sprite.add_to_space(space), sprites))
    # lambda sprite: sprite.add_to_space(space) -> def _lambda_(sprite): sprite.add_to_space(space)

    fps = 25
    run = True
    out = False
    num_out = 0

    while run:
        background_map.draw()

        # -------------------starting event loop----------------#
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:
                if not out:
                    if event.key == pygame.K_w:
                        player1.body.velocity = (0, 400)

                    if event.key == pygame.K_s:
                        player1.body.velocity = (0, -400)

                    if event.key == pygame.K_UP:
                        player2.body.velocity = (0, 400)

                    if event.key == pygame.K_DOWN:
                        player2.body.velocity = (0, -400)

                    if event.key == pygame.K_r:
                        reset()

            if event.type == pygame.KEYUP:
                if not out:
                    if event.key == pygame.K_w:
                        player1.body.velocity = (0, 0)

                    if event.key == pygame.K_s:
                        player1.body.velocity = (0, 0)

                    if event.key == pygame.K_UP:
                        player2.body.velocity = (0, 0)

                    if event.key == pygame.K_DOWN:
                        player2.body.velocity = (0, 0)

        if ball_color:
            # ----------------Dynamic colors and Beast mode----------------#

            p = [500, 800, 1400, 1500]
            v = abs(sum(ball.body.velocity))
            p.append(v)
            p.sort()
            i_ = p.index(v)
            ball.set_color(["white", "yellow", "azul", "purple", "red"][i_])
            border.set_color(["white", "yellow", "azul", "purple", "red"][i_])

            if i_ >= 4 and beast_mode:
                sprites.append(add_ball(screen))
                sprites.append(add_ball(screen))
                reset()

        # ----------------Extra Game mechanics ----------------#

        if life_pl1[0] <= 0 or life_pl2[0] <= 0:

            if not out:
                reset()
                ball.body.velocity = (0, 0)
                player1.body.velocity = (0, -300)
                player2.body.velocity = (0, 300)

            num_out += 1
            out = True

            text.show(f"!!!PL{1 if life_pl2[0] <= 0 else 2} WIN!!! Starting in {int(300 / num_out * 100)}",
                      (screen.width / 2 - 100, screen.height / 2 - 50), (255, 255, 255))

            if num_out >= 300:
                life_pl1[0] = 3
                life_pl2[0] = 3
                out = False
                reset()

        player1.body.velocity = (0, player1.body.velocity[1])
        player2.body.velocity = (0, player2.body.velocity[1])
        player1.body.position = (60, player1.body.position[1])
        player2.body.position = (screen.width - 60, player2.body.position[1])
        if ball.if_of_screen() or -2000 <= sum(ball.body.velocity) >= 2000:
            reset()

        if len(sprites) > 4:
            kill_list = []
            for sprite in sprites[4:]:
                if sprite.if_of_screen():
                    kill_list.append(sprite)
                    sprite.kill = True

            for sprite in kill_list:
                sprites.remove(sprite)
                if sprite.do_kill():
                    del sprite

        # -------------------drawing sprites to screen---------------#

        # -------------------print score----------------#
        text.show(f"PL2 Life {life_pl2[0]}", (screen.width - 180, 60), (255, 255, 255))
        text.show(f"PL1 Life {life_pl1[0]}", (80, 60), (255, 255, 255))

        if rotation:
            player1.debug_draw_rect()
            player2.debug_draw_rect()
        else:
            player1.body.angular_velocity = 0
            player2.body.angular_velocity = 0
            player1.body.angle = 0
            player2.body.angle = 0

        list(map(lambda sprite_: sprite_.draw_func(), sprites))
        mouse.show_m(False)

        # -------------------using clock to cap fps and space.step to run physics----------------#
        space.step(1 / fps)
        clock.tick(fps)

        pygame.display.flip()


if __name__ == '__main__':
    # starting Game
    pygame.init()
    functional()
