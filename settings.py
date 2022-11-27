import pygame as pg

vec2 = pg.math.Vector2
# RES = WIDTH, HEIGHT = vec2(1000, 600)
RES = WIDTH, HEIGHT = vec2(1280, 720)
CENTER = H_WIDTH, H_HEIGHT = RES // 2
TS = TILE_SIZE = 250

PLAYER_SPEED = 0.4
PLAYER_ROT_SPEED = 0.0015
NUM_ANGLES = 90  # must evenly divide 360; higher num = smoother rotation = longer prerender/load time

BG_COLOR = 'olivedrab'
BORDER_COLOR = 'black'
OUTLINE_THICKNESS = 4
ANIM_SPEED = 100  # ms per frame

# entity settings
ENTITY_SPRITE_ATTRS = {
    'player': {
        'path': 'assets/entities/player/player.png',
        'mask_path': 'assets/entities/player/mask.png',
        'num_layers': 7,
        'scale': 0.35,
        'y_offset': 0,
    },
    'kitty': {
        'path': 'assets/entities/cats/kitty.png',
        'num_layers': 8,
        'scale': 0.8,
        'y_offset': -20,
    },
    'explosion': {
        'num_layers': 7,
        'scale': 1.0,
        'path': 'assets/entities/explosion/explosion.png',
        'y_offset': 50,
    },
    'bullet': {
        'num_layers': 1,
        'scale': 0.4,
        'path': 'assets/entities/bullet/bullet.png',
        'y_offset': 50,
    },
}

STACKED_SPRITE_ATTRS = {
    'blue_tree': {
        'path': 'assets/stacked_sprites/blue_tree.png',
        'num_layers': 43,
        'scale': 8,
        'y_offset': -130,
    },
    'car': {
        'path': 'assets/stacked_sprites/car.png',
        'num_layers': 9,
        'scale': 10,
        'y_offset': 10,
    },
    'grass': {
        'path': 'assets/stacked_sprites/grass.png',
        'num_layers': 11,
        'scale': 7,
        'y_offset': 20,
        'outline': False,
    },
    'van': {
        'path': 'assets/stacked_sprites/van.png',
        'num_layers': 20,
        'scale': 6,
        'y_offset': 10,
    },
    'tank': {
        'path': 'assets/stacked_sprites/tank.png',
        'num_layers': 17,
        'scale': 8,
        'y_offset': 0,
    }
}