import math
import random
import time
from typing import List

from util.MGameM import Screen, Sprite, Text, Mouse, clock, Sheet, space, Map, Animation, parser  # V.2.6

import pygame
from pygame import Vector2


def create_proj_spr(screen, position, color=(200, 20, 15), angel=.0, radius=4, type_=-1, speed=0, c=8, damage=1.0):
    proj_ = Sprite(screen, "p")
    speed = 580 + speed

    if damage > 10:
        color = "purple"
    if damage > 15:
        color = "azul"
    if damage > 20:
        color = "black"

    if damage >= 20:
        radius += damage - 10

    if damage >= 35:
        type_ = 0

    if damage >= 200:
        type_ = 1

    if damage >= 500:
        type_ = 2

    if damage >= 999:
        type_ = 3

    img = " "
    if type_ != -1:
        img = game_data[f"P{type_ + 1}"]
    x = speed * math.cos(angel)
    y = speed * math.sin(angel)
    #print(type_, color, c, game_data["damage"])
    proj_.make_sprite(type_="circle" if type_ == -1 else "img", file=img, color=color, radius=radius, position=position,
                      physics=True, mass=500, elasticity=.4, velocity=(x, y), collisions_level=c)
    proj_.add_to_space(space)
    return proj_


def garbage_collecktor(proj: List[Sprite], del_list: List[Sprite]):
    for p in proj:
        if p.do_kill() or p.if_of_screen():
            del_list.append(p)
            p.kill = True
    for p in del_list:
        if p.do_kill() and p in proj:
            proj.remove(p)
            del p


def pos_setter_bar(value):
    return_color = "red"
    if value > 20:
        return_color = "purple"
        value -= 20
    if value > 20:
        return_color = "azul"
        value -= 20
    if value > 20:
        return_color = "black"
        value -= 20
    if value < 0:
        value = 0
    return value, return_color


def pos_setter_bar_(value):
    return_color = "red"
    if value > 200:
        return_color = "purple"
        return value/80, return_color
    if value > 1600:
        return_color = "azul"
        return value / 160, return_color
    if value > 3200:
        return_color = "black"
        return value / 1800, return_color

    if value < 0:
        value = 0
    return value, return_color


