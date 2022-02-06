from util.MGameM import Screen, Sprite, Text, Mouse, clock, Sheet, space, Map  # import custom
import pygame


def functional():
    # Open a Window -
    screen = Screen(width=1280, height=720, title="Pong")
    bg1 = Map(screen, "statick")
    bg = Map(screen, "dynamic-img")
    bg.load_dynamic_img("main", "img/testBG.png")
    # init Sprites blueprint

    player_wh = [213, 228]
    e_type2_wh = [100, 75]
    e_type1_wh = [100, 77]

    sprite_sheet_data = {
        "width": 359,
        "height": 261,
        "default": (0, 0, 359, 261),
        "player": (32, 19, player_wh[0], player_wh[1]),
        "enemy1": (255, 118, e_type1_wh[0], e_type1_wh[1]),
        "enemy2": (254, 117, e_type2_wh[0], e_type2_wh[1])
    }

    sprite_sheet = Sheet("img/spaceWarAssets.png", sprite_sheet_data)  # Sheet
    player_sprite = Sprite(screen, "player")  # img
    player_sprite.debug_img_rot_draw = True
    player_sprite.make_sprite("img", 1, player_wh[0], player_wh[1], file=sprite_sheet.make_new_sheet_img("player",
                                                                                                         img_size=0.3),
                              position=(400, 400), physics=True, moment=500, mass=5)
    player_sprite.add_to_space(space)

    border_offset = -50
    points = [(border_offset, border_offset), (border_offset, screen.height - border_offset),
              (screen.width - border_offset, screen.height - border_offset),
              (screen.width - border_offset, border_offset)]
    border = Sprite(screen, "border_l").make_sprite(type_="box", width=5, aa_lines_list=points,
                                                    collisions_for_sep_aa_line=(2, 3, 4, 5), is_closed=True
                                                    # color_for_aa_line=((255, 255, 0),(255, 0, 255),(255, 0, 0),
                                                    # (255, 0, 0))
                                                    , color="white", elasticity=1,
                                                    physics=False)  # line


    #border.add_to_space(space)

    def round_e_1_(arbiter, space_, data):
        player_sprite.body.position = screen.width - border_offset - player_sprite.width/2 - 1*abs(player_sprite.body.angle*10),\
                                      player_sprite.body.position[1]
        return False

    round_e_1 = space.add_collision_handler(1, 2)
    round_e_1.pre_solve = round_e_1_

    def round_e_2_(arbiter, space_, data):
        player_sprite.body.position = player_sprite.body.position[0], border_offset + player_sprite.height/2 + 1*abs(player_sprite.body.angle*10)
        return False

    round_e_2 = space.add_collision_handler(1, 3)
    round_e_2.pre_solve = round_e_2_

    def round_e_3_(arbiter, space_, data):
        player_sprite.body.position = border_offset + player_sprite.width/2 - 1*abs(player_sprite.body.angle*10), player_sprite.body.position[1]
        return False

    round_e_3 = space.add_collision_handler(1, 4)
    round_e_3.pre_solve = round_e_3_

    def round_e_4_(arbiter, space_, data):
        player_sprite.body.position = player_sprite.body.position[0],\
                                      screen.height - border_offset - player_sprite.height/2-1*abs(player_sprite.body.angle*10)
        return False

    round_e_4 = space.add_collision_handler(1, 5)
    round_e_4.pre_solve = round_e_4_


    # init Text
    text_score = Text(screen)
    text_score.init_font(20)

    text_info = Text(screen)
    text_info.init_font(15)

    # init Mouse
    mouse = Mouse(screen, None)

    # game vars

    score = 0
    hp = 100
    bullets = 0

    wave = 0
    run = True
    player_sprite.body.angle = -1.6

    while run:
        bg1.draw()
        bg.draw()

        # using clock to cap fps
        dt = clock.tick(25) / 10
        space.step(1/25)
        # dt control movement speed

        # starting event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:

                # if game is not over
                if not hp <= 0:

                    if event.key == pygame.K_w:
                        player_sprite.set_do_slow_down(False)
                        player_sprite.body.velocity = (player_sprite.body.velocity[0], 300)

                    if event.key == pygame.K_s:
                        player_sprite.set_do_slow_down(False)
                        player_sprite.body.velocity = (player_sprite.body.velocity[0], -300)

                    if event.key == pygame.K_a:
                        player_sprite.set_do_slow_down(False)
                        player_sprite.body.velocity = (-300, player_sprite.body.velocity[1])

                    if event.key == pygame.K_d:
                        player_sprite.set_do_slow_down(False)
                        player_sprite.body.velocity = (300, player_sprite.body.velocity[1])

                    if event.key == pygame.K_q:
                        player_sprite.rotate(.25, True)

                    if event.key == pygame.K_e:
                        player_sprite.rotate(-.25, True)

            if event.type == pygame.KEYUP:

                player_sprite.set_do_slow_down(True)

                if event.key == pygame.K_q:
                    player_sprite.rotate(.3, False)

                if event.key == pygame.K_e:
                    player_sprite.rotate(-.3, False)

        player_sprite.do_rotate()

        player_sprite.slow_down(1.1)
        player_sprite.draw_func()

        border.draw_func()

        # print(360 % angel)

        mouse.show_m(False)
        pygame.display.update()
        #pygame.display.flip()


if __name__ == '__main__':
    # starting Game
    functional()
