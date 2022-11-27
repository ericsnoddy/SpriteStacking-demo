# std lib
from random import uniform

# local
from stacked_sprite import *

P = 'player'
A, B, C, D, E = 'blue_tree', 'car', 'tank', 'van', 'grass'

MAP = [
    [0, 0, A, 0, 0, 0, A, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, A, 0, 0, 0, 0, A, A, 0, 0, 0, 0],
    [A, A, 0, 0, A, 0, D, D, E, A, 0, 0, 0, 0],
    [0, A, B, 0, 0, E, A, A, 0, A, A, 0, 0, 0],
    [A, 0, 0, B, P, E, 0, A, C, 0, A, 0, 0, 0],
    [0, A, 0, E, 0, D, 0, C, 0, 0, A, 0, 0, 0],
    [0, A, 0, 0, B, E, E, 0, C, A, A, 0, 0, 0],
    [A, 0, 0, 0, 0, 0, 0, 0, 0, A, 0, 0, 0, 0],
    [0, 0, A, 0, A, A, 0, 0, 0, 0, 0, 0, 0, 0],
]

MAP_SIZE = MAP_WIDTH, MAP_HEIGHT = vec2(len(MAP), len(MAP[0]))
MAP_CENTER = MAP_SIZE / 2

class Scene:
    def __init__(self, app):
        self.app = app
        self.load_scene()


    def load_scene(self):
        # randomize rotation and position within the tile for aesthetics
        rand_pos_func = lambda pos: pos + vec2(uniform(-0.25, 0.25))
        rand_rot_func = lambda: uniform(0, 360)

        for j, row in enumerate(MAP):
            for i, name in enumerate(row):
                pos = vec2(i, j) + vec2(0.5)  # add half to each to get center
                if name == 'player':
                    self.app.player.offset = pos * TS
                elif name:
                    StackedSprite(self.app, name=name, pos=rand_pos_func(pos), rot=rand_rot_func())