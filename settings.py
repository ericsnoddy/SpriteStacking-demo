import pygame as pg

vec2 = pg.math.Vector2
RES = WIDTH, HEIGHT = vec2(1280, 720)
CENTER = H_WIDTH, H_HEIGHT = RES // 2
BG_COLOR = (20, 30, 46)

STACKED_SPRITE_ATTRS = {
    'van': {
        'path': 'assets/stacked_sprites/van.png',
        'num_layers': 20,
        'scale': 18,
    }
}