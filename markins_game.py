import random
import time

import pymunk

from util.MGameM import Screen, Sprite, Text, Mouse, clock, Sheet, space, Map, Animation  # import custom

import pygame


def create_proj_spr(screen, position, space_, color=(200, 20, 15)):
    proj_ = Sprite(screen, "p")
    proj_.make_sprite(type_="circle", color=color, radius=3, position=position,
                      physics=True, mass=550, elasticity=.4, velocity=(120, 0))
    proj_.add_to_space(space_)
    return proj_


def functional():
    sp = pymunk.Space()
    sp.gravity = (320, 0)
    # Open a Window -
    screen = Screen(width=1280, height=720, title="Pong")
    bg1 = Map(screen, "statick")
    bg = Map(screen, "dynamic-img")
    bg.load_dynamic_img("main", "img/testBG.png")
    bg.speed = [-5, 0]
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
    # player_sprite.debug_img_rot_draw = True
    player_sprite.make_sprite("img", 1, player_wh[0], player_wh[1], file=sprite_sheet.make_new_sheet_img("player",
                                                                                                         img_size=0.3),
                              position=(200, 400), physics=True, moment=50, mass=50000)
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

    border.add_to_space(space)

    sprite_sheet_data2 = {
        "0": (0, 0, 49, 49),
        "1": (51, 0, 49, 49),
        "2": (101, 0, 49, 49),
        "3": (151, 0, 49, 49),
        "4": (201, 0, 49, 49),
        "5": (251, 0, 49, 49),
        "6": (301, 0, 49, 49),
        "7": (351, 0, 49, 49),
        "8": (401, 0, 49, 49),
        "9": (451, 0, 49, 49),
    }
    warp_alim = Animation(screen=screen, name="test", file="img/testAlim2.png", sprite_sheet_info=sprite_sheet_data,
                          color_key=(0, 0, 0))

    warp_alim.make_new_animation("warp", sprite_sheet_data2, size=3)

    # warp_alim.debug_img_rot_draw = True

    warp_alim.make_sprite("img", elasticity=1,
                          position=(600, 400), physics=False, velocity=(20, 10),
                          file=warp_alim.stos[warp_alim.ac_alim][0][1])

    warp_alim.add_to_space(sp)

    warp = [False]

    def warp_(arbiter, space_, data):
        warp[0] = True
        return True

    warp__ = space.add_collision_handler(1, 4)
    warp__.pre_solve = warp_

    def round_e_1_(arbiter, space_, data):
        player_sprite.body.position = screen.width - border_offset - player_sprite.width / 2 - 1 * abs(
            player_sprite.body.angle * 10), \
                                      player_sprite.body.position[1]
        return False

    round_e_1 = space.add_collision_handler(1, 2)
    round_e_1.pre_solve = round_e_1_

    def round_e_2_(arbiter, space_, data):
        player_sprite.body.position = player_sprite.body.position[
                                          0], border_offset + player_sprite.height / 2 + 1 * abs(
            player_sprite.body.angle * 10)
        return False

    round_e_2 = space.add_collision_handler(1, 3)
    round_e_2.pre_solve = round_e_2_

    def round_e_4_(arbiter, space_, data):
        player_sprite.body.position = player_sprite.body.position[0], \
                                      screen.height - border_offset - player_sprite.height / 2 - 1 * abs(
                                          player_sprite.body.angle * 10)
        return False

    round_e_4 = space.add_collision_handler(1, 5)
    round_e_4.pre_solve = round_e_4_
    text = Text(screen)
    text.init_font()
    proj = []
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
    tog = False

    wave = 0
    run = True
    player_sprite.body.angle = -1.6
    fps = 25
    for_ = 0
    while run:
        bg1.draw()
        bg.draw()

        # using clock to cap fps
        dt = clock.tick(fps) / 10
        space.step(1 / fps)
        sp.step(1 / fps)
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

                    if event.key == pygame.K_SPACE:
                        tog = not tog
                        # proj.append(create_proj_spr(screen, player_sprite.body.position))
                        # proj.append(create_proj_spr(screen, player_sprite.body.position))
                        # proj.append(create_proj_spr(screen, player_sprite.body.position))
                        # proj.append(create_proj_spr(screen, player_sprite.body.position))
                        # proj.append(create_proj_spr(screen, player_sprite.body.position))
                        # proj.append(create_proj_spr(screen, player_sprite.body.position))

            if event.type == pygame.KEYUP:

                player_sprite.set_do_slow_down(True)

                if event.key == pygame.K_q:
                    player_sprite.rotate(.3, False)

                if event.key == pygame.K_e:
                    player_sprite.rotate(-.3, False)

        if tog:
            for _ in range(8):
                proj.append(create_proj_spr(screen, player_sprite.body.position, sp))
        border.draw_func()

        text.show(f"Fps {100 / dt:.1f}", (screen.width - 180, 60), (255, 255, 255))

        # print(360 % angel)

        if warp[0]:

            warp_alim.next_step(15)
            warp_alim.body.position = player_sprite.body.position
            warp_alim.draw_func()
            for_ += 1
            bg.speed = [-10, 0]
            # if for_ == 2:
            #    player_sprite.body.position = (300, screen.height/2)
            player_sprite.body.velocity = (-500, 0)
            # space.gravity = (-9000, 0)
            sp.gravity = (9 * 100, 0)
            if for_ >= 20:
                bg.speed = [-470, 0]
                player_sprite.body.velocity = (-260, 0)
            if for_ >= 40:
                bg.speed = [-150, 0]
                player_sprite.body.velocity = (960, 0)
            if for_ == 60:
                player_sprite.body.position = (0, screen.height / 2)
            if for_ >= 65:
                sp.gravity = (320, 0)
                bg.speed = [-5, 0]
                for_ = 0
                warp[0] = False
                player_sprite.body.velocity = (0, 0)
                space.gravity = (0, 0)

        player_sprite.do_rotate()
        for ap in proj:
            ap.draw_func()
        player_sprite.slow_down(1.1)
        player_sprite.draw_func()
        player_sprite.body.angular_velocity = 0

        mouse.show_m(False)
        pygame.display.update()
        # pygame.display.flip()


if __name__ == '__main__':
    # starting Game
    functional()
