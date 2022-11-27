# std lib
import sys

# local
from settings import *  # includes pygame as pg
from stacked_sprite import StackedSprite
from cache import Cache
from player import Player
from scene import Scene

class App:
    def __init__(self):
        self.win = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.time = 0
        self.dt = 0.01  # delta time
        # groups - Using LayeredUpdates has a peculiarity that allows for simple y-sorting
        # Each sprite has a private layer attr self._layer that just determines draw order
        # See change_layer() in the StackedSprite class
        self.main_group = pg.sprite.LayeredUpdates()
        # load prerendered game objects
        self.cache = Cache()
        # player and world
        self.player = Player(self)
        self.scene = Scene(self)


    def update(self):
        self.main_group.update()
        pg.display.set_caption(f'{self.clock.get_fps(): .1f}')
        self.dt = self.clock.tick()


    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001  # ms


    def draw(self):
        self.win.fill(BG_COLOR)
        self.main_group.draw(self.win)
        pg.display.flip()


    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()


    def run(self):
        while True:
            self.check_events()
            self.get_time()
            self.update()
            self.draw()


if __name__ == '__main__':
    app = App()
    app.run()
