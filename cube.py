from enum import Enum
import numpy as np

class Color(Enum):
    NONE = None
    UP = "U"
    RIGHT = "R"
    FRONT = "F"
    DOWN = "D"
    LEFT = "L"
    BACK = "B"

class Move(Enum):
    U = 0
    R = 1
    F = 2
    D = 3
    L = 4
    B = 5
    UW = 6
    RW = 7
    FW = 8
    DW = 9
    LW = 10
    BW = 11
    M = 12
    E = 13
    S = 14
    X = 15
    Y = 16
    Z = 17

class Cubie:
    def __init__(self, color_ud=Color.NONE, color_rl=Color.NONE, color_fb=Color.NONE):
        self.color_ud = color_ud
        self.color_rl = color_rl
        self.color_fb = color_fb
    
    def swap_ud_rl(self):
        color_ud = self.color_ud
        self.color_ud = self.color_rl
        self.color_rl = color_ud
    
    def swap_ud_db(self):
        color_ud = self.color_ud
        self.color_ud = self.color_db
        self.color_db = color_ud

    def swap_rl_fb(self):
        color_rl = self.color_rl
        self.color_rl = self.color_fb
        self.color_fb = color_rl

class Cube:
    layer0 = np.full((3, 3), Cubie(color_ud=Color.UP))
    layer1 = np.full((3, 3), Cubie())
    layer2 = np.full((3, 3), Cubie(color_ud=Color.DOWN))

    cube = np.array([layer0,layer1,layer2])

    #region Color left right
    cube = np.rot90(cube,1,(2,0))

    for i in range(3):
        for j in range(3):
            cubie = cube[0][i][j]
            cubie.color_rl = Color.LEFT
            cube[0][i][j] = cubie
    
    for i in range(3):
        for j in range(3):
            cubie = cube[2][i][j]
            cubie.color_rl = Color.RIGHT
            cube[2][i][j] = cubie
    
    cube = np.rot90(cube,-1,(2,0))
    #endregion

    #region Color front back
    cube = np.rot90(cube,1,(0,1))

    for i in range(3):
        for j in range(3):
            cubie = cube[0][i][j]
            cubie.color_fb = Color.FRONT
            cube[0][i][j] = cubie
    
    for i in range(3):
        for j in range(3):
            cubie = cube[2][i][j]
            cubie.color_fb = Color.BACK
            cube[2][i][j] = cubie
    
    cube = np.rot90(cube,-1,(0,1))
    #endregion

    def move(self, move, amount):
        match move:
            case Move.U:
                layer = self[0]
                layer = np.rot90(layer,-amount)
                self[0] = layer
            case Move.D:
                layer = self[2]
                layer = np.rot90(layer,amount)
                self[2] = layer