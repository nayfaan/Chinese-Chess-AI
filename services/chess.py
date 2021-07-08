import numpy as np

EMPTY, OUTBOUND = 0, -1
RED_GENERAL, RED_KNIGHT, RED_ELEPHANT, RED_HORSE, RED_CAR, RED_CANNON, RED_PAWN = 8, 9, 10, 11, 12, 13, 14
BLACK_GENERAL, BLACK_KNIGHT, BLACK_ELEPHANT, BLACK_HORSE, BLACK_CAR, BLACK_CANNON, BLACK_PAWN = 16, 17, 18, 19, 20, 21, 22

START_POSITION = "rheagaehr/9/1c5c1/s1s1s1s1s/9/9/S1S1S1S1S/1C5C1/9/RHEAGAEHR"

READ_POSITION_PIECE = {
            'a': BLACK_KNIGHT,
            'c': BLACK_CANNON,
            'r': BLACK_CAR,
            'e': BLACK_ELEPHANT,
            'g': BLACK_GENERAL,
            'h': BLACK_HORSE,
            's': BLACK_PAWN,
            'A': RED_KNIGHT,
            'C': RED_CANNON,
            'R': RED_CAR,
            'E': RED_ELEPHANT,
            'G': RED_GENERAL,
            'H': RED_HORSE,
            'S': RED_PAWN
        }

class Board:
    def __init__(self, position="9/9/9/9/9/9/9/9/9/9"):
        self.board_data = self.__start_empty_board__()
        self.read_board(position)
    
    def __str__(self):
        s = ""
        for i in self.board_data:
            s += str("[ ")
            for j in i:
                s += ('%2d ' % j)
            s += "]\n"
        return s
        
    def __start_empty_board__(self):
        board_data = []
        for i in range(14):
            board_data.append([])
            for j in range(13):
                if i < 2 or i > 11 or j < 2 or j > 10:
                    board_data[i].append(OUTBOUND)
                else:
                    board_data[i].append(EMPTY)
        return board_data
        
    def read_board(self, position):
        loc_x, loc_y = 2, 2
    
        for i in position:
            if i.isnumeric():
                for j in range(int(i)):
                    self.board_data[loc_y][loc_x] = 0
                    loc_x += 1
            elif i == "/":
                loc_y = loc_y + 1
                loc_x = 2
            else:
                self.board_data[loc_y][loc_x] = READ_POSITION_PIECE.get(i, 0)
                loc_x += 1

def initiate_html():
    b = Board(START_POSITION)
    return b.board_data

def update_html(position):
    b = Board(START_POSITION)
    return b.board_data

if __name__ == "__main__":
    b = Board(START_POSITION)
    print(b)
