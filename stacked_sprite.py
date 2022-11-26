# std lib
import math

# local
from settings import *

class StackedSprite(pg.sprite.Sprite):
    def __init__(self, app, name, pos):
        self.app = app
        self.name = name
        self.pos = vec2(pos)
        self.group = self.app.main_group
        super().__init__(self.group) # init sprite into sprite group

        self.attrs = STACKED_SPRITE_ATTRS[self.name]
        self.layer_array = self.get_layer_array()


    def update(self):
        self.get_image()


    def get_image(self):
        # create transparent surf with height increased by number of layers * scaling
        # allows room for the y-shift for sprite stacking effect
        surf = pg.Surface(self.layer_array[0].get_size())
        sprite_surf = pg.Surface([surf.get_width(), 
                                    surf.get_height() + self.attrs['num_layers'] * self.attrs['scale']], pg.SRCALPHA)

        # blit the layer slices on the surface stacked with set scaling
        for i, layer in enumerate(self.layer_array):
            sprite_surf.blit(layer, (0, i * self.attrs['scale']))

        self.image = sprite_surf
        # CENTER offset keeps (0,0) center of screen
        self.rect = self.image.get_rect(center = self.pos + CENTER)
        

    def get_layer_array(self):
        # load sprite sheet
        sprite_sheet = pg.image.load(self.attrs['path']).convert_alpha()

        # scaling via scalar multiplication
        sprite_sheet = pg.transform.scale(sprite_sheet, vec2(sprite_sheet.get_size()) * self.attrs['scale'])
        sheet_width = sprite_sheet.get_width()
        sheet_height = sprite_sheet.get_height()
        # the sprite sheet is vertically arranged; derive layer height from num_layers
        sprite_height = sheet_height // self.attrs['num_layers']
        # revert to the sum of each layer's height for sheet height to prevent error from possible decimal trunctation
        sheet_height = sprite_height * self.attrs['num_layers']
        # get sprite layers by slicing the sprite sheet
        layer_array = []
        for y in range(0, sheet_height, sprite_height):
            sprite = sprite_sheet.subsurface(0, y, sheet_width, sprite_height)
            layer_array.append(sprite)
        # return layers in reverse order b/c they're drawn from bottom up on the sprite sheet
        return layer_array[::-1]