def play(level=0):
    def set_bars():

        p2, c2 = pos_setter_bar_(player_data["max_mult"])
        p3, c3 = pos_setter_bar(player_data["hp"])

        nitro_line.point2 = (687 + p2 * 10, 102)
        hp_line.point2 = (347 + p3 * 31.5, 46)

        nitro_line.set_color(c2 if c2 != "black" else "white")
        hp_line.set_color(c3 if c3 != "black" else "white")

    def home():
        game_data["ships_i"][2] = player_data["max_mult"]
        player_data['inventar']['ships'][s_num[0]] -= 1
        start_frame(sum(player_data['inventar']['ships']) > 0)

    t0 = time.time()
    t1 = time.time()
    t2 = time.time()
    bg.speed = [-5, 0]
    # init Sprites blueprint
    player_sprite = Sprite(screen, "player")  # img
    # player_sprite.debug_img_rot_draw = True

    ships = [game_data["E0"],
             game_data["E1"],
             game_data["E2"],
             game_data["E3"],
             game_data["E4"],
             game_data["E5"]]

    player_sprite.make_sprite("img", 1,
                              file=ships[s_num[0]], position=(200, 400),
                              physics=True, moment=50, mass=50)
    player_sprite.add_to_space(space)

    item_sp = Sprite(screen, "item_sp").make_sprite("img", 45,
                                                    file=game_data["I4"], position=(-200, -400),
                                                    physics=True, moment=50, mass=50)
    item_sp.add_to_space(space)

    border_offset = -120
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

    enemy_0 = Sprite(screen, "enemy-0")  # img
    enemy_0.make_sprite("img", collisions_level=10,
                        file=game_data["C1"], position=(1100, 200),
                        physics=True, moment=50, mass=50, velocity=(-50, 0))
    enemy_0.add_to_space(space)

    enemy_1 = Sprite(screen, "enemy-0")  # img
    enemy_1.make_sprite("img", collisions_level=11,
                        file=game_data["C2"], position=(1100, 400),
                        physics=True, moment=50, mass=50, velocity=(-50, 0))
    enemy_1.add_to_space(space)

    enemy_2 = Sprite(screen, "enemy-0")  # img
    enemy_2.make_sprite("img", collisions_level=12,
                        file=game_data["C1"], position=(1100, 600),
                        physics=True, moment=50, mass=50, velocity=(-50, 0))
    enemy_2.add_to_space(space)

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
    warp_alim = Animation(screen=screen, name="test", file="img/testAlim2.png",
                          color_key=(0, 0, 0))

    warp_alim.make_new_animation("warp", sprite_sheet_data2, size=3)

    warp_alim.make_sprite("img", elasticity=1,
                          position=(-600, -400), physics=False, velocity=(20, 10),
                          file=warp_alim.stos[warp_alim.ac_alim][0][1])

    warp = [False]

    def warp_(arbiter, space_, data):
        warp[0] = True
        return True

    warp__ = space.add_collision_handler(1, 4)
    warp__.pre_solve = warp_

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

    def norc(arbiter, space_, data):
        return False

    proj_front_border = space.add_collision_handler(8, 4)
    proj_front_border.pre_solve = norc

    proj_front_border = space.add_collision_handler(8, 2)
    proj_front_border.pre_solve = norc

    proj_front_border = space.add_collision_handler(8, 4)
    proj_front_border.pre_solve = norc

    proj_front_border = space.add_collision_handler(80, 8)
    proj_front_border.pre_solve = norc

    def proj_e_data0_(arbiter, space_, data):
        #print("hit")
        player_data["hp"] -= player_data["e_damage"] + level * 2 - game_data['ships_i'][1]
        set_bars()
        arbiter.shapes[0].body.position = (10000, 1000)
        player_sprite.body.position = list(arbiter.shapes[1].body.position).copy()
        return False

    proj_e_data0 = space.add_collision_handler(80, 1)
    proj_e_data0.pre_solve = proj_e_data0_

    def proj_e_data0_(arbiter, space_, data):
        if item_exist[0]:
            player_data["Bitcoins"] += player_data["e_damage"] + level * 10
            arbiter.shapes[0].body.position = (10000, 1000)
            #print("DESPOWN")
            item_exist[0] = False
            item_exist[1] = False
            item_sp.body.position = (-10000, -1000)
            player_sprite.body.position = list(arbiter.shapes[1].body.position).copy()
        return False

    proj_e_data0 = space.add_collision_handler(45, 1)
    proj_e_data0.pre_solve = proj_e_data0_

    def proj_e_data0_(arbiter, space_, data):
        enemy_0_data[0] -= game_data['damage']*player_data['max_mult']
        arbiter.shapes[0].body.position = (10000, 1000)
        player_data["max_mult"] += game_data["damage"] if player_data["max_mult"] <= game_data["ships_i"][2] else \
            game_data["ships_i"][2] - 1
        return False

    proj_e_data0 = space.add_collision_handler(8, 10)
    proj_e_data0.pre_solve = proj_e_data0_

    def proj_e_data1_(arbiter, space_, data):
        enemy_1_data[0] -= game_data['damage']*player_data['max_mult']
        arbiter.shapes[0].body.position = (10000, 1000)
        player_data["max_mult"] += game_data["damage"] if player_data["max_mult"] <= game_data["ships_i"][2] else \
            game_data["ships_i"][2] - 1
        return False

    proj_e_data1 = space.add_collision_handler(8, 11)
    proj_e_data1.pre_solve = proj_e_data1_

    def proj_e_data2_(arbiter, space_, data):
        enemy_2_data[0] -= game_data['damage']*player_data['max_mult']
        arbiter.shapes[0].body.position = (10000, 1000)
        player_data["max_mult"] += game_data["damage"] if player_data["max_mult"] <= game_data["ships_i"][2] else \
            game_data["ships_i"][2] - 1
        return False

    proj_e_data2 = space.add_collision_handler(8, 12)
    proj_e_data2.pre_solve = proj_e_data2_

    text = Text(screen)
    text.init_font()
    proj: List[Sprite] = []
    del_list: List[Sprite] = []
    # init Text
    text_score = Text(screen)
    text_score.init_font(20)

    text_info = Text(screen)
    text_info.init_font(15)
    # init Mouse
    mouse = Mouse(screen, None)
    # game vars
    run = True
    enemy_0_data = [5 + level ** 1.6, 0, 0]
    enemy_1_data = [5 + level ** 1.6, 0, 0]
    enemy_2_data = [5 + level ** 1.6, 0, 0]

    # space.gravity = (-80, 0)

    for_ = 0
    bg_statick_img.lode_new("Hud")

    player_data["hp"] = game_data["ships_i"][3]

    nitro_line = Sprite(screen, "damage").make_sprite("line", width=15, point1=(687, 102),
                                                      point2=(687 + player_data["max_mult"] * 10, 102),
                                                      physics=False, moment=50, mass=50, color="blue")

    hp_line = Sprite(screen, "damage").make_sprite("line", width=14, point1=(347, 46),
                                                   point2=(347 + player_data["hp"] * 31.5, 46),
                                                   physics=False, moment=50, mass=50, color="red")

    i = 0
    for item_inv in player_data["items"]:
        item_inv.body.position = game_data["i_pos"][0][i]
        i += 1

    set_bars()
    item_exist = [False, True]

    while run:

        # using clock to cap fps
        dt = clock.tick(fps) / 10
        space.step(1 / fps)
        # dt control movement speed

        bg.draw()
        bg_statick_img.draw()

        hp_line.draw_func()
        nitro_line.draw_func()

        # starting event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:
                smax = game_data['ships_i'][2] if game_data['ships_i'][2] <= 200 else 200
                if event.key == pygame.K_i:
                    start_frame(True)
                if event.key == pygame.K_w:
                    player_sprite.set_do_slow_down(False)
                    player_sprite.body.velocity = (player_sprite.body.velocity[0], 300 + smax)
                if event.key == pygame.K_s:
                    player_sprite.set_do_slow_down(False)
                    player_sprite.body.velocity = (player_sprite.body.velocity[0], -300 - smax)
                if event.key == pygame.K_a:
                    player_sprite.set_do_slow_down(False)
                    player_sprite.body.velocity = (-300 - smax, player_sprite.body.velocity[1])
                if event.key == pygame.K_d:
                    player_sprite.set_do_slow_down(False)
                    player_sprite.body.velocity = (300 + smax, player_sprite.body.velocity[1])
                if event.key == pygame.K_q:
                    player_sprite.rotate(.16, True)
                if event.key == pygame.K_e:
                    player_sprite.rotate(-.16, True)
                if event.key == pygame.K_SPACE:
                    garbage_collecktor(proj, del_list)
                    x, y = player_sprite.body.position
                    proj.append(
                        create_proj_spr(screen, (x, y + 5), damage=game_data['damage']*player_data['max_mult'], angel=player_sprite.body.angle,
                                        speed=game_data['ships_i'][2]))
                    proj.append(
                        create_proj_spr(screen, (x, y - 5), damage=game_data['damage']*player_data['max_mult'], angel=player_sprite.body.angle,
                                        speed=game_data['ships_i'][2]))

            if event.type == pygame.KEYUP:

                player_sprite.set_do_slow_down(True)

                if event.key == pygame.K_q:
                    player_sprite.rotate(.3, False)

                if event.key == pygame.K_e:
                    player_sprite.rotate(-.3, False)

        text.show(f"Fps {100 / dt:.1f}", (screen.width - 220, 10), (255, 255, 255))
        text.show(f"P {len(proj)}", (screen.width - 220, 30), (255, 255, 255))
        text.show(f"Level {level}", (screen.width - 220, 50), (255, 255, 255))
        text.show(f"$ {player_data['Bitcoins']:.2f}", (screen.width - 220, 70), (255, 255, 255))

        text.show(f"E-HP {enemy_0_data[0]:.0f} {enemy_1_data[0]:.0f} {enemy_2_data[0]:.0f}", (5, 10), (255, 255, 255))

        text.show(f"HP {player_data['hp']:.2f}", (5, 30), (255, 255, 255))
        text.show(f"NITRO {player_data['max_mult']:.2f}", (5, 50), (255, 255, 255))
        text.show(f"DAMAGE {game_data['damage']*player_data['max_mult']:.2f}", (5, 70), (255, 255, 255))

        text.show(f"X {player_data['max_mult']:.2f}", (874, 580), (255, 255, 255))

        if warp[0]:
            proj = []
            warp_alim.next_step(15)
            warp_alim.body.position = player_sprite.body.position
            warp_alim.draw_func()
            for_ += 1
            bg.speed = [-10, 0]
            # if for_ == 2:
            #    player_sprite.body.position = (300, screen.height/2)
            player_sprite.body.velocity = (-500, 0)
            enemy_0.body.position = (10000, 0)
            enemy_1.body.position = (10000, 0)
            enemy_2.body.position = (10000, 0)
            # space.gravity = (-9000, 0)
            player_sprite.body.angle = 0
            if for_ >= 20:
                bg.speed = [-470, 0]
                player_sprite.body.velocity = (-260, 0)
            if for_ >= 40:
                bg.speed = [-150, 0]
                player_sprite.body.velocity = (960, 0)
            if for_ == 60:
                player_sprite.body.position = (0, screen.height / 2)
            if for_ >= 65:
                if level % 2 == 0:
                    item_exist[1] = True
                bg.speed = [-5, 0]
                for_ = 0
                warp[0] = False
                player_sprite.body.velocity = (0, 0)
                # space.gravity = (-10 - 2 * level, 0)
                level += 1
                player_data["e_damage"] += level
                enemy_0.body.position = (1100, 600)
                enemy_1.body.position = (1100, 400)
                enemy_2.body.position = (1100, 200)
                enemy_0.body.velocity = (-100+level*2, 0)
                enemy_1.body.velocity = (-100+level*2, 0)
                enemy_2.body.velocity = (-100+level*2, 0)
                enemy_0_data = [round(6 + level ** 1.6), 0, 0]
                enemy_1_data = [round(6 + level ** 1.6), 0, 0]
                enemy_2_data = [round(6 + level ** 1.6), 0, 0]

        player_sprite.do_rotate()
        for ap in proj:
            ap.draw_func()
        player_sprite.slow_down(1.02)
        player_sprite.draw_func()
        player_sprite.body.angular_velocity = 0

        if item_exist[0]:
            item_sp.draw_func()

        if enemy_0_data[0] >= 0:
            enemy_0.draw_func()
            if time.time() - t0 >= (10000 - level * 4) / 5430:
                player_data["max_mult"] -= level * 4 if player_data["max_mult"] >= 0 else 0
                x, y = enemy_0.body.position
                proj.append(create_proj_spr(screen, (x - 50, y),
                                            angel=enemy_0.body.angle + 3.15, speed=game_data['ships_i'][2], c=80,
                                            damage=player_data["e_damage"]))
                t0 = time.time()
        if enemy_1_data[0] >= 0:
            enemy_1.draw_func()
            if time.time() - t1 >= (10000 - level * 4) / 5030:
                player_data["max_mult"] -= level * 4 if player_data["max_mult"] >= 0 else 0
                x, y = enemy_1.body.position
                proj.append(create_proj_spr(screen, (x - 50, y),
                                            angel=enemy_1.body.angle + 3.15, speed=game_data['ships_i'][2], c=80,
                                            damage=player_data["e_damage"]))

                proj.append(create_proj_spr(screen, (x - 75, y),
                                            angel=enemy_1.body.angle + 3.15, speed=game_data['ships_i'][2], c=80,
                                            damage=player_data["e_damage"]))
                t1 = time.time()
        if enemy_2_data[0] >= 0:
            enemy_2.draw_func()
            if time.time() - t2 >= (10000 - level * 4) / 5400:
                player_data["max_mult"] -= level * 4 if player_data["max_mult"] >= 0 else 0
                x, y = enemy_2.body.position
                proj.append(create_proj_spr(screen, (x - 50, y),
                                            angel=enemy_2.body.angle + 3.15, speed=game_data['ships_i'][2], c=80))
                t2 = time.time()

        if enemy_0_data[0] <= 0:
            enemy_0.body.position = (10000, -1000)

        if enemy_1_data[0] <= 0:
            if item_exist[1]:
                item_exist[0] = True
            item_sp.body.position = (screen.width / 2, screen.height / 2)
            item_sp.body.velocity = enemy_1.body.velocity
            enemy_1.body.position = (10000, -1000)

        if enemy_2_data[0] <= 0:
            enemy_2.body.position = (10000, -1000)

        if player_sprite.body.position[0] <= -1:
            home()

        if player_data["hp"] <= 0:
            home()

        if enemy_0.body.position[0] <= -1 or enemy_1.body.position[0] <= -1 or enemy_2.body.position[0] <= -1:
            if level == 0:
                home()
            else:
                level -= 1
                enemy_0.body.position = (1100, 600)
                enemy_1.body.position = (1100, 400)
                enemy_2.body.position = (1100, 200)
                player_sprite.body.position = (1200, screen.height / 2)

        list(map(lambda sprite_: sprite_.draw_func(), player_data["items"]))

        mouse.show_m(False)
        pygame.display.update()
        # pygame.display.flip()


