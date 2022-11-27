# std lib
from math import sqrt, pi

# reqs
from pygame.constants import *

# local
from settings import *
from entity import BaseEntity

class Player(BaseEntity):
    def __init__(self, app, name='player'):
        super().__init__(app, name)
        # init Player layer = CENTER.y b/c Player doesn't have screen_pos.y attr so won't be updated
        self.group.change_layer(self, CENTER.y)  
        self.rect = self.image.get_rect(center=CENTER)

        self.offset = vec2(0)
        self.incr = vec2(0)
        self.angle = 0  # radians


    def update(self):
        super().update()  # run update from inherited class (animate)
        self.control()
        self.move()

    
    def move(self):
        self.offset += self.incr

    
    def control(self):
        # reset Vector2 variable
        self.incr = vec2(0)
        # modify speed w.r.t. time since last frame for FPS-independent movement
        speed = PLAYER_SPEED * self.app.dt 
        rot_speed = PLAYER_ROT_SPEED * self.app.dt
        keys = pg.key.get_pressed()

        # rotation
        if keys[K_LEFT]:
            self.angle += rot_speed
        if keys[K_RIGHT]:
            self.angle -= rot_speed

        # linear movement
        # to correct directions being relative to rotated world, we rotate direction vec CCW by player angle
        if keys[K_w]:
            self.incr += vec2(0, -speed).rotate_rad(-self.angle)
        elif keys[K_s]:
            self.incr += vec2(0, speed).rotate_rad(-self.angle)
        if keys[K_a]:
            self.incr += vec2(-speed, 0).rotate_rad(-self.angle)
        elif keys[K_d]:
            self.incr += vec2(speed, 0).rotate_rad(-self.angle)

        # simple trig to normalize the direction vector so diagonals are not faster
        if self.incr.x and self.incr.y:
            self.incr *= 1 / sqrt(2)