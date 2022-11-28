# std lib
from random import uniform

# local
from stacked_sprite import *
from entity import Entity

P = 'player'
# entities
K = 'kitty'
# stacked sprites
A, B, C, D, E, F, S, X = 'blue_tree', 'car', 'tank', 'van', 'grass', 'pancake', 'sphere', 'crate'

MAP = [
    [0, 0, A, 0, 0, 0, A, 0, 0, 0, X, 0, 0, 0],
    [0, F, K, A, 0, 0, 0, 0, A, A, 0, F, 0, 0],
    [A, A, 0, 0, A, 0, D, D, E, A, S, 0, X, 0],
    [0, A, B, 0, 0, E, A, A, 0, A, A, F, 0, 0],
    [A, X, 0, B, P, E, 0, A, C, 0, A, 0, 0, 0],
    [0, A, 0, E, 0, D, K, C, 0, 0, A, 0, 0, 0],
    [0, A, A, 0, B, E, E, 0, C, A, A, 0, S, 0],
    [A, 0, 0, S, 0, 0, X, 0, 0, A, 0, A, X, 0],
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
                pos = vec2(i, j) + vec2(0.5)  # add half to each coord to get center
                if name == 'player':
                    self.app.player.offset = pos * TILE_SIZE
                elif name == 'kitty':
                    Entity(self.app, name, pos=rand_pos_func(pos))
                elif name == 'blue_tree':
                    StackedSpriteAlpha(self.app, name=name, pos=rand_pos_func(pos), rot=rand_rot_func())
                elif name:
                    StackedSprite(self.app, name=name, pos=rand_pos_func(pos), rot=rand_rot_func())


    def get_closest_obj_to_player(self):
        for sprite in self.app.transparent_objects:
            sprite.alpha_trigger = False
        closest_list = sorted(self.app.transparent_objects, key=lambda e: e.dist_to_player)
        for tree in range(4):
            closest_list[tree].alpha_trigger = True
        

    def update(self):
        self.get_closest_obj_to_player()
        