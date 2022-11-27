# local
from settings import *

class BaseEntity(pg.sprite.Sprite):
    def __init__(self, app, name):
        self.app = app
        self.name = name
        self.group = app.main_group
        super().__init__(self.group)

        self.attrs = ENTITY_SPRITE_ATTRS[name]
        entity_cache = self.app.cache.entity_sprite_cache
        self.images = entity_cache[name]['images']
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.frame_index = 0


    def update(self):
        self.animate()


    def animate(self):
        if self.app.anim_trigger:
            self.frame_index = (self.frame_index + 1) % len(self.images)
            self.image = self.images[self.frame_index]
