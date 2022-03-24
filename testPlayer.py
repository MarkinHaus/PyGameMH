from util.MGameM import Screen, Sprite, Text, Mouse, clock, space, Map, Animation
import random
import pygame

"""

    f = [0, 40, 97, 153, 208, 265, 320, 377, 433, 489, 544]
    #f.reverse()
    sprite_sheet_data = [{}]
    g = 0
    for i in range(10):
        for j in range(10):
            sprite_sheet_data[0][g] = (50*j+1, f[i+1]-40, 50-1, (f[i+1] - f[i])-1)
            g += 1
    #sprite_sheet_data_ideal = {
    #    "0": (0,   50*a_num, 50, 50),
    #    "1": (50,  50*a_num, 50, 50),
    #    "2": (100, 50*a_num, 50, 50),
    #    "3": (150, 50*a_num, 50, 50),
    #    "4": (200, 50*a_num, 50, 50),
    #    "5": (250, 50*a_num, 50, 50),
    #    "6": (300, 50*a_num, 50, 50),
    #    "7": (350, 50*a_num, 50, 50),
    #    "8": (400, 50*a_num, 50, 50),
    #    "9": (450, 50*a_num, 50, 50),
    #}
    print(sprite_sheet_data)
    dc_ideal = {}
    sprite_sheet_data_ideal = [0, 57, 56, 57, 0]
    l = 0
    for i in sprite_sheet_data_ideal:
        dc_ideal[str(l)] = sprite_sheet_data[0][i]
        l += 1
        """


def functional():
    # Open a Window -
    space.gravity = (0, -600)
    screen = Screen(width=1236, height=512, title="Stick-Man")

    background_map = Map(screen, "statick", color=(220, 220, 220))  # statick statick-img dynamic-img

    # -------------------player----------------#
    a_num = 3
    # 0 - 10
    # 1 - 4
    # 2 + 2
    # 3 + 8
    # f.reverse()
    sprite_sheet_data = [{}]
    g = 0
    for i in range(2):
        for j in range(12):
            f = (18 * j) + (198 * j) - 8
            print(j, f)
            sprite_sheet_data[0][g] = (185*i, 0 if f < 0 else f, 185, 180 if i == 0 else 191)
            g += 1
    # sprite_sheet_data_ideal = {
    #    "0": (0,   50*a_num, 50, 50),
    #    "1": (50,  50*a_num, 50, 50),
    #    "2": (100, 50*a_num, 50, 50),
    #    "3": (150, 50*a_num, 50, 50),
    #    "4": (200, 50*a_num, 50, 50),
    #    "5": (250, 50*a_num, 50, 50),
    #    "6": (300, 50*a_num, 50, 50),
    #    "7": (350, 50*a_num, 50, 50),
    #    "8": (400, 50*a_num, 50, 50),
    #    "9": (450, 50*a_num, 50, 50),
    # }
    print(sprite_sheet_data)
    dc_ideal = {}
    sprite_sheet_data_ideal = list(range(0, 12))
    l = 0
    for i in sprite_sheet_data_ideal:
        dc_ideal[str(l)] = sprite_sheet_data[0][i]
        l += 1

    dc_walk = {}
    sprite_sheet_data_ideal = list(range(12, 23))
    l = 0
    for i in sprite_sheet_data_ideal:
        dc_walk[str(l)] = sprite_sheet_data[0][i]
        l += 1
    player = Animation(screen=screen, name="test", file="img/Stickmanswordsprites2.png",
                       color_key=(138, 138, 138))

    player.make_new_animation("walk", dc_walk, size=.6)
    player.make_new_animation("ideal", dc_ideal, size=.6)

    # warp_alim.debug_img_rot_draw = True

    player.make_sprite("img", elasticity=1,
                       position=(600, 400), physics=True,  # velocity=(20, 10),
                       file=player.stos[player.ac_alim][0][1])

    # warp_alim.add_to_space(sp)

    # -------------------init Text----------------#
    text = Text(screen)
    text.init_font()

    # -------------------init Mouse----------------#
    mouse = Mouse(screen, None)

    # ------------------- Border -------------------------#
    border_b = Sprite(screen, "border_b").make_sprite(type_="line", width=5, point1=(50, 50), point2=(1180, 50),
                                                      collisions_level=1, color="black",
                                                      physics=False)
    # -------------------make sprite array----------------#
    sprites = [border_b, player]  # _l, border_r, border_t, border_b]

    # -------------------ADDING OBJECTS IN TO WORLD----------------#

    list(
        map(
            lambda sprite_: sprite_.add_to_space(space)
            , sprites
        )
    )
    # lambda sprite: sprite.add_to_space(space) -> def _lambda_(sprite): sprite.add_to_space(space)

    fps = 25
    run = True

    while run:
        background_map.draw()

        # -------------------starting event loop----------------#
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:

                # if game is not over
                    if event.key == pygame.K_s:
                        player.set_do_slow_down(False)
                        player.body.velocity = (player.body.velocity[0], -250)

                    if event.key == pygame.K_a:
                        player.set_do_slow_down(False)
                        player.body.velocity = (-250, player.body.velocity[1])

                    if event.key == pygame.K_d:
                        player.set_do_slow_down(False)
                        player.load_animation("walk")
                        player.body.velocity = (250, player.body.velocity[1])

                    if event.key == pygame.K_q:
                        player.rotate(.25, True)

                    if event.key == pygame.K_e:
                        player.rotate(-.25, True)

                    if event.key == pygame.K_SPACE:
                        player.set_do_slow_down(False)
                        player.body.velocity = (player.body.velocity[0], 300)

            if event.type == pygame.KEYUP:
                player.load_animation("ideal")
                player.set_do_slow_down(True)

                if event.key == pygame.K_q:
                    player.rotate(.3, False)

                if event.key == pygame.K_e:
                    player.rotate(-.3, False)
        # -------------------print score----------------#
        text.show(f"TEXT", (screen.width - 180, 60), (0, 0, 0))

        # -------------------drawing sprites to screen---------------#

        player.next_step(24)
        player.draw_func()
        player.do_rotate()
        player.slow_down(1.9)
        player.body.angular_velocity = 0
        #player.debug_draw_rect((255, 0,255))

        list(map(lambda sprite_: sprite_.draw_func(), sprites))

        mouse.show_m(False)

        # -------------------using clock to cap fps and space.step to run physics----------------#
        space.step(1 / fps)
        clock.tick(fps)

        pygame.display.flip()


if __name__ == '__main__':
    print("Hello, Pygame and Pymunk")
    print("Universe!")
    # starting Game
    pygame.init()
    functional()
