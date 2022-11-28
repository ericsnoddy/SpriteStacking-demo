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
        # custom event for triggering next frame of animations
        self.anim_trigger = False
        self.anim_event = pg.USEREVENT + 0
        pg.time.set_timer(self.anim_event, ANIM_SPEED)
        # groups - Using LayeredUpdates has a peculiarity that allows for simple y-sorting
        # Each sprite has a private layer attr self._layer that just determines draw order
        # See change_layer() in the StackedSprite class
        self.main_group = pg.sprite.LayeredUpdates()
        self.transparent_objects = []
        # load prerendered game objects
        self.cache = Cache()
        # player and world
        self.player = Player(self)
        self.scene = Scene(self)


    def update(self):
        self.scene.update()
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
        self.anim_trigger = False
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            # catch custom timer event to trigger next animation frame 
            elif e.type == self.anim_event:
                self.anim_trigger = True


    def run(self):
        while True:
            self.check_events()
            self.get_time()
            self.update()
            self.draw()


if __name__ == '__main__':
    app = App()
    app.run()
