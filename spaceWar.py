from typing import List

from util.MGameM import Screen, Sprite, Text, Mouse, Physics, clock  # import custom
import pygame


class Projectiles:

    def __init__(self, projectiles_list: List[Sprite]):
        self.projectiles = projectiles_list
        self.ac_enemies = []

    def spawn_projectile(self, index: int):
        self.ac_enemies.append(self.projectiles[index])

    def kill_projectile(self, index: int):
        self.ac_enemies.remove(self.projectiles[index])


class Enemies:

    def __init__(self, enemies_list: List[Sprite]):
        self.enemies = enemies_list
        self.ac_enemies = []
        self.hp = [0] * len(enemies_list)

    def spawn_enemy(self, index: int):
        self.ac_enemies.append(self.enemies[index])

    def kill_enemy(self, index: int):
        self.ac_enemies.remove(self.enemies[index])

    def shoot(self, player: Sprite):
        projectile_list = []
        for enemy in self.ac_enemies:

            x = player.x - enemy.x
            y = player.y - enemy.y
            projectile_list.append((x, y))


def functional():
    # Open a Window -
    screen = Screen(width=812, height=624, background='black', title="Pong")

    # init Sprites blueprint
    sprites = []
    game_pad_width = 30
    game_pad_height = 120

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

    sprite_sheet = Sprite(screen, "sprite_sheet")  # sheet
    player_sprite = Sprite(screen, "player")  # img

    sprite_sheet.make_sprite("sheet", -1, sheet_data=sprite_sheet_data, file="img/spaceWarAssets.png")
    player_sprite.make_sprite("img", 1, player_wh[0], player_wh[1], file="img/spaceWarAssets.png")
    player_sprite.img = sprite_sheet.set_new_sheet_img("player", img_size=0.3)

    # make projectile

    num_of_max_projectile = 200
    projectiles_list = []

    for i in range(num_of_max_projectile):
        projectile = Sprite(screen, f"projectile{i}")
        projectile.make_sprite("circle", 1, radius=10, color="red")
        projectiles_list.append(projectile)
        i += 1

    projectiles = Projectiles(projectiles_list)

    # make enemies
    num_of_max_enemies1 = 8
    num_of_max_enemies2 = 4

    enemies1_list = []
    enemies2_list = []

    for i in range(num_of_max_enemies1):
        enemy1 = Sprite(screen, f"enemy1_{i}")
        enemy1.make_sprite("img", 1, player_wh[0], player_wh[1], file="img/spaceWarAssets.png")
        enemy1.img = sprite_sheet.set_new_sheet_img("enemy1")
        enemies1_list.append(enemy1)

    for i in range(num_of_max_enemies2):
        enemy2 = Sprite(screen, f"enemy1_{i}")
        enemy2.make_sprite("img", 1, player_wh[0], player_wh[1], file="img/spaceWarAssets.png")
        enemy2.img = sprite_sheet.set_new_sheet_img("enemy2")
        enemies2_list.append(enemy2)

    enemies1 = Enemies(enemies1_list)
    enemies2 = Enemies(enemies2_list)

    # add sprites to sprites array

    ac_enemies = []
    ac_projectiles = []

    # init Text
    text_score = Text(screen)
    text_score.init_font(15)

    text_info = Text(screen)
    text_info.init_font(15)

    # init Mouse
    mouse = Mouse(screen, None)

    # game vars

    score = 0
    hp = 100
    bullets = 0

    wave = 0

    angel = 0

    run = True
    while run:

        angel += 1

        screen.surface.fill(screen.background)

        # using clock to cap fps
        dt = clock.tick(25) / 10
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

                    if event.key == pygame.K_LEFT:
                        pass

                    if event.key == pygame.K_RIGHT:
                        pass

                    if event.key == pygame.K_UP:
                        pass

                    if event.key == pygame.K_DOWN:
                        pass

        player_sprite.draw_func()
        player_sprite.rotate(angel)

        # print(360 % angel)

        mouse.show_m(False)
        pygame.display.update(player_sprite.img)
        #pygame.display.flip()


if __name__ == '__main__':
    # starting Game
    functional()
