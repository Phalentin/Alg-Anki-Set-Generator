# ---------------------------------------------------
# SORRY TO EVERYONE WHO WANTS TO MAKE CHANGES TO THIS
# ---------------------------------------------------
from enum import Enum

class InvalidNotationError(Exception):
    pass

class Move(Enum):
    NONE = 0
    U = 1
    R = 2
    F = 3
    D = 4
    L = 5
    B = 6
    M = 7
    E = 8
    S = 9
    X = 10
    Y = 11
    Z = 12
    UW = 13
    RW = 14
    FW = 15
    DW = 16
    LW = 17
    BW = 18

move_chars = ["Uw","Rw","Fw","Dw","Lw","Bw","U","R","F","D","L","B","u","r","f","d","l","b","M","E","S","x","y","z"]

def cycle(stickers):
    last_element = stickers[-1]
    stickers.pop()
    stickers.insert(0, last_element)
    return stickers

def rotate_face(face, cubestring):
    sticker_0 = cubestring[face][0]
    sticker_1 = cubestring[face][2]
    sticker_2 = cubestring[face][8]
    sticker_3 = cubestring[face][6]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[face][0] = cycled_stickers[0]
    cubestring[face][2] = cycled_stickers[1]
    cubestring[face][8] = cycled_stickers[2]
    cubestring[face][6] = cycled_stickers[3]

    sticker_0 = cubestring[face][1]
    sticker_1 = cubestring[face][5]
    sticker_2 = cubestring[face][7]
    sticker_3 = cubestring[face][3]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[face][1] = cycled_stickers[0]
    cubestring[face][5] = cycled_stickers[1]
    cubestring[face][7] = cycled_stickers[2]
    cubestring[face][3] = cycled_stickers[3]

def rotate_u(cubestring):
    rotate_face(0, cubestring)
    sticker_0 = cubestring[1][0]
    sticker_1 = cubestring[2][0]
    sticker_2 = cubestring[4][0]
    sticker_3 = cubestring[5][0]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[1][0] = cycled_stickers[0]
    cubestring[2][0] = cycled_stickers[1]
    cubestring[4][0] = cycled_stickers[2]
    cubestring[5][0] = cycled_stickers[3]

    sticker_0 = cubestring[1][1]
    sticker_1 = cubestring[2][1]
    sticker_2 = cubestring[4][1]
    sticker_3 = cubestring[5][1]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[1][1] = cycled_stickers[0]
    cubestring[2][1] = cycled_stickers[1]
    cubestring[4][1] = cycled_stickers[2]
    cubestring[5][1] = cycled_stickers[3]
    
    sticker_0 = cubestring[1][2]
    sticker_1 = cubestring[2][2]
    sticker_2 = cubestring[4][2]
    sticker_3 = cubestring[5][2]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[1][2] = cycled_stickers[0]
    cubestring[2][2] = cycled_stickers[1]
    cubestring[4][2] = cycled_stickers[2]
    cubestring[5][2] = cycled_stickers[3]

def rotate_r(cubestring):
    rotate_face(1, cubestring)
    sticker_0 = cubestring[0][2]
    sticker_1 = cubestring[5][6]
    sticker_2 = cubestring[3][2]
    sticker_3 = cubestring[2][2]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[0][2] = cycled_stickers[0]
    cubestring[5][6] = cycled_stickers[1]
    cubestring[3][2] = cycled_stickers[2]
    cubestring[2][2] = cycled_stickers[3]

    sticker_0 = cubestring[0][5]
    sticker_1 = cubestring[5][3]
    sticker_2 = cubestring[3][5]
    sticker_3 = cubestring[2][5]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[0][5] = cycled_stickers[0]
    cubestring[5][3] = cycled_stickers[1]
    cubestring[3][5] = cycled_stickers[2]
    cubestring[2][5] = cycled_stickers[3]
    
    sticker_0 = cubestring[0][8]
    sticker_1 = cubestring[5][0]
    sticker_2 = cubestring[3][8]
    sticker_3 = cubestring[2][8]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[0][8] = cycled_stickers[0]
    cubestring[5][0] = cycled_stickers[1]
    cubestring[3][8] = cycled_stickers[2]
    cubestring[2][8] = cycled_stickers[3]

