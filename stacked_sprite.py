# std lib
import math

# local
from settings import *

class StackedSprite(pg.sprite.Sprite):
    def __init__(self, app, name, pos):
        self.app = app
        self.name = name
        self.pos = vec2(pos)
        self.player = app.player
        self.group = app.main_group
        super().__init__(self.group) # init sprite into sprite group

        self.attrs = STACKED_SPRITE_ATTRS[name]
        self.cache = app.cache.stacked_sprite_cache
        self.viewing_angle = app.cache.viewing_angle
        self.rotated_sprites = self.cache[name]['rotated_sprites']  # {angle: rotated image}
        self.angle = 0
        self.screen_pos = vec2(0)


    def update(self):
        self.transform()
        self.get_angle()
        self.get_image()


    def transform(self):
        # shift the object according to player's offset
        pos = self.pos - self.player.offset
        # Rotate the vector by the player's angle
        pos = pos.rotate_rad(self.player.angle)
        # offset from center of screen
        self.screen_pos = pos + CENTER


    def get_angle(self):
        self.angle = -math.degrees(self.player.angle) // self.viewing_angle
        # get index of the angle for dictionary key lookup
        self.angle = int(self.angle % NUM_ANGLES)


    def get_image(self):
        # get corresponding cached image (surface with properly blitted sprites)
        self.image = self.rotated_sprites[self.angle]
        # CENTER offset keeps (0,0) center of screen - player offset moves world around the player
        self.rect = self.image.get_rect(center = self.screen_pos)
        

    

