# std lib
import math

# local
from settings import *

class StackedSprite(pg.sprite.Sprite):
    def __init__(self, app, name, pos):
        self.app = app
        self.name = name
        self.pos = vec2(pos)
        self.group = app.main_group
        super().__init__(self.group) # init sprite into sprite group

        self.attrs = STACKED_SPRITE_ATTRS[name]
        self.cache = app.cache.stacked_sprite_cache
        self.viewing_angle = app.cache.viewing_angle
        self.rotated_sprites = self.cache[name]['rotated_sprites']  # {angle: rotated image}
        self.angle = 0


    def update(self):
        self.get_angle()
        self.get_image()


    def get_angle(self):
        self.angle = -math.degrees(self.app.time) // self.viewing_angle
        # get index of the angle for dictionary key lookup
        self.angle = int(self.angle % NUM_ANGLES)


    def get_image(self):
        # get corresponding cached image (surface with properly blitted sprites)
        self.image = self.rotated_sprites[self.angle]
        # CENTER offset keeps (0,0) center of screen
        self.rect = self.image.get_rect(center = self.pos + CENTER)
        

    

