# std lib
import math

# local
from settings import *

class StackedSprite(pg.sprite.Sprite):
    def __init__(self, app, name, pos, rot=0):  # rot=degrees
        self.app = app
        self.name = name
        self.pos = vec2(pos) * TILE_SIZE  # multiply by TS for convient placement in grid structure; see Scene class
        self.player = app.player
        # init sprite into sprite group
        self.group = app.main_group
        super().__init__(self.group)
        
        # get obj attrs
        self.attrs = STACKED_SPRITE_ATTRS[name]
        # b/c sprites are different sizes, their height needs adjusted to make them all appear level; trial and error
        self.y_off = vec2(0, self.attrs['y_offset'])

        # get obj cache and init rotation vars
        self.viewing_angle = app.cache.viewing_angle
        self.cache = app.cache.stacked_sprite_cache        
        self.rotated_sprites = self.cache[name]['rotated_sprites']  # {key: angle deg, value: rendered rotated image}
        self.angle_key = 0  # using degrees for convenience
        self.screen_pos = vec2(0)
        # calc reqd angle offset in degs [0,360] for rotating objs rel to the world grid
        self.rot = (rot % 360) // self.viewing_angle


    def update(self):
        self.transform()
        self.get_angle()
        self.get_image()
        self.change_layer()


    def change_layer(self):
        # screen_pos is sprite's pos minus player offset, rotated by player angle, and offset from CENTER
        # we change each sprite's layer (draw order) based on it's screen_pos y-value
        # This has to be called once by Player init to make player center = CENTER
        self.group.change_layer(self, self.screen_pos.y)


    def transform(self):
        # shift the object according to player's offset
        pos = self.pos - self.player.offset
        # Rotate the vector by the player's angle (rads)
        pos = pos.rotate_rad(self.player.angle)
        # offset from center of screen
        self.screen_pos = pos + CENTER


    def get_angle(self):
        # each angle can be referenced by index 0=1st angle, 1=2nd angle, 89=last angle if NUM_ANGLES=90

        # About the negative sign... after laborious, step-by-step analysis I think I finally get it...
        # Truncating the number with '//' outputs 0 when angle is between [0,1) radian, and we don't want that
        # Python behavior with truncation of negative divsision returns next int toward negative infinity
        # Eg, 3.5 degs // 4 outputs 0.0, -3.5 // 4 outputs -1.0 -- and we can easily discard the negative
        # WE DO NOT WANT 0.0 after the first step unless player.angle = 0.0
        #### Orrrr... maybe the negative is just because pygame has reversed y-axes (negative is up)? Argh.
        discrete_angle = -math.degrees(self.player.angle) // self.viewing_angle + self.rot  # add the rotation offset
        # get index of the angle for dictionary key lookup
        self.angle_key = int(discrete_angle % NUM_ANGLES)


    def get_image(self):
        # get corresponding cached image (surface with properly blitted sprites)
        self.image = self.rotated_sprites[self.angle_key]
        # CENTER offset keeps (0,0) center of screen - player offset moves world around the player
        self.rect = self.image.get_rect(center = self.screen_pos + self.y_off)
        

    