def start_frame(tog=False):
    def set_bars():
        p0, c0 = pos_setter_bar(game_data["ships_i"][0])
        p1, c1 = pos_setter_bar(game_data["ships_i"][1])
        p2, c2 = pos_setter_bar(game_data["ships_i"][2])
        p3, c3 = pos_setter_bar(game_data["ships_i"][3])

        damage_line.point2 = (762 + p0 * 10, 256)
        resistance_line.point2 = (762 + p1 * 10, 189)
        nitro_line.point2 = (762 + p2 * 10, 124)
        hp_line.point2 = (762 + p3 * 10, 59)

        damage_line.set_color(c0)
        resistance_line.set_color(c1)
        nitro_line.set_color(c2)
        hp_line.set_color(c3)

    # Open a Window -
    text = Text(screen)
    text.init_font()
    run = True
    if tog:
        bg_statick_img.lode_new("Start2")
    else:
        bg_statick_img.lode_new("Start")

    items = []
    positions = [(337, 258),
                 (405, 258),
                 (468, 258),
                 (535, 258),
                 (600, 255),
                 (602, 190),
                 (602, 123),
                 (603, 60),
                 (336, 189),
                 (399, 189),
                 (470, 189),
                 (533, 190),
                 (340, 126),
                 (404, 123)]
    names = ["I1", "I2", "I3", "I4", "P1", "P2", "P3", "P4", "I_E0", "I_E1", "I_E2", "I_E3", "I_E4", "I_E5"]
    for i in range(14):
        item = Sprite(screen, "Item_holder").make_sprite("img", 60 + i, file=game_data[names[i]], position=positions[i],
                                                         physics=False, moment=50, mass=50)
        items.append(item)

    ships = [game_data["E0"],
             game_data["E1"],
             game_data["E2"],
             game_data["E3"],
             game_data["E4"],
             game_data["E5"]]

    stats = [game_data["items"][i][1] for i in range(6)]  # [[2, 1, 1, 8],
    # [1, 10, 3, 4],
    # [15, 0, 1, 10],
    # [8, 4, 1, 8],
    # [3, 1, 1, 8],
    # [2, 1, 1, 12]]

    game_data["ships_i"] = stats[s_num[0]]

    ship = Sprite(screen, "show_player").make_sprite("img",
                                                     file=ships[s_num[0]], position=(638, 550),
                                                     physics=False, moment=50, mass=50)

    sh_item = Sprite(screen, "show_player").make_sprite("img",
                                                        file=game_data["I0"], position=(353, 427),
                                                        physics=False, moment=50, mass=50)

    p, c = pos_setter_bar(game_data["ships_i"][0])

    damage_line = Sprite(screen, "damage").make_sprite("line", width=15, point1=(760, 256),
                                                       point2=(762 + p * 10, 256),
                                                       physics=False, moment=50, mass=50, color=c)

    p, c = pos_setter_bar(game_data["ships_i"][1])

    resistance_line = Sprite(screen, "damage").make_sprite("line", width=15, point1=(760, 189),
                                                           point2=(762 + p * 10, 189),
                                                           physics=False, moment=50, mass=50, color=c)

    p, c = pos_setter_bar(game_data["ships_i"][2])

    nitro_line = Sprite(screen, "damage").make_sprite("line", width=15, point1=(760, 124),
                                                      point2=(762 + p * 10, 124),
                                                      physics=False, moment=50, mass=50, color=c)

    p, c = pos_setter_bar(game_data["ships_i"][3])

    hp_line = Sprite(screen, "damage").make_sprite("line", width=15, point1=(760, 59),
                                                   point2=(762 + p * 10, 59),
                                                   physics=False, moment=50, mass=50, color=c)

    poses = [(525, 365),
             (564, 365),
             (611, 365),
             (657, 365),
             (696, 365),
             (740, 365)]

    dot = Sprite(screen, "dot").make_sprite(type_="circle", color="red", radius=5, position=poses[0], physics=False)

    sprites = [ship, sh_item, damage_line, resistance_line, nitro_line, hp_line, dot] + player_data["items"] + items
    ship.body.angle = 0.6
    d = 0
    ac_pris = 0
    item_index = 0
    item_ac = False
    info_text = ""

    i = 0
    for item_inv in player_data["items"]:
        item_inv.body.position = game_data["i_pos"][1][i]
        i += 1

    while run:
        bg.draw()
        bg_statick_img.draw()

        # using clock to cap fps
        dt = clock.tick(fps) / 10
        #space.step(1 / fps)
        # dt control movement speed

        # starting event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit(0)

            if pygame.mouse.get_pressed(3)[0]:
                #print("#" * 10, "\n")
                #print(pygame.mouse.get_pos(), "TEXT")
                #print(parser(pygame.mouse.get_pos(), screen.height))
                if not tog:
                    tog = True
                    bg_statick_img.lode_new("Start2")
                else:
                    x, y = parser(pygame.mouse.get_pos(), screen.height)
                    mouse_vec = Vector2(x, y)
                    play_vec = Vector2(940, 663)
                    if mouse_vec.distance_to(play_vec) <= 40:
                        if player_data['inventar']['ships'][d] > 0:
                            game_data["damage"] = game_data["ships_i"][0]
                            player_data["max_mult"] = game_data["ships_i"][2]
                            play()

                    lb = Vector2(760, 536)
                    if mouse_vec.distance_to(lb) <= 40:
                        d = ships.index(ship.img) + 1 if ships.index(ship.img) < len(ships) - 1 else 0
                        ship.img = ships[ships.index(ship.img) + 1 if ships.index(ship.img) < len(ships) - 1 else 0]
                        game_data["ships_i"] = stats[d]
                        set_bars()
                        s_num[0] = d

                    rb = Vector2(520, 534)
                    if mouse_vec.distance_to(rb) <= 40:
                        d = ships.index(ship.img) - 1 if ships.index(ship.img) != 0 else 5
                        ship.img = ships[d]
                        game_data["ships_i"] = stats[d]
                        set_bars()
                        s_num[0] = d

                    buy_item = Vector2(355, 498)
                    if mouse_vec.distance_to(buy_item) <= 40:
                        info_text = f"Du hast nicht Genügend Geld oder Platz"
                        if player_data["Bitcoins"] >= ac_pris and item_ac and item_index < 6:
                            player_data["Bitcoins"] -= ac_pris
                            #print(item_ac[0][0])
                            if "ship" in item_ac[0][0]:
                                player_data["inventar"]["ships"][int(item_ac[0][0][-1])] += 1
                                info_text = f"{item_ac[0][0]} wurde dem Invetar hinzugefügt"
                            else:
                                player_data["items"][item_index].img = game_data[item_ac[0][-1]]
                                #print(player_data["items"][item_index].body.position)
                                player_data["inventar"]["items"][item_index] = item_ac
                                info_text = f"Item wurde gekauft {item_ac[0][0]}"
                                sh_item.img = game_data["I0"]
                                if "powerUp" in item_ac[0][0]:
                                    stats[d][0] += item_ac[0][1]
                                    stats[d][1] += item_ac[0][2]
                                    stats[d][2] += item_ac[0][3]
                                    stats[d][3] += item_ac[0][4]
                                    set_bars()
                                item_index += 1
                                if item_index > 5:
                                    pass
                                else:
                                    dot.body.position = poses[item_index]
                            item_ac = False

                    sell_item = Vector2(938, 495)
                    if mouse_vec.distance_to(sell_item) <= 40:
                        info_text = "Kein Item augewählt zum verkaufen"
                        if item_index > 0:
                            item_index -= 1
                            player_data["Bitcoins"] += ac_pris * 0.8
                            info_text = f"Item wurde verkauft "
                            player_data["items"][item_index].img = game_data["I0"]
                            item_ac = False
                            dot.body.position = poses[item_index]
                            if "powerUp" in player_data["inventar"]["items"][item_index][0][0]:
                                stats[d][0] -= player_data["inventar"]["items"][item_index][0][1]
                                stats[d][1] -= player_data["inventar"]["items"][item_index][0][2]
                                stats[d][2] -= player_data["inventar"]["items"][item_index][0][3]
                                stats[d][3] -= player_data["inventar"]["items"][item_index][0][4]
                                set_bars()

                    for i in range(14):
                        x_, y_ = positions[i]
                        iv = Vector2(x_, y_)
                        if mouse_vec.distance_to(iv) <= 20:
                            info_text = ""
                            ac_pris = game_data['price_i'][i]
                            item_in_ew = names[i]
                            #print(item_in_ew)
                            item_ac = [i for i in game_data["items"] if item_in_ew in i]
                            sh_item.img = game_data[item_in_ew]

        text.show(f"Fps {100 / dt:.1f}", (screen.width - 220, 10), (255, 255, 255))
        text.show(f"X {player_data['inventar']['ships'][s_num[0]]}", (675, 78), (255, 255, 255))
        text.show(f"$ {player_data['Bitcoins']:.2f}", (screen.width - 220, 30), (255, 255, 255))
        text.show(f"Item~$ {ac_pris:.1f}", (screen.width - 220, 50), (255, 255, 255))

        text.show(f"{game_data['ships_i'][0]}", (865, 440), (255, 255, 255))
        text.show(f"{game_data['ships_i'][1]}", (865, 505), (255, 255, 255))
        text.show(f"{game_data['ships_i'][2]}", (865, 570), (255, 255, 255))
        text.show(f"{game_data['ships_i'][3]}", (865, 640), (255, 255, 255))

        text.show(f"{info_text}", (451, 389), (255, 255, 255))

        if tog:
            list(map(lambda sprite_: sprite_.draw_func(), sprites))
        # print(360 % angel)
        pygame.display.update()
        # pygame.display.flip()


