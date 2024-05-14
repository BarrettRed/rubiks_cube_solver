import random
import time
from tkinter import *

class Rubiks_Cube:
    def __init__(self):
        self.solution = []
        self.state = list(range(55))
        for i in range(1, 10):
            self.state[i] = 'RED'
        for i in range(10, 19):
            self.state[i] = 'GREEN'
        for i in range(19, 28):
            self.state[i] = 'ORANGE'
        for i in range(28, 37):
            self.state[i] = 'BLUE'
        for i in range(37, 46):
            self.state[i] = 'WHITE'
        for i in range(46, 55):
            self.state[i] = 'YELLOW'
        self.color_to_center_sticker = {
            "RED": 5,
            "GREEN": 14,
            "ORANGE": 23,
            "BLUE": 32,
            "WHITE": 41,
            "YELLOW": 50
        }
        self.edges = {
            13: 53,  # F
            11: 26,  # F
            15: 38,  # F
            17: 2,   # F
            22: 51,  # R
            20: 35,  # R
            24: 42,  # R
            26: 11,  # R
            4: 49,   # L
            2: 17,   # L
            6: 40,   # L
            8: 29,   # L
            31: 47,  # B
            29: 8,   # B
            33: 44,  # B
            35: 20,  # B
            47: 31,  # U
            51: 22,  # U
            53: 13,  # U
            49: 4,   # U
            38: 15,  # D
            42: 24,  # D
            44: 33,  # D
            40: 6,   # D
        }
        self.corners = [
            # up
            [7, 28, 46],
            [1, 16, 52],
            [10, 25, 54],
            [19, 34, 48],
            # down
            [9, 30, 43],
            [3, 18, 37],
            [12, 27, 39],
            [21, 36, 45],
        ]
        self.rotation_moves = {
            "U": self.rotate_U,
            "U2": self.rotate_U2,
            "U'": self.rotate_Ub,
            "D": self.rotate_D,
            "D2": self.rotate_D2,
            "D'": self.rotate_Db,
            "L": self.rotate_L,
            "L2": self.rotate_L2,
            "L'": self.rotate_Lb,
            "R": self.rotate_R,
            "R2": self.rotate_R2,
            "R'": self.rotate_Rb,
            "F": self.rotate_F,
            "F2": self.rotate_F2,
            "F'": self.rotate_Fb,
            "B": self.rotate_B,
            "B2": self.rotate_B2,
            "B'": self.rotate_Bb
        }
        self.equal_rotations = {
            # ("side", "move"): equal_move,
            # left side
            ("L", "R"): "F",
            ("L", "R'"): "F'",
            ("L", "R2"): "F2",
            ("L", "L"): "B",
            ("L", "L'"): "B'",
            ("L", "L2"): "B2",
            ("L", "U"): "U",
            ("L", "U'"): "U'",
            ("L", "U2"): "U2",
            ("L", "D"): "D",
            ("L", "D'"): "D'",
            ("L", "D2"): "D2",
            ("L", "F"): "L",
            ("L", "F'"): "L'",
            ("L", "F2"): "L2",
            ("L", "B"): "R",
            ("L", "B'"): "R'",
            ("L", "B2"): "R2",
            # right side
            ("R", "R"): "B",
            ("R", "R'"): "B'",
            ("R", "R2"): "B2",
            ("R", "L"): "F",
            ("R", "L'"): "F'",
            ("R", "L2"): "F2",
            ("R", "U"): "U",
            ("R", "U'"): "U'",
            ("R", "U2"): "U2",
            ("R", "D"): "D",
            ("R", "D'"): "D'",
            ("R", "D2"): "D2",
            ("R", "F"): "R",
            ("R", "F'"): "R'",
            ("R", "F2"): "R2",
            ("R", "B"): "R",
            ("R", "B'"): "R'",
            ("R", "B2"): "R2",
            # back side
            ("B", "R"): "L",
            ("B", "R'"): "L'",
            ("B", "R2"): "L2",
            ("B", "L"): "R",
            ("B", "L'"): "R'",
            ("B", "L2"): "R2",
            ("B", "U"): "U",
            ("B", "U'"): "U'",
            ("B", "U2"): "U2",
            ("B", "D"): "D",
            ("B", "D'"): "D'",
            ("B", "D2"): "D2",
            ("B", "F"): "B",
            ("B", "F'"): "B'",
            ("B", "F2"): "B2",
            ("B", "B"): "F",
            ("B", "B'"): "F'",
            ("B", "B2"): "F2",
            # front side
            ("F", "R"): "R",
            ("F", "R'"): "R'",
            ("F", "R2"): "R2",
            ("F", "L"): "L",
            ("F", "L'"): "L'",
            ("F", "L2"): "L2",
            ("F", "U"): "U",
            ("F", "U'"): "U'",
            ("F", "U2"): "U2",
            ("F", "D"): "D",
            ("F", "D'"): "D'",
            ("F", "D2"): "D2",
            ("F", "F"): "F",
            ("F", "F'"): "F'",
            ("F", "F2"): "F2",
            ("F", "B"): "B",
            ("F", "B'"): "B'",
            ("F", "B2"): "B2",
        }

    @staticmethod
    def get_side(i):
        sides = ["L", "F", "R", "B", "D", "U"]
        return sides[(i - 1) // 9]

    def rotate(self, move: str):
        self.rotation_moves[move]()
        self.solution.append(move)
        time.sleep(0.05)
        draw_cube()

    def scramble(self):
        for i in range(20):
            self.rotate(random.choice(list(self.rotation_moves.keys())))
        self.solution = []

    def rotate_B(self):
        self.state[31], self.state[29], self.state[33], self.state[35] = self.state[35], self.state[31], self.state[29], self.state[33]
        self.state[28], self.state[30], self.state[36], self.state[34] = self.state[34], self.state[28], self.state[30], self.state[36]
        temp7, temp8, temp9 = self.state[7], self.state[8], self.state[9]
        self.state[9], self.state[8], self.state[7] = self.state[46], self.state[47], self.state[48]
        self.state[46], self.state[47], self.state[48] = self.state[19], self.state[20], self.state[21]
        self.state[19], self.state[20], self.state[21] = self.state[45], self.state[44], self.state[43]
        self.state[45], self.state[44], self.state[43] = temp9, temp8, temp7

    def rotate_B2(self):
        self.rotate_B()
        self.rotate_B()

    def rotate_Bb(self):
        self.rotate_B()
        self.rotate_B()
        self.rotate_B()

    def rotate_F(self):
        self.state[13], self.state[11], self.state[15], self.state[17] = self.state[17], self.state[13], self.state[11], self.state[15]
        self.state[10], self.state[12], self.state[18], self.state[16] = self.state[16], self.state[10], self.state[12], self.state[18]
        temp52, temp53, temp54 = self.state[52], self.state[53], self.state[54]
        self.state[52], self.state[53], self.state[54] = self.state[3], self.state[2], self.state[1]
        self.state[3], self.state[2], self.state[1] = self.state[39], self.state[38], self.state[37]
        self.state[39], self.state[38], self.state[37] = self.state[25], self.state[26], self.state[27]
        self.state[27], self.state[26], self.state[25] = temp54, temp53, temp52

    def rotate_F2(self):
        self.rotate_F()
        self.rotate_F()

    def rotate_Fb(self):
        self.rotate_F()
        self.rotate_F()
        self.rotate_F()

    def rotate_U(self):
        self.state[52], self.state[46], self.state[48], self.state[54] = self.state[54], self.state[52], self.state[46], self.state[48]
        self.state[53], self.state[49], self.state[47], self.state[51] = self.state[51], self.state[53], self.state[49], self.state[47]
        temp7, temp4, temp1 = self.state[7], self.state[4], self.state[1]
        self.state[7], self.state[4], self.state[1] = self.state[16], self.state[13], self.state[10]
        self.state[16], self.state[13], self.state[10] = self.state[25], self.state[22], self.state[19]
        self.state[25], self.state[22], self.state[19] = self.state[34], self.state[31], self.state[28]
        self.state[34], self.state[31], self.state[28] = temp7, temp4, temp1

    def rotate_U2(self):
        self.rotate_U()
        self.rotate_U()

    def rotate_Ub(self):
        self.rotate_U()
        self.rotate_U()
        self.rotate_U()

    def rotate_D(self):
        self.state[38], self.state[42], self.state[44], self.state[40] = self.state[40], self.state[38], self.state[42], self.state[44]
        self.state[39], self.state[45], self.state[43], self.state[37] = self.state[37], self.state[39], self.state[45], self.state[43]
        temp18, temp15, temp12 = self.state[18], self.state[15], self.state[12]
        self.state[18], self.state[15], self.state[12] = self.state[9], self.state[6], self.state[3]
        self.state[9], self.state[6], self.state[3] = self.state[36], self.state[33], self.state[30]
        self.state[36], self.state[33], self.state[30] = self.state[27], self.state[24], self.state[21]
        self.state[27], self.state[24], self.state[21] = temp18, temp15, temp12

    def rotate_D2(self):
        self.rotate_D()
        self.rotate_D()

    def rotate_Db(self):
        self.rotate_D()
        self.rotate_D()
        self.rotate_D()

    def rotate_L(self):
        self.state[1], self.state[3], self.state[9], self.state[7] = self.state[7], self.state[1], self.state[3], self.state[9]
        self.state[2], self.state[6], self.state[8], self.state[4] = self.state[4], self.state[2], self.state[6], self.state[8]
        temp16, temp17, temp18 = self.state[16], self.state[17], self.state[18]
        self.state[16], self.state[17], self.state[18] = self.state[46], self.state[49], self.state[52]
        self.state[46], self.state[49], self.state[52] = self.state[30], self.state[29], self.state[28]
        self.state[30], self.state[29], self.state[28] = self.state[37], self.state[40], self.state[43]
        self.state[37], self.state[40], self.state[43] = temp16, temp17, temp18

    def rotate_L2(self):
        self.rotate_L()
        self.rotate_L()

    def rotate_Lb(self):
        self.rotate_L()
        self.rotate_L()
        self.rotate_L()

    def rotate_R(self):
        self.state[19], self.state[21], self.state[27], self.state[25] = self.state[25], self.state[19], self.state[21], self.state[27]
        self.state[22], self.state[20], self.state[24], self.state[26] = self.state[26], self.state[22], self.state[20], self.state[24]
        temp10, temp11, temp12 = self.state[10], self.state[11], self.state[12]
        self.state[10], self.state[11], self.state[12] = self.state[39], self.state[42], self.state[45]
        self.state[39], self.state[42], self.state[45] = self.state[36], self.state[35], self.state[34]
        self.state[36], self.state[35], self.state[34] = self.state[48], self.state[51], self.state[54]
        self.state[54], self.state[51], self.state[48] = temp12, temp11, temp10

    def rotate_R2(self):
        self.rotate_R()
        self.rotate_R()

    def rotate_Rb(self):
        self.rotate_R()
        self.rotate_R()
        self.rotate_R()

    def is_cross_solved(self):
        for i in [38, 40, 42, 44]:
            if self.state[i] != "WHITE":
                return False
        correct_color_sequence = ["GREEN", "ORANGE", "BLUE", "RED"]
        current_sequence = [self.state[15], self.state[24], self.state[33], self.state[6]]
        for i in range(3):
            if current_sequence == correct_color_sequence:
                return True
            else:
                self.rotate_D()
        self.rotate_D()
        return False

    def make_correct_cross(self):
        wrong_pos_edges = []

        adj_sticker = self.edges[38]
        if not self.state[adj_sticker] == self.state[adj_sticker - 1]:
            wrong_pos_edges.append(38)

        adj_sticker = self.edges[40]
        if not self.state[adj_sticker] == self.state[adj_sticker - 1]:
            wrong_pos_edges.append(40)

        adj_sticker = self.edges[42]
        if not self.state[adj_sticker] == self.state[adj_sticker - 1]:
            wrong_pos_edges.append(42)

        adj_sticker = self.edges[44]
        if not self.state[adj_sticker] == self.state[adj_sticker - 1]:
            wrong_pos_edges.append(44)

        if len(wrong_pos_edges) == 1 or len(wrong_pos_edges) == 4 or len(wrong_pos_edges) == 3:
            self.rotate("D")
        elif len(wrong_pos_edges) == 2:
            sol = []
            if wrong_pos_edges[0] == 38:
                if wrong_pos_edges[1] == 44:
                    sol = ["F2", "B2", "U2", "F2", "B2"]
                if wrong_pos_edges[1] == 40:
                    sol = ["F", "D", "F'", "D'", "F"]
                if wrong_pos_edges[1] == 42:
                    sol = ["F", "D'", "F'", "D", "F"]
            if wrong_pos_edges[0] == 40:
                if wrong_pos_edges[1] == 42:
                    sol = ["F2", "B2", "U2", "F2", "B2"]
                if wrong_pos_edges[1] == 44:
                    sol = ["F", "D", "F'", "D'", "F"]
                equal_sol = []
                for i in sol:
                    equal_sol.append(self.equal_rotations[("L", i)])
            if wrong_pos_edges[0] == 42:
                sol = ["F", "D'", "F'", "D", "F"]
                equal_sol = []
                for i in sol:
                    equal_sol.append(self.equal_rotations[("R", i)])
                sol = equal_sol
            for move in sol:
                self.rotate(move)

    def cross(self):
        # white stickers on the bottom/white side
        count = 0
        for i in [38, 40, 42, 44]:
            if self.state[i] == "WHITE":
                count += 1
        if count == 4 and not self.is_cross_solved():
            self.make_correct_cross()
        while not self.is_cross_solved():
            count = 0
            for i in [38, 40, 42, 44]:
                if self.state[i] == "WHITE":
                    count += 1
            if count == 4 and not self.is_cross_solved():
                self.make_correct_cross()
            # white stickers on right and left edges
            for i, j in [[2, 38], [11, 42], [20, 44], [29, 40]]:
                if self.state[i] == "WHITE":
                    while self.state[j] == "WHITE":
                        self.rotate("D")
                    self.rotate(self.equal_rotations[(self.get_side(i), "R'")])
            for i, j in [[8, 44], [17, 40], [26, 38], [35, 42]]:
                if self.state[i] == "WHITE":
                    while self.state[j] == "WHITE":
                        self.rotate("D")
                    self.rotate(self.equal_rotations[(self.get_side(i), "L")])
            # white stickers on the top/yellow side
            if self.state[47] == "WHITE":
                while self.state[44] == "WHITE":
                    self.rotate("D")
                self.rotate("B2")
            if self.state[49] == "WHITE":
                while self.state[40] == "WHITE":
                    self.rotate("D")
                self.rotate("L2")
            if self.state[51] == "WHITE":
                while self.state[42] == "WHITE":
                    self.rotate("D")
                self.rotate("R2")
            if self.state[53] == "WHITE":
                while self.state[38] == "WHITE":
                    self.rotate("D")
                self.rotate("F2")
            #
            for i, j, k in [[4, 6, 40], [13, 15, 38], [22, 24, 42], [31, 33, 44]]:
                if self.state[i] == "WHITE" or self.state[j] == "WHITE":
                    while self.state[k] == "WHITE":
                        self.rotate("D")
                    self.rotate(self.equal_rotations[self.get_side(i), "F"])

    def is_first_layer_solved(self):
        for i in [37, 39, 43, 45]:
            if self.state[i] != "WHITE":
                return False
        for i in [9, 18, 27, 36]:
            if self.state[i] != self.state[i - 4]:
                return False
        for i in [3, 12, 21, 30]:
            if self.state[i] != self.state[i + 2]:
                return False
        return True

    def first_layer(self):
        while not self.is_first_layer_solved():
            left_forward = [7, 16, 25, 34]
            for i in left_forward:
                if self.state[i] == "WHITE":
                    corner = []
                    for j in self.corners:
                        if j.count(i) > 0:
                            corner = j.copy()
                            break
                    corner.remove(i)
                    up_sticker = max(corner)
                    corner.remove(up_sticker)
                    left_sticker = corner[0]
                    center_sticker = left_sticker + 4
                    up_sticker_color = self.state[up_sticker]
                    while self.state[center_sticker] != up_sticker_color:
                        self.rotate("U'")
                        left_sticker = (left_sticker + 9) % 36  # 1, 10, 19, 28 - possible values
                        center_sticker = left_sticker + 4

                    self.rotate(self.equal_rotations[self.get_side(center_sticker), "L'"])
                    self.rotate(self.equal_rotations[self.get_side(center_sticker), "U"])
                    self.rotate(self.equal_rotations[self.get_side(center_sticker), "L"])

            right_forward = [1, 10, 19, 28]
            for i in right_forward:
                if self.state[i] == "WHITE":
                    corner = []
                    for j in self.corners:
                        if j.count(i) > 0:
                            corner = j.copy()
                            break
                    corner.remove(i)
                    up_sticker = max(corner)
                    corner.remove(up_sticker)
                    right_sticker = corner[0]
                    center_sticker = right_sticker - 2
                    up_sticker_color = self.state[up_sticker]
                    while self.state[center_sticker] != up_sticker_color:
                        self.rotate("U'")
                        right_sticker = (right_sticker + 9) % 36  # 7, 16, 25, 34 - possible values
                        center_sticker = right_sticker - 2
                    sol = ["R", "U'", "R'"]
                    self.rotate(self.equal_rotations[self.get_side(center_sticker), "R"])
                    self.rotate(self.equal_rotations[self.get_side(center_sticker), "U'"])
                    self.rotate(self.equal_rotations[self.get_side(center_sticker), "R'"])

            for i in [46, 48, 52, 54]:
                if self.state[i] == "WHITE":
                    corner = []
                    seq = [7, 16, 25, 34]
                    for j in self.corners:
                        if j.count(i) > 0:
                            corner = j.copy()
                            break
                    corner.remove(i)
                    right_sticker = max(corner)
                    corner.remove(right_sticker)
                    left_sticker = corner[0]
                    if i == 46:
                        right_sticker = 7
                        left_sticker = 28
                    center_sticker = left_sticker + 4
                    right_sticker_color = self.state[right_sticker]
                    while self.state[center_sticker] != right_sticker_color:
                        self.rotate("U'")
                        right_sticker = seq[(seq.index(right_sticker) + 1) % 4]
                        left_sticker = (left_sticker + 9) % 36
                        center_sticker = left_sticker + 4

                    self.rotate(self.equal_rotations[self.get_side(center_sticker), "R"])
                    self.rotate(self.equal_rotations[self.get_side(center_sticker), "U'"])
                    self.rotate(self.equal_rotations[self.get_side(center_sticker), "R'"])
                    self.rotate(self.equal_rotations[self.get_side(center_sticker), "U"])
                    self.rotate(self.equal_rotations[self.get_side(center_sticker), "F'"])
                    self.rotate(self.equal_rotations[self.get_side(center_sticker), "U"])
                    self.rotate(self.equal_rotations[self.get_side(center_sticker), "F"])

            for i in [9, 18, 27, 36]:
                if self.state[i] == "WHITE":
                    corner = []
                    for j in self.corners:
                        if j.count(i) > 0:
                            corner = j.copy()
                    corner.remove(i)
                    left_sticker = min(corner)
                    corner.remove(left_sticker)
                    bottom_sticker = corner[0]
                    left_center_sticker = left_sticker + 2
                    forward_center_sticker = i - 4
                    if self.state[bottom_sticker] == self.state[left_center_sticker] and self.state[forward_center_sticker] == self.state[left_sticker]:
                        self.rotate(self.equal_rotations[self.get_side(left_center_sticker), "R"])
                        self.rotate(self.equal_rotations[self.get_side(left_center_sticker), "U"])
                        self.rotate(self.equal_rotations[self.get_side(left_center_sticker), "R'"])
                        self.rotate(self.equal_rotations[self.get_side(left_center_sticker), "U'"])
                        self.rotate(self.equal_rotations[self.get_side(left_center_sticker), "R"])
                        self.rotate(self.equal_rotations[self.get_side(left_center_sticker), "U"])
                        self.rotate(self.equal_rotations[self.get_side(left_center_sticker), "R'"])
                    else:
                        self.rotate(self.equal_rotations[self.get_side(left_center_sticker), "R"])
                        self.rotate(self.equal_rotations[self.get_side(left_center_sticker), "U"])
                        self.rotate(self.equal_rotations[self.get_side(left_center_sticker), "R'"])

            for i in [3, 12, 21, 30]:
                if self.state[i] == "WHITE":
                    corner = []
                    for j in self.corners:
                        if j.count(i) > 0:
                            corner = j.copy()
                    corner.remove(i)
                    right_sticker = min(corner)
                    corner.remove(right_sticker)
                    bottom_sticker = corner[0]
                    right_center_sticker = right_sticker - 4
                    forward_center_sticker = i + 2
                    if self.state[bottom_sticker] == self.state[right_center_sticker] and self.state[forward_center_sticker] == self.state[right_sticker]:
                        self.rotate(self.equal_rotations[self.get_side(forward_center_sticker), "R"])
                        self.rotate(self.equal_rotations[self.get_side(forward_center_sticker), "U'"])
                        self.rotate(self.equal_rotations[self.get_side(forward_center_sticker), "R'"])
                        self.rotate(self.equal_rotations[self.get_side(forward_center_sticker), "U"])
                        self.rotate(self.equal_rotations[self.get_side(forward_center_sticker), "R"])
                        self.rotate(self.equal_rotations[self.get_side(forward_center_sticker), "U'"])
                        self.rotate(self.equal_rotations[self.get_side(forward_center_sticker), "R'"])
                    else:
                        self.rotate(self.equal_rotations[self.get_side(forward_center_sticker), "R"])
                        self.rotate(self.equal_rotations[self.get_side(forward_center_sticker), "U'"])
                        self.rotate(self.equal_rotations[self.get_side(forward_center_sticker), "R'"])

    def is_second_layer_solved(self):
        # checking left edges
        # forward_sticker color should be equal forward_center_sticker (= forward_sticker - 3) color
        # left
        for i in [8, 17, 26, 35]:
            if self.state[i] != self.state[i - 3]:
                return False
            if self.state[self.edges[i]] != self.state[self.edges[i] + 3]:
                return False
        return True

    def second_layer(self):
        while not self.is_second_layer_solved():
            edges = [4, 13, 22, 31]
            for index, i in enumerate(edges):
                up_sticker = self.edges[i]
                if self.state[i] != "YELLOW" and self.state[up_sticker] != "YELLOW":
                    if self.state[up_sticker] == self.state[edges[(index + 2) % 4] + 1]:
                        if self.state[i] == self.state[edges[(index + 1) % 4] + 1]:  # if forward_sticker_color is right_center_sticker_color
                            side = self.get_side(edges[(index + 1) % 4] + 1)
                            self.rotate(self.equal_rotations[side, "R"])
                            self.rotate(self.equal_rotations[side, "U'"])
                            self.rotate(self.equal_rotations[side, "R'"])
                            self.rotate(self.equal_rotations[side, "U'"])
                            self.rotate(self.equal_rotations[side, "F'"])
                            self.rotate(self.equal_rotations[side, "U"])
                            self.rotate(self.equal_rotations[side, "F"])
                        elif self.state[i] == self.state[edges[(index + 3) % 4] + 1]:
                            side = self.get_side(edges[(index + 3) % 4] + 1)
                            self.rotate(self.equal_rotations[side, "L'"])
                            self.rotate(self.equal_rotations[side, "U"])
                            self.rotate(self.equal_rotations[side, "L"])
                            self.rotate(self.equal_rotations[side, "U"])
                            self.rotate(self.equal_rotations[side, "F"])
                            self.rotate(self.equal_rotations[side, "U'"])
                            self.rotate(self.equal_rotations[side, "F'"])
                    elif self.state[up_sticker] == self.state[edges[(index + 1) % 4] + 1]:
                        if self.state[i] == self.state[i + 1]:
                            side = self.get_side(i)
                            self.rotate(self.equal_rotations[side, "U"])
                            self.rotate(self.equal_rotations[side, "R"])
                            self.rotate(self.equal_rotations[side, "U'"])
                            self.rotate(self.equal_rotations[side, "R'"])
                            self.rotate(self.equal_rotations[side, "U'"])
                            self.rotate(self.equal_rotations[side, "F'"])
                            self.rotate(self.equal_rotations[side, "U"])
                            self.rotate(self.equal_rotations[side, "F"])
                        else:
                            side = self.get_side(self.color_to_center_sticker[self.state[i]])
                            self.rotate(self.equal_rotations[side, "U"])
                            self.rotate(self.equal_rotations[side, "L'"])
                            self.rotate(self.equal_rotations[side, "U"])
                            self.rotate(self.equal_rotations[side, "L"])
                            self.rotate(self.equal_rotations[side, "U"])
                            self.rotate(self.equal_rotations[side, "F"])
                            self.rotate(self.equal_rotations[side, "U'"])
                            self.rotate(self.equal_rotations[side, "F'"])
                    elif self.state[up_sticker] == self.state[edges[(index + 3) % 4] + 1]:
                        if self.state[i] == self.state[i + 1]:
                            side = self.get_side(i)
                            self.rotate(self.equal_rotations[side, "U'"])
                            self.rotate(self.equal_rotations[side, "L'"])
                            self.rotate(self.equal_rotations[side, "U"])
                            self.rotate(self.equal_rotations[side, "L"])
                            self.rotate(self.equal_rotations[side, "U"])
                            self.rotate(self.equal_rotations[side, "F"])
                            self.rotate(self.equal_rotations[side, "U'"])
                            self.rotate(self.equal_rotations[side, "F'"])
                        else:
                            side = self.get_side(self.color_to_center_sticker[self.state[i]])
                            self.rotate(self.equal_rotations[side, "U'"])
                            self.rotate(self.equal_rotations[side, "R"])
                            self.rotate(self.equal_rotations[side, "U'"])
                            self.rotate(self.equal_rotations[side, "R'"])
                            self.rotate(self.equal_rotations[side, "U'"])
                            self.rotate(self.equal_rotations[side, "F'"])
                            self.rotate(self.equal_rotations[side, "U"])
                            self.rotate(self.equal_rotations[side, "F"])
                    else:
                        self.rotate("U")

            edges = [8, 17, 26, 35]
            for i in edges:
                if self.state[i] == "YELLOW" or self.state[self.edges[i]] == "YELLOW":
                    continue
                if self.state[i] == self.state[i - 3] and self.state[self.edges[i]] == self.state[self.edges[i] + 3]:
                    continue
                else:
                    self.rotate(self.equal_rotations[self.get_side(i), "R"])
                    self.rotate(self.equal_rotations[self.get_side(i), "U'"])
                    self.rotate(self.equal_rotations[self.get_side(i), "R'"])
                    self.rotate(self.equal_rotations[self.get_side(i), "U'"])
                    self.rotate(self.equal_rotations[self.get_side(i), "F'"])
                    self.rotate(self.equal_rotations[self.get_side(i), "U"])
                    self.rotate(self.equal_rotations[self.get_side(i), "F"])

    def is_top_cross_solved(self):
        for i in [47, 49, 51, 53]:
            if self.state[i] != "YELLOW":
                return False
        return True

    def top_cross(self):
        while not self.is_top_cross_solved():
            angles = [
                # 00 and 01 - stickers that make angle, 1 - sticker of necessary side for movements
                [[49, 47], 14],
                [[47, 51], 5],
                [[51, 53], 32],
                [[49, 53], 23]
            ]
            sticks = [
                [[49, 51], 14],
                [[47, 53], 5]
            ]
            current = []
            for i in [47, 49, 51, 53]:
                if self.state[i] == "YELLOW":
                    current.append(i)
            if len(current) == 0:
                self.rotate("F")
                self.rotate("R")
                self.rotate("U")
                self.rotate("R'")
                self.rotate("U'")
                self.rotate("F'")
            for stick in sticks:
                if current in stick:
                    self.rotate(self.equal_rotations[self.get_side(stick[1]), "F"])
                    self.rotate(self.equal_rotations[self.get_side(stick[1]), "R"])
                    self.rotate(self.equal_rotations[self.get_side(stick[1]), "U"])
                    self.rotate(self.equal_rotations[self.get_side(stick[1]), "R'"])
                    self.rotate(self.equal_rotations[self.get_side(stick[1]), "U'"])
                    self.rotate(self.equal_rotations[self.get_side(stick[1]), "F'"])
                    current = []
                    break
            if len(current) > 0:
                for angle in angles:
                    if current in angle:
                        self.rotate(self.equal_rotations[self.get_side(angle[1]), "F"])
                        self.rotate(self.equal_rotations[self.get_side(angle[1]), "U"])
                        self.rotate(self.equal_rotations[self.get_side(angle[1]), "R"])
                        self.rotate(self.equal_rotations[self.get_side(angle[1]), "U'"])
                        self.rotate(self.equal_rotations[self.get_side(angle[1]), "R'"])
                        self.rotate(self.equal_rotations[self.get_side(angle[1]), "F'"])

    def is_top_layer_solved(self):
        for i in range(46, 55):
            if self.state[i] != "YELLOW":
                return False
        return True

    def is_corners_top_layers_solved(self):
        for i in [7, 16, 25, 34]:
            if self.state[i] != self.state[i - 2]:
                return False
        for i in [1, 10, 19, 28]:
            if self.state[i] != self.state[i + 4]:
                return False
        return True

    def correct_corners_top_layer(self):
        while not self.is_corners_top_layers_solved():
            wrong_corners = []
            for i, j in [[7, 28], [16, 1], [25, 10], [34, 19]]:
                if self.state[i] == self.state[i - 2] and self.state[j] == self.state[j + 4]:
                    continue
                else:
                    wrong_corners.append([i, j])
            if len(wrong_corners) == 2:
                r = abs(wrong_corners[1][0] - wrong_corners[0][0])
                if r // 9 == 2:
                    side = self.get_side(wrong_corners[0][0])
                    self.rotate(self.equal_rotations[side, "L'"])
                    self.rotate(self.equal_rotations[side, "U"])
                    self.rotate(self.equal_rotations[side, "R"])
                    self.rotate(self.equal_rotations[side, "U'"])
                    self.rotate(self.equal_rotations[side, "L"])
                    self.rotate(self.equal_rotations[side, "U"])
                    self.rotate(self.equal_rotations[side, "L'"])
                    self.rotate(self.equal_rotations[side, "U"])
                    self.rotate(self.equal_rotations[side, "R'"])
                    self.rotate(self.equal_rotations[side, "U'"])
                    self.rotate(self.equal_rotations[side, "L"])
                    self.rotate(self.equal_rotations[side, "U2"])
                    self.rotate(self.equal_rotations[side, "R"])
                    self.rotate(self.equal_rotations[side, "U2"])
                    self.rotate(self.equal_rotations[side, "R'"])
                else:
                    side = self.get_side(wrong_corners[0][0])
                    self.rotate(self.equal_rotations[side, "R"])
                    self.rotate(self.equal_rotations[side, "U2"])
                    self.rotate(self.equal_rotations[side, "R'"])
                    self.rotate(self.equal_rotations[side, "U'"])
                    self.rotate(self.equal_rotations[side, "R"])
                    self.rotate(self.equal_rotations[side, "U2"])
                    self.rotate(self.equal_rotations[side, "L'"])
                    self.rotate(self.equal_rotations[side, "U"])
                    self.rotate(self.equal_rotations[side, "R'"])
                    self.rotate(self.equal_rotations[side, "U'"])
                    self.rotate(self.equal_rotations[side, "L"])
            else:
                self.rotate("U")

    def top_layer(self):
        while not self.is_top_layer_solved():
            count = 0
            for i in range(46, 55):
                if self.state[i] == "YELLOW":
                    count += 1
            if count == 5:
                for i in range(4):
                    if self.state[10] == self.state[16] == self.state[28] == self.state[34]:
                        self.rotate("F")
                        for j in range(3):
                            self.rotate("R")
                            self.rotate("U")
                            self.rotate("R'")
                            self.rotate("U'")
                        self.rotate("F'")
                        break
                    elif self.state[1] == self.state[7] == self.state[10] == self.state[34]:
                        self.rotate("R")
                        self.rotate("U2")
                        self.rotate("R2")
                        self.rotate("U'")
                        self.rotate("R2")
                        self.rotate("U'")
                        self.rotate("R2")
                        self.rotate("U2")
                        self.rotate("R")
                        break
                    else:
                        self.rotate("U")

            elif count == 6:
                for i in range(4):
                    if self.state[7] == self.state[16] == self.state[25] == self.state[48]:
                        self.rotate("R")
                        self.rotate("U2")
                        self.rotate("R'")
                        self.rotate("U'")
                        self.rotate("R")
                        self.rotate("U'")
                        self.rotate("R'")
                        break
                    elif self.state[10] == self.state[19] == self.state[28] == self.state[52]:
                        self.rotate("R")
                        self.rotate("U")
                        self.rotate("R'")
                        self.rotate("U")
                        self.rotate("R")
                        self.rotate("U2")
                        self.rotate("R'")
                    else:
                        self.rotate("U")
            elif count == 7:
                for i in range(4):
                    if self.state[10] == self.state[16] == self.state[46] == self.state[48]:
                        self.rotate("L2")
                        self.rotate("D'")
                        self.rotate("L")
                        self.rotate("U2")
                        self.rotate("L'")
                        self.rotate("D")
                        self.rotate("L")
                        self.rotate("U2")
                        self.rotate("L")
                        break
                    elif self.state[10] == self.state[34] == self.state[46] == self.state[52]:
                        self.rotate("R'")
                        self.rotate("F'")
                        self.rotate("L")
                        self.rotate("F")
                        self.rotate("R")
                        self.rotate("F'")
                        self.rotate("L'")
                        self.rotate("F")
                        break
                    elif self.state[1] == self.state[34] == self.state[46] == self.state[54]:
                        self.rotate("R'")
                        self.rotate("F'")
                        self.rotate("L'")
                        self.rotate("F")
                        self.rotate("R")
                        self.rotate("F'")
                        self.rotate("L")
                        self.rotate("F")
                        break
                    else:
                        self.rotate("U")
        self.correct_corners_top_layer()
        self.make_correct_top_cross()

    def is_top_cross_correct(self):
        edges = [4, 13, 22, 31]
        for i in edges:
            if self.state[i] != self.state[i + 1]:
                return False
        return True

    def make_correct_top_cross(self):
        while not self.is_top_cross_correct():
            current_directions = {
                4: 0,
                13: 0,
                22: 0,
                31: 0
            }
            edges = [4, 13, 22, 31]
            directions = {
                (4, 13): "r",
                (4, 22): "s",
                (4, 31): "l",
                (13, 4): "l",
                (13, 22): "r",
                (13, 31): "s",
                (22, 4): "s",
                (22, 13): "l",
                (22, 31): "r",
                (31, 4): "r",
                (31, 13): "s",
                (31, 22): "l"
            }
            for i in edges:
                if self.state[i] != self.state[i + 1]:
                    for j in edges:
                        if self.state[i] == self.state[j + 1]:
                            current_directions[i] = directions[(i, j)]
            dirs = list(current_directions.values())
            if dirs.count(0) == 1:
                for key, val in current_directions.items():
                    if val == 0:
                        side = self.get_side((key + 18) % 36)
                        cur_dir = current_directions[(key + 18) % 36]
                        if cur_dir == "l":
                            self.rotate(self.equal_rotations[side, "R2"])
                            self.rotate(self.equal_rotations[side, "U"])
                            self.rotate(self.equal_rotations[side, "R"])
                            self.rotate(self.equal_rotations[side, "U"])
                            self.rotate(self.equal_rotations[side, "R'"])
                            self.rotate(self.equal_rotations[side, "U'"])
                            self.rotate(self.equal_rotations[side, "R'"])
                            self.rotate(self.equal_rotations[side, "U'"])
                            self.rotate(self.equal_rotations[side, "R'"])
                            self.rotate(self.equal_rotations[side, "U"])
                            self.rotate(self.equal_rotations[side, "R'"])
                        elif cur_dir == "r":
                            self.rotate(self.equal_rotations[side, "R"])
                            self.rotate(self.equal_rotations[side, "U'"])
                            self.rotate(self.equal_rotations[side, "R"])
                            self.rotate(self.equal_rotations[side, "U"])
                            self.rotate(self.equal_rotations[side, "R"])
                            self.rotate(self.equal_rotations[side, "U"])
                            self.rotate(self.equal_rotations[side, "R"])
                            self.rotate(self.equal_rotations[side, "U'"])
                            self.rotate(self.equal_rotations[side, "R'"])
                            self.rotate(self.equal_rotations[side, "U'"])
                            self.rotate(self.equal_rotations[side, "R2"])
            elif dirs.count(0) == 0 and dirs.count("s"):
                self.rotate(self.equal_rotations[14, "R2"])
                self.rotate(self.equal_rotations[14, "L2"])
                self.rotate(self.equal_rotations[14, "D"])
                self.rotate(self.equal_rotations[14, "R2"])
                self.rotate(self.equal_rotations[14, "L2"])
                self.rotate(self.equal_rotations[14, "U2"])
                self.rotate(self.equal_rotations[14, "R2"])
                self.rotate(self.equal_rotations[14, "L2"])
                self.rotate(self.equal_rotations[14, "D"])
                self.rotate(self.equal_rotations[14, "R2"])
                self.rotate(self.equal_rotations[14, "L2"])
            elif dirs.count(0) == 0:
                self.rotate(self.equal_rotations[14, "R"])
                self.rotate(self.equal_rotations[14, "B'"])
                self.rotate(self.equal_rotations[14, "R'"])
                self.rotate(self.equal_rotations[14, "B"])
                self.rotate(self.equal_rotations[14, "F"])
                self.rotate(self.equal_rotations[14, "R'"])
                self.rotate(self.equal_rotations[14, "B'"])
                self.rotate(self.equal_rotations[14, "F"])
                self.rotate(self.equal_rotations[14, "R'"])
                self.rotate(self.equal_rotations[14, "B"])
                self.rotate(self.equal_rotations[14, "R"])
                self.rotate(self.equal_rotations[14, "F2"])
                self.rotate(self.equal_rotations[14, "U"])
            else:
                self.rotate("U")

    def solve(self):
        self.cross()
        self.first_layer()
        self.second_layer()
        self.top_cross()
        self.top_layer()
        print("Number of movements: " + str(len(self.solution)))
        for i in range(len(self.solution) - 1):
            if self.solution[i] == self.solution[i + 1]:
                if len(self.solution[i]) == 2 and self.solution[i] == "2":
                    self.solution[i] = ""
                    self.solution[i + 1] = ""
                else:
                    self.solution[i] = ""
                    self.solution[i + 1] = self.solution[i + 1][0] + "2"
        while "" in self.solution:
            self.solution.remove("")
        print(" ".join(self.solution))


cube = Rubiks_Cube()
canvas = Canvas(bg="white", width=240, height=200)
canvas.pack(anchor=CENTER, expand=1)

def draw_cube():
    global cube, canvas
    canvas.delete(ALL)
    i = 46
    for y in [0, 20, 40]:
        for x in [60, 80, 100]:
            canvas.create_rectangle(x, y, x + 20, y + 20, fill=cube.state[i])
            i += 1
    i = 1
    for x in [40, 20, 0]:
        for y in [60, 80, 100]:
            canvas.create_rectangle(x, y, x + 20, y + 20, fill=cube.state[i])
            i += 1
    i = 10
    for x in [100, 80, 60]:
        for y in [60, 80, 100]:
            canvas.create_rectangle(x, y, x + 20, y + 20, fill=cube.state[i])
            i += 1
    i = 19
    for x in [160, 140, 120]:
        for y in [60, 80, 100]:
            canvas.create_rectangle(x, y, x + 20, y + 20, fill=cube.state[i])
            i += 1
    i = 28
    for x in [220, 200, 180]:
        for y in [60, 80, 100]:
            canvas.create_rectangle(x, y, x + 20, y + 20, fill=cube.state[i])
            i += 1
    i = 37
    for y in [120, 140, 160]:
        for x in [60, 80, 100]:
            canvas.create_rectangle(x, y, x + 20, y + 20, fill=cube.state[i])
            i += 1
    canvas.update()

def main():
    global cube
    draw_cube()
    root = Tk()
    root.title("Rubik's Cube Solver")
    root.geometry("200x200+100+100")
    scramble_btn = Button(root, text="Scramble", command=cube.scramble, width=10)
    scramble_btn.pack()

    solve_btn = Button(root, text="Solve", command=cube.solve, width=10)
    solve_btn.pack()

    solve_cross_btn = Button(root, text="Cross", command=cube.cross, width=10)
    solve_cross_btn.pack()

    solve_first_layer_btn = Button(root, text="First Layer", command=cube.first_layer, width=10)
    solve_first_layer_btn.pack()

    solve_second_layer = Button(root, text="Second Layer", command=cube.second_layer, width=10)
    solve_second_layer.pack()

    solve_top = Button(root, text="Top layer", command=cube.solve, width=10)
    solve_top.pack()

    root.mainloop()
    root.mainloop()


main()