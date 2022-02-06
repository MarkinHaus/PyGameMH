import pygame
import sys
import random
from util.MGameM import Screen, Sprite, clock, space, Map


def convert_coordinates(pos):
    return int(pos[0]), 900 - int(pos[1])


def create_apple_spr(color=(200, 20, 15)):
    appel = Sprite(screen, f"appel{len(apples)}")
    appel.make_sprite(type_="circle", color=color, radius=9, position=(350 + random.randint(0, 100), 600),
                      physics=True, mass=150, elasticity=.4)
    appel.add_to_space(space)
    return appel


screen = Screen(width=800, height=900, title="test")

bg = Map(screen, "statick", (212, 212, 212))

space.gravity = (0, -300)

apples = []

sprite4 = Sprite(screen, "top1")
sprite4.debug_img_rot_draw = True
sprite4.make_sprite("img", elasticity=1,
                    position=(400, 1200), physics=True, velocity=(20, 10),
                    file="img/testIB.png")


top_1 = Sprite(screen, "top1")
top_1.make_sprite(type_="rect", width=screen.width - 420, color="black",
                  height=15, position=(400, 60))

top_2 = Sprite(screen, "top2")
top_2.make_sprite(type_="line", width=5, point1=(240, 400), point2=(240, 60), color="black")

top_3 = Sprite(screen, "top3")
top_3.make_sprite(type_="line", width=5, point1=(640, 400), point2=(640, 60), color="black")

top_1.add_to_space(space)
top_2.add_to_space(space)
top_3.add_to_space(space)
sprite4.add_to_space(space)

# k = 5000
pygame.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    bg.draw()

    top_1.draw_func()
    top_2.draw_func()
    top_3.draw_func()
    sprite4.draw_func()

    # ap_arr = d[i]

    apples.append(create_apple_spr())
    apples.append(create_apple_spr())
    apples.append(create_apple_spr())
    apples.append(create_apple_spr())
    apples.append(create_apple_spr())
    apples.append(create_apple_spr())
    apples.append(create_apple_spr())

    pygame.draw.circle(screen.surface, (0, 255, 15),
                       (int(top_1.body.position[0]), int(screen.height - top_1.body.position[1])), 5)

    pygame.draw.circle(screen.surface, (0, 255, 150),
                       (int(top_1.body.position[0] + top_1.width / 2), int(screen.height - top_1.body.position[1])), 5)

    for ap in apples:
        ap.draw_func()

    pygame.display.flip()
    clock.tick(30)
    space.step(1 / 30)