def rotate_f(cubestring):
    rotate_face(2, cubestring)
    sticker_0 = cubestring[0][6]
    sticker_1 = cubestring[1][0]
    sticker_2 = cubestring[3][2]
    sticker_3 = cubestring[4][8]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[0][6] = cycled_stickers[0]
    cubestring[1][0] = cycled_stickers[1]
    cubestring[3][2] = cycled_stickers[2]
    cubestring[4][8] = cycled_stickers[3]

    sticker_0 = cubestring[0][7]
    sticker_1 = cubestring[1][3]
    sticker_2 = cubestring[3][1]
    sticker_3 = cubestring[4][5]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[0][7] = cycled_stickers[0]
    cubestring[1][3] = cycled_stickers[1]
    cubestring[3][1] = cycled_stickers[2]
    cubestring[4][5] = cycled_stickers[3]
    
    sticker_0 = cubestring[0][8]
    sticker_1 = cubestring[1][6]
    sticker_2 = cubestring[3][0]
    sticker_3 = cubestring[4][2]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[0][8] = cycled_stickers[0]
    cubestring[1][6] = cycled_stickers[1]
    cubestring[3][0] = cycled_stickers[2]
    cubestring[4][2] = cycled_stickers[3]

def rotate_d(cubestring):
    rotate_face(3, cubestring)
    sticker_0 = cubestring[5][8]
    sticker_1 = cubestring[4][8]
    sticker_2 = cubestring[2][8]
    sticker_3 = cubestring[1][8]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[5][8] = cycled_stickers[0]
    cubestring[4][8] = cycled_stickers[1]
    cubestring[2][8] = cycled_stickers[2]
    cubestring[1][8] = cycled_stickers[3]

    sticker_0 = cubestring[5][7]
    sticker_1 = cubestring[4][7]
    sticker_2 = cubestring[2][7]
    sticker_3 = cubestring[1][7]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[5][7] = cycled_stickers[0]
    cubestring[4][7] = cycled_stickers[1]
    cubestring[2][7] = cycled_stickers[2]
    cubestring[1][7] = cycled_stickers[3]
    
    sticker_0 = cubestring[5][6]
    sticker_1 = cubestring[4][6]
    sticker_2 = cubestring[2][6]
    sticker_3 = cubestring[1][6]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[5][6] = cycled_stickers[0]
    cubestring[4][6] = cycled_stickers[1]
    cubestring[2][6] = cycled_stickers[2]
    cubestring[1][6] = cycled_stickers[3]

def rotate_l(cubestring):
    rotate_face(4, cubestring)
    sticker_0 = cubestring[2][6]
    sticker_1 = cubestring[3][6]
    sticker_2 = cubestring[5][2]
    sticker_3 = cubestring[0][6]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[2][6] = cycled_stickers[0]
    cubestring[3][6] = cycled_stickers[1]
    cubestring[5][2] = cycled_stickers[2]
    cubestring[0][6] = cycled_stickers[3]

    sticker_0 = cubestring[2][3]
    sticker_1 = cubestring[3][3]
    sticker_2 = cubestring[5][5]
    sticker_3 = cubestring[0][3]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[2][3] = cycled_stickers[0]
    cubestring[3][3] = cycled_stickers[1]
    cubestring[5][5] = cycled_stickers[2]
    cubestring[0][3] = cycled_stickers[3]
    
    sticker_0 = cubestring[2][0]
    sticker_1 = cubestring[3][0]
    sticker_2 = cubestring[5][8]
    sticker_3 = cubestring[0][0]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[2][0] = cycled_stickers[0]
    cubestring[3][0] = cycled_stickers[1]
    cubestring[5][8] = cycled_stickers[2]
    cubestring[0][0] = cycled_stickers[3]

