# local
from settings import *
import time
# build a dictionary of cached sprite layers at every viewing angle to improve performance
class Cache:
    def __init__(self):
        self.stacked_sprite_cache = {}
        self.viewing_angle = 360 // NUM_ANGLES
        self.get_stacked_sprite_cache()


    def get_stacked_sprite_cache(self):
        # build a dictionary of rotated sprites for future convenience
        for obj_name in STACKED_SPRITE_ATTRS:
            self.stacked_sprite_cache[obj_name] = {
                'rotated_sprites': {}
            }
            # build layer array from obj attributes, send to prerender
            attrs = STACKED_SPRITE_ATTRS[obj_name]
            layer_array = self.get_layer_array(attrs)
            self.run_prerender(obj_name, layer_array, attrs)


    def run_prerender(self, obj_name, layer_array, attrs):
        # limit rotation to discreet intervals set by NUM_ANGLES, for performance
        for angle in range(NUM_ANGLES):
            # create transparent surf with height increased by number of layers * scaling
            # allows room for the y-shift for sprite stacking effect
            surf = pg.Surface(layer_array[0].get_size())        
            surf = pg.transform.rotate(surf, angle * self.viewing_angle)  # first rotate surface by the view angle
            sprite_surf = pg.Surface([surf.get_width(), 
                                        surf.get_height() + attrs['num_layers'] * attrs['scale']])

            # CLEVER PERFORMANCE TRICK - instead of flagging the surf with pg.SRCALPHA to preserve transparency
            sprite_surf.fill('khaki')  # we fill the surf with a color we won't use
            sprite_surf.set_colorkey('khaki')  # then make that color transparent

            # blit the layer slices on the surface, stacked with set scaling
            for i, layer in enumerate(layer_array):
                # rotate layer by the view angle
                layer = pg.transform.rotate(layer, angle * self.viewing_angle)
                sprite_surf.blit(layer, (0, i * attrs['scale']))

            # flip image b/c pygame uses downward-positive y-axis - mirror x-axis to maintain CW rotation
            image = pg.transform.flip(sprite_surf, True, True)
            # add to dictionary --> {key: angle, value: blitted surf rotated by angle}
            self.stacked_sprite_cache[obj_name]['rotated_sprites'][angle] = image
            

    def get_layer_array(self, attrs):
        # load sprite sheet
        sprite_sheet = pg.image.load(attrs['path']).convert_alpha()

        # scaling via scalar multiplication
        sprite_sheet = pg.transform.scale(sprite_sheet, vec2(sprite_sheet.get_size()) * attrs['scale'])
        sheet_width = sprite_sheet.get_width()
        sheet_height = sprite_sheet.get_height()
        # the sprite sheet is vertically arranged; derive layer height from num_layers
        sprite_height = sheet_height // attrs['num_layers']
        # revert to the sum of each layer's height for sheet height to prevent error from possible decimal trunctation
        sheet_height = sprite_height * attrs['num_layers']
        # get sprite layers by slicing the sprite sheet
        layer_array = []
        for y in range(0, sheet_height, sprite_height):
            sprite = sprite_sheet.subsurface(0, y, sheet_width, sprite_height)
            layer_array.append(sprite)
        # return layers in reverse order b/c they're drawn from bottom up on the sprite sheet
        return layer_array[::-1]