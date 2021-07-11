import services.chess
from services.chess import *

#Flask: Web app wrapper
from flask import Flask, render_template, request, escape, url_for, redirect, make_response
from flask import jsonify
app = Flask(__name__,
            static_url_path="",
            static_folder="web/static",
            template_folder="web/templates")
            
from flask_restful import Resource, Api

#transform board notation to which images to put
DISPLAY_POSITION_PIECE = {
            0: "empty",
            17: "black_knight",
            21: "black_cannon",
            20: "black_car",
            18: "black_elephant",
            16: "black_general",
            19: "black_horse",
            22: "black_pawn",
            9: "red_knight",
            13: "red_cannon",
            12: "red_car",
            10: "red_elephant",
            8: "red_general",
            11: "red_horse",
            14: "red_pawn"
        }
for i in DISPLAY_POSITION_PIECE:
    DISPLAY_POSITION_PIECE.update({i:"images/qi/" + DISPLAY_POSITION_PIECE[i] + ".png"})

#initialize grids
grid_base = [[]] * 10
for i in range(len(grid_base)):
    grid_base[i] = [""] * 9

b = services.chess.Board(START_POSITION).board_data
debug = str(b)
grid = grid_base[:]

#Starting web app
@app.route("/index", methods=["GET", "POST", "PUT"])
def index():
    #update()
    #return render_template("index.html")
    global debug
    global grid
    
    #idfk where this came from
    if request.method == "GET":
        debug = "This is GET!"
        
        return render_template("index.html", debug=debug, grid=grid)
    
    #background process: clicking board elements
    elif request.method == "PUT":
        debug = request.form.get("position")
        
        return jsonify({"debug":debug, "grid":grid})
        
    
    #post method, only called at initiation (?)
    else:
        grid = translate_board_data(b)
        
        return render_template("index.html", debug=debug, grid=grid)
        



def translate_board_data(b):
    grid_temp = [x[:] for x in grid_base]
    for i in range(2,11):
        for j in range(2,12):
            grid_temp[j-2][i-2] = DISPLAY_POSITION_PIECE.get(b[j][i], "")
    return grid_temp

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