def rotate_b(cubestring):
    rotate_face(5, cubestring)
    sticker_0 = cubestring[3][8]
    sticker_1 = cubestring[4][6]
    sticker_2 = cubestring[0][0]
    sticker_3 = cubestring[1][2]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[0][0] = cycled_stickers[0]
    cubestring[1][2] = cycled_stickers[1]
    cubestring[3][8] = cycled_stickers[2]
    cubestring[4][6] = cycled_stickers[3]

    sticker_0 = cubestring[3][7]
    sticker_1 = cubestring[4][3]
    sticker_2 = cubestring[0][1]
    sticker_3 = cubestring[1][5]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[0][1] = cycled_stickers[0]
    cubestring[1][5] = cycled_stickers[1]
    cubestring[3][7] = cycled_stickers[2]
    cubestring[4][3] = cycled_stickers[3]
    
    sticker_0 = cubestring[3][6]
    sticker_1 = cubestring[4][0]
    sticker_2 = cubestring[0][2]
    sticker_3 = cubestring[1][8]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[0][2] = cycled_stickers[0]
    cubestring[1][8] = cycled_stickers[1]
    cubestring[3][6] = cycled_stickers[2]
    cubestring[4][0] = cycled_stickers[3]

def rotate_m(cubestring):
    sticker_0 = cubestring[2][4]
    sticker_1 = cubestring[3][4]
    sticker_2 = cubestring[5][4]
    sticker_3 = cubestring[0][4]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[2][4] = cycled_stickers[0]
    cubestring[3][4] = cycled_stickers[1]
    cubestring[5][4] = cycled_stickers[2]
    cubestring[0][4] = cycled_stickers[3]

    sticker_0 = cubestring[2][1]
    sticker_1 = cubestring[3][1]
    sticker_2 = cubestring[5][7]
    sticker_3 = cubestring[0][1]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[2][1] = cycled_stickers[0]
    cubestring[3][1] = cycled_stickers[1]
    cubestring[5][7] = cycled_stickers[2]
    cubestring[0][1] = cycled_stickers[3]
    
    sticker_0 = cubestring[2][7]
    sticker_1 = cubestring[3][7]
    sticker_2 = cubestring[5][1]
    sticker_3 = cubestring[0][7]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[2][7] = cycled_stickers[0]
    cubestring[3][7] = cycled_stickers[1]
    cubestring[5][1] = cycled_stickers[2]
    cubestring[0][7] = cycled_stickers[3]

def rotate_e(cubestring):
    sticker_0 = cubestring[2][4]
    sticker_1 = cubestring[1][4]
    sticker_2 = cubestring[5][4]
    sticker_3 = cubestring[4][4]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[2][4] = cycled_stickers[0]
    cubestring[1][4] = cycled_stickers[1]
    cubestring[5][4] = cycled_stickers[2]
    cubestring[4][4] = cycled_stickers[3]

    sticker_0 = cubestring[2][3]
    sticker_1 = cubestring[1][3]
    sticker_2 = cubestring[5][3]
    sticker_3 = cubestring[4][3]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[2][3] = cycled_stickers[0]
    cubestring[1][3] = cycled_stickers[1]
    cubestring[5][3] = cycled_stickers[2]
    cubestring[4][3] = cycled_stickers[3]
    
    sticker_0 = cubestring[2][5]
    sticker_1 = cubestring[1][5]
    sticker_2 = cubestring[5][5]
    sticker_3 = cubestring[4][5]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[2][5] = cycled_stickers[0]
    cubestring[1][5] = cycled_stickers[1]
    cubestring[5][5] = cycled_stickers[2]
    cubestring[4][5] = cycled_stickers[3]

def rotate_s(cubestring):
    sticker_0 = cubestring[0][4]
    sticker_1 = cubestring[1][4]
    sticker_2 = cubestring[3][4]
    sticker_3 = cubestring[4][4]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[0][4] = cycled_stickers[0]
    cubestring[1][4] = cycled_stickers[1]
    cubestring[3][4] = cycled_stickers[2]
    cubestring[4][4] = cycled_stickers[3]

    sticker_0 = cubestring[0][5]
    sticker_1 = cubestring[1][7]
    sticker_2 = cubestring[3][3]
    sticker_3 = cubestring[4][1]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[0][5] = cycled_stickers[0]
    cubestring[1][7] = cycled_stickers[1]
    cubestring[3][3] = cycled_stickers[2]
    cubestring[4][1] = cycled_stickers[3]
    
    sticker_0 = cubestring[0][3]
    sticker_1 = cubestring[1][1]
    sticker_2 = cubestring[3][5]
    sticker_3 = cubestring[4][7]
    cycled_stickers = cycle([sticker_0,sticker_1,sticker_2,sticker_3])
    cubestring[0][3] = cycled_stickers[0]
    cubestring[1][1] = cycled_stickers[1]
    cubestring[3][5] = cycled_stickers[2]
    cubestring[4][7] = cycled_stickers[3]

