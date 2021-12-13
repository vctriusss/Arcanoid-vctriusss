import time
from constants import *
from Platform import Platform
from Ball import Ball
from block_patterns import *

pg.init()
pg.display.set_caption('Arcanoid')
img = pg.image.load('background.jpg')


def GameOverScenario():
    black = pg.Rect(int(0.3 * screen_width), int(0.45 * screen_height), 500, 150)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    exit()
                elif event.key == pg.K_r:
                    return True
        pg.draw.rect(screen, pg.Color('black'), black)
        screen.blit(text_gameover, (black.x + 10, black.y + 5))
        screen.blit(text_reload, (black.x + 10, black.y + 100))
        pg.display.flip()


def draw_objects(*args):
    for arg in args:
        if type(arg) != list:
            arg.draw()
        else:
            for block in arg:
                block.draw()


def game():
    platform = Platform()
    ball = Ball()
    block_pattern = choice(patterns)
    clock = pg.time.Clock()

    time_end = time.time() + 1
    while time.time() < time_end:
        screen.blit(img, (0, 0))
        draw_objects(platform, block_pattern)
        pg.display.flip()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
        key = pg.key.get_pressed()
        if key[pg.K_a] and platform.body.left > 0:
            platform.body.left -= platform.speed
        if key[pg.K_d] and platform.body.right < screen_width:
            platform.body.right += platform.speed
        if key[pg.K_ESCAPE]:
            exit()
        screen.blit(img, (0, 0))

        if ball.is_out():
            GameOverScenario()
            game()
        draw_objects(platform, ball, block_pattern)
        for block in block_pattern:
            block.hit_by(ball)
        ball.fly()
        ball.wall_bounce()
        platform.collision(ball)

        pg.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    game()
