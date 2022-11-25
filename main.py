# std lib
import sys

# reqs
import pygame as pg

# local
from settings import *
from stacked_sprite import StackedSprite

class App:
    def __init__(self):
        self.win = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.time = 0
        self.dt = 0.01  # delta time
        # groups
        self.main_group = pg.sprite.Group()

        # test
        StackedSprite(self, 'rect', CENTER, self.main_group)


    def update(self):
        self.main_group.update()
        pg.display.set_caption(f'{self.clock.get_fps(): .1f}')
        self.dt = self.clock.tick()


    def draw(self):
        self.win.fill(BG_COLOR)
        self.main_group.draw(self.win)
        pg.display.flip()


    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()


    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001  # ms


    def run(self):
        while True:
            self.check_events()
            self.get_time()
            self.update()
            self.draw()


if __name__ == '__main__':
    app = App()
    app.run()