def scramble_to_cubestring(scramble):
    cubestring =   [["U","U","U",
                    "U","U","U",
                    "U","U","U"],
                    ["R","R","R",
                    "R","R","R",
                    "R","R","R"],
                    ["F","F","F",
                    "F","F","F",
                    "F","F","F"],
                    ["D","D","D",
                    "D","D","D",
                    "D","D","D"],
                    ["L","L","L",
                    "L","L","L",
                    "L","L","L"],
                    ["B","B","B",
                    "B","B","B",
                    "B","B","B"]]
    
    instructions = []
    moves = scramble.split()

    for i in range(len(moves)):
        amount_val = 1
        move_type = Move.NONE

        move = moves[i]
        move = move.replace("(", "").replace(")", "")

        #region Check move
        if "Uw" in move or "u" in move:
            move_type = Move.UW
        elif "Rw" in move or "r" in move:
            move_type = Move.RW
        elif "Fw" in move or "f" in move:
            move_type = Move.FW
        elif "Dw" in move or "d" in move:
            move_type = Move.DW
        elif "Lw" in move or "l" in move:
            move_type = Move.LW
        elif "Bw" in move or "b" in move:
            move_type = Move.BW
        elif "U" in move:
            move_type = Move.U
        elif "R" in move:
            move_type = Move.R
        elif "F" in move:
            move_type = Move.F
        elif "D" in move:
            move_type = Move.D
        elif "L" in move:
            move_type = Move.L
        elif "B" in move:
            move_type = Move.B
        elif "M" in move:
            move_type = Move.M
        elif "E" in move:
            move_type = Move.E
        elif "S" in move:
            move_type = Move.S
        elif "x" in move:
            move_type = Move.X
        elif "y" in move:
            move_type = Move.Y
        elif "z" in move:
            move_type = Move.Z
        else:
            raise InvalidNotationError("Invalid Scramble Notation")
            return 4
        #endregion
        
        amount = move
        for char in move_chars:
            amount = amount.replace(char,"")

        for char in amount:
            if char.isdigit():
                amount_val += int(char) % 4 - 1
            elif char in ["'", "`"]:
                amount_val = (amount_val - 2) * -1 + 2
            elif char == "*":
                pass
            else:
                raise InvalidNotationError
        instructions.append((move_type, amount_val))
    
    for instruction in instructions:
        move_type = instruction[0]
        amount_val = instruction[1]
        for i in range(amount_val):
            match move_type:
                case Move.U:
                    rotate_u(cubestring)
                case Move.R:
                    rotate_r(cubestring)
                case Move.F:
                    rotate_f(cubestring)
                case Move.D:
                    rotate_d(cubestring)
                case Move.L:
                    rotate_l(cubestring)
                case Move.B:
                    rotate_b(cubestring)
                case Move.M:
                    rotate_m(cubestring)
                case Move.E:
                    rotate_e(cubestring)
                case Move.S:
                    rotate_s(cubestring)
                case Move.UW:
                    rotate_u(cubestring)
                    for i in range(3):
                        rotate_e(cubestring)
                case Move.RW:
                    rotate_r(cubestring)
                    for i in range(3):
                        rotate_m(cubestring)
                case Move.FW:
                    rotate_f(cubestring)
                    rotate_s(cubestring)
                case Move.DW:
                    rotate_d(cubestring)
                    rotate_e(cubestring)
                case Move.LW:
                    rotate_l(cubestring)
                    rotate_m(cubestring)
                case Move.BW:
                    rotate_b(cubestring)
                    for i in range(3):
                        rotate_s(cubestring)
                case Move.X:
                    rotate_r(cubestring)
                    for i in range(3):
                        rotate_m(cubestring)
                        rotate_l(cubestring)
                case Move.Y:
                    rotate_u(cubestring)
                    for i in range(3):
                        rotate_e(cubestring)
                        rotate_d(cubestring)
                case Move.Z:
                    rotate_f(cubestring)
                    rotate_s(cubestring)
                    for i in range(3):
                        rotate_b(cubestring)
    
    output = ""
    for side in cubestring:
        for sticker in side:
            output += sticker
    
    return output