def load_assets():
    sprite_sheet_data = {
        "width": 192,
        "height": 160,
        "default": (0, 0, 64, 64),
        "in_to_game": (64, 0, 64, 64),
        "choose_Ship": (128, 0, 64, 64),
        "Hud": (0, 80, 64, 64),
        "I0": (154, 140, 32, 32),
    }

    sprite_sheet = Sheet("img/BGs-modified.png", sprite_sheet_data)  # Sheet
    z = 11
    game_data["start"] = sprite_sheet.make_new_sheet_img("default", img_size=z)
    game_data["in_to_game"] = sprite_sheet.make_new_sheet_img("in_to_game", img_size=z)
    game_data["choose_Ship"] = sprite_sheet.make_new_sheet_img("choose_Ship", img_size=z)
    game_data["Hud"] = sprite_sheet.make_new_sheet_img("Hud", img_size=z)

    game_data["I0"] = sprite_sheet.make_new_sheet_img("I0", img_size=.5)

    bg_statick_img.load_statick_img("Start2", game_data["choose_Ship"])
    bg_statick_img.load_statick_img("Start", game_data["start"])
    bg_statick_img.load_statick_img("Hud", game_data["Hud"])

    sprite_sheet_data = {
        "width": 160,
        "height": 288,
        "default": (128, 0, 32, 32),
        "E1": (96, 64, 32, 32),
        "E2": (96, 96, 32, 32),
        "E3": (128, 96, 32, 32),
        "E4": (64, 128, 32, 32),
        "E5": (96, 128, 32, 32),

        "C1": (0, 192, 32, 32),
        "C2": (32, 192, 32, 32),
        "C2_op": (64, 192, 32, 32),
        "C-dy": (96, 192, 32, 32),

        "I1": (64, 224, 32, 32),
        "I2": (96, 224, 32, 32),
        "I3": (128, 224, 32, 32),
        "I4": (0, 256, 32, 32),

        "I-1": (32, 256, 32, 32),
        "I-2": (64, 256, 32, 32),

        "P1": (128, 32, 32, 32),
        "P2": (0, 64, 32, 32),
        "P3": (32, 64, 32, 32),
        "P4": (64, 64, 32, 32),
    }

    sprite_sheet = Sheet("img/assetspng.png", sprite_sheet_data, color_key=(138, 138, 138))  # Sheet
    z = 3
    a, b = 0, 0
    game_data["E0"] = sprite_sheet.make_new_sheet_img("default", anker=(a, b), img_size=z)
    game_data["E1"] = sprite_sheet.make_new_sheet_img("E1", anker=(a, b), img_size=z)
    game_data["E2"] = sprite_sheet.make_new_sheet_img("E2", anker=(a, b), img_size=z)
    game_data["E3"] = sprite_sheet.make_new_sheet_img("E3", anker=(a, b), img_size=z)
    game_data["E4"] = sprite_sheet.make_new_sheet_img("E4", anker=(a, b), img_size=z)
    game_data["E5"] = sprite_sheet.make_new_sheet_img("E5", anker=(a, b), img_size=z)

    game_data["I1"] = sprite_sheet.make_new_sheet_img("I1", anker=(a, b), img_size=z - 1)
    game_data["I2"] = sprite_sheet.make_new_sheet_img("I2", anker=(a, b), img_size=z - 1)
    game_data["I3"] = sprite_sheet.make_new_sheet_img("I3", anker=(a, b), img_size=z - 1)
    game_data["I4"] = sprite_sheet.make_new_sheet_img("I4", anker=(a, b), img_size=z - 1)

    game_data["C1"] = sprite_sheet.make_new_sheet_img("C1", anker=(a, b), img_size=z)
    game_data["C2"] = sprite_sheet.make_new_sheet_img("C2", anker=(a, b), img_size=z)

    z = .5
    game_data["P1"] = sprite_sheet.make_new_sheet_img("P1", anker=(a, b), img_size=z)
    game_data["P2"] = sprite_sheet.make_new_sheet_img("P2", anker=(a, b), img_size=z)
    game_data["P3"] = sprite_sheet.make_new_sheet_img("P3", anker=(a, b), img_size=z)
    game_data["P4"] = sprite_sheet.make_new_sheet_img("P4", anker=(a, b), img_size=z)

    z = 1
    game_data["I_E0"] = sprite_sheet.make_new_sheet_img("default", anker=(a, b), img_size=z)
    game_data["I_E1"] = sprite_sheet.make_new_sheet_img("E1", anker=(a, b), img_size=z)
    game_data["I_E2"] = sprite_sheet.make_new_sheet_img("E2", anker=(a, b), img_size=z)
    game_data["I_E3"] = sprite_sheet.make_new_sheet_img("E3", anker=(a, b), img_size=z)
    game_data["I_E4"] = sprite_sheet.make_new_sheet_img("E4", anker=(a, b), img_size=z)
    game_data["I_E5"] = sprite_sheet.make_new_sheet_img("E5", anker=(a, b), img_size=z)

    sprite_sheet_data2 = {
       "0": (64, 160, 32, 32),
       "1": (96, 160, 32, 32),
       "2": (128, 160, 32, 32),
    }

    for i in range(10):
        a = Animation(screen=screen, name="test", file="img/assetspng.png", sprite_sheet_info=sprite_sheet_data,
                  color_key=(138, 138, 138))
        a.make_new_animation("explosion", sprite_sheet_data2)
        game_data["expo"].append(a)


