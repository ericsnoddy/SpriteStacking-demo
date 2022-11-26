import pygame as pg

vec2 = pg.math.Vector2
RES = WIDTH, HEIGHT = vec2(1280, 720)
CENTER = H_WIDTH, H_HEIGHT = RES // 2
BG_COLOR = (20, 30, 46)
NUM_ANGLES = 90  # must evenly divide 360; limit view angles to incr performance
PLAYER_SPEED = 0.4
PLAYER_ROT_SPEED = 0.0015

STACKED_SPRITE_ATTRS = {
    'van': {
        'path': 'assets/stacked_sprites/van.png',
        'num_layers': 20,
        'scale': 6,
    },
    'tank': {
        'path': 'assets/stacked_sprites/tank.png',
        'num_layers': 17,
        'scale': 10,
    }
}