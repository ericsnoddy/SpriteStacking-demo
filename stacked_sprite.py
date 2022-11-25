# std lib
import math

# local
from settings import *

class StackedSprite(pg.sprite.Sprite):
    def __init__(self, app, name, pos, group):
        self.app = app
        self.name = name
        self.pos = vec2(pos)
        self.group = group
        super().__init__(self.group)

        self.image = pg.Surface([200, 200])
        self.image.fill('orange')
        self.rect = self.image.get_rect(center = pos)