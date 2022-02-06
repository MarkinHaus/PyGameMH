from util.MGameM import Screen, Sprite, Text, Mouse, clock, space, Map
import random
import pygame


def functional():
    # Open a Window -
    screen = Screen(width=1236, height=512, title="Pong")

    background_map = Map(screen, "statick", color=(0, 0, 0))  # statick statick-img dynamic-img

    # -------------------ball----------------#
    ball = Sprite(screen, "ball")  # ball
    ball.make_sprite(type_="circle", radius=10, color="white", collisions_level=1,
                     position=(screen.width, screen.height / 2),
                     velocity=(-240, 40),
                     mass=10,
                     moment=10,
                     elasticity=1, physics=True)

    # -------------------init Text----------------#
    text = Text(screen)
    text.init_font()

    # -------------------init Mouse----------------#
    mouse = Mouse(screen, None)

    # -------------------make sprite array----------------#
    sprites = [ball]  # _l, border_r, border_t, border_b]

    # -------------------ADDING OBJECTS IN TO WORLD----------------#

    ball.add_to_space(space)

    # list(
    #    map(
    #        lambda sprite_: sprite_.add_to_space(space)
    #        , sprites
    #    )
    # )
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
        # -------------------print score----------------#
        text.show(f"TEXT", (screen.width - 180, 60), (255, 255, 255))

        # -------------------drawing sprites to screen---------------#

        # list(map(lambda sprite_: sprite_.draw_func(), sprites))

        ball.draw_func()
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
