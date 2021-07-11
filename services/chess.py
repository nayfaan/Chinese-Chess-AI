import numpy as np
from termcolor import colored

EMPTY, OUTBOUND = 0, -1
RED_GENERAL, RED_KNIGHT, RED_ELEPHANT, RED_HORSE, RED_CAR, RED_CANNON, RED_PAWN = 9, 10, 11, 12, 13, 14, 15
BLACK_GENERAL, BLACK_KNIGHT, BLACK_ELEPHANT, BLACK_HORSE, BLACK_CAR, BLACK_CANNON, BLACK_PAWN = 17, 18, 19, 20, 21, 22, 23

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

GRAPHIC_PIECE_DATA = {
    str(RED_KNIGHT):   ("█  █  █",
                        "█ ███ █",
                        "██ █ ██",
                        "██   ██",
                        "███ ███",
                        "███████",
                        "███████",
                        " █████ ",
                        "  ███  "),
                     
    str(RED_CANNON):   ("███████",
                        " █████ ",
                        " █████ ",
                        " █████ ",
                        " ██  █ ",
                        " █ ██ █",
                        " █ ██ █",
                        " ██  █ ",
                        "  ███  "),
                     
    str(RED_CAR):      ("█ █ █ █",
                        "███████",
                        " █████ ",
                        " █████ ",
                        " █████ ",
                        " █████ ",
                        " █████ ",
                        "███████",
                        "███████"),
                     
    str(RED_ELEPHANT): ("  ███  ",
                        "  █ █  ",
                        " █   █ ",
                        " ██ ██ ",
                        "  ███  ",
                        "  ███  ",
                        " █████ ",
                        "███████",
                        "███████"),
                     
    str(RED_GENERAL):  ("█ █ █ █",
                        "█ █ █ █",
                        " █ █ █ ",
                        "  █ █  ",
                        "  ███  ",
                        "  ███  ",
                        " █████ ",
                        " █████ ",
                        "███████"),
                     
    str(RED_HORSE):    ("█████  ",
                        " █████ ",
                        " █ ████",
                        " ██████",
                        " ██████",
                        " ███ ██",
                        " ███ ██",
                        "    ███",
                        "███████"),
                     
    str(RED_PAWN):     ("  ███  ",
                        "  ███  ",
                        "  ███  ",
                        "   █   ",
                        "  ███  ",
                        "  ███  ",
                        " █████ ",
                        "███████",
                        "███████"),
                     
    str(EMPTY):        ("       ",
                        "       ",
                        "       ",
                        "       ",
                        "       ",
                        "       ",
                        "       ",
                        "       ",
                        "       ")
}

def graphic_piece_lookup(num, line):
    p = {}
    p.update({"color": int(np.floor(num / 8))})
    if num != 0: p.update({"type": num % 8 + 8})
    else:p.update({"type": 0})
    
    output = GRAPHIC_PIECE_DATA.get(str(p.get("type")))[line]
    if p.get("color") == 2:
        output = colored(output, "red")
    return output

def graphic_piece(p):
    graph = ""
    
    for i in range(9):
        for j in p[2:-2]:
            graph += "│  "
            graph += graphic_piece_lookup(j,i)
            graph += "  "
        graph += "│\n"
    
    return graph

class Board:
    def __init__(self, position="9/9/9/9/9/9/9/9/9/9"):
        self.board_data = self.__start_empty_board__()
        self.read_board(position)
    
    def __str__(self):
        width = 11
        s = ("┌" + ("─" * width + "┬") * 9)[:-1] + "┐\n"
        active_board = self.board_data[2:-2]
        for i in range(len(active_board)):
            s += graphic_piece(active_board[i])
            if i != len(active_board) -1:
                s += (("├" + ("─" * width + "┼") * 9)[:-1] + "┤\n")
            if i == 4:
                s += (("│" + (" " * (width + 1)) * 9)[:-1] + "│\n") *3
                s += (("├" + ("─" * width + "┼") * 9)[:-1] + "┤\n")
        s += (("└" + ("─" * width + "┴") * 9)[:-1] + "┘\n")
            
        '''for i in self.board_data:
            s += str("[ ")
            for j in i:
                s += ("%2d " % j)
            s += "]\n"'''
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
    
    def code_board(self):
        code = ""
        consecutive = 0
        for i in range(1):
            for j in range(1):
                pass #TBW
        return code
        
    
def click_board(position):
    
    return 0

if __name__ == "__main__":
    b = Board(START_POSITION)
    print(b)