#
# warp_alim.make_new_animation("warp", sprite_sheet_data2, size=3)


if __name__ == '__main__':
    # starting Game
    screen = Screen(width=1280, height=720, title="Pong")
    bg_statick_img = Map(screen, "statick-img", color=(125, 125, 125))
    bg = Map(screen, "dynamic-img")
    bg.load_dynamic_img("v1", "img/testBG.png")
    s_num = [0]
    fps = 25

    game_data = {"ships_i": [2, 1, 1, 8], "damage": 1.2, "types": -1, "expo": [], "i_pos":
        [[(341, 121), (382, 120),
          (426, 119),
          (472, 121),
          (516, 120),
          (558, 122), ],
         [(498, 406),
          (549, 406),
          (591, 406),
          (634, 407),
          (679, 407),
          (725, 409)
          ]], "items": [
        ["ship0", [2, 1, 1, 8], "I_E0"], ["ship1", [1, 10, 3, 4], "I_E1"],
        ["ship2", [30, 4, 35, 40], "I_E2"], ["ship3", [8, 4, 1, 8], "I_E3"],
        ["ship4", [15, 0, 5, 10], "I_E4"], ["ship5", [99, 99, 99, 99], "I_E5"],

        ["projectile1", 400, 1, "P1"], ["projectile2", 600, 5, "P2"],
        ["projectile3", 800, 20, "P3"], ["projectile4", 1200, 99, "P4"],

        ["powerUp1", 10, -2, 5, 4, "I1"], ["powerUp2", 0, 20, 12, -5, "I2"],
        ["powerUp3", 0, -5, 30, -10, "I3"], ["powerUp4", 1, 0, 0, 1, "I4"],

    ], "price_i": [130, 350, 999, 30, 0.9, 5, 90, 70, 200, 400, 900, 600, 500, 1999]}
    load_assets()
    player_data = {
        "e_damage": 1,
        "score": 0,
        "hp": 100,
        "max_mult": 2,
        "bullets": 0,
        "Bitcoins": 10,
        "items": [Sprite(screen, f"Item_holder-{i}").make_sprite("img", 1,
                                                                 file=game_data["I0"],
                                                                 position=game_data["i_pos"][1][i],
                                                                 physics=False, moment=50, mass=50) for i in range(6)],
        "inventar": {"ships": [2, 1, 1, 1, 0, 0, 0, 0], "items": [-1, -1, -1, -1, -1, -1]}
    }

    # for sprite in player_data["items"]:
    #    sprite.debug_img_rot_draw = True

    start_frame()
