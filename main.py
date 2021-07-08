import services.chess
from services.chess import *

#Flask: Web app wrapper
from flask import Flask, render_template, request, escape, url_for
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
    DISPLAY_POSITION_PIECE.update({i:"<img src=\"images/qi/" + DISPLAY_POSITION_PIECE[i] + ".png\" class=\"qi\"/>"})
#initialize grids
grid = []
for i in range(10):
    grid.append([])
    for j in range(9):
            grid[i].append("")

#Starting web app
@app.route("/index", methods=["GET", "POST"])
def index():
    #update()
    #return render_template("index.html")
    
    if request.method == "POST":
        debug = "This is POST!"#update()
        
        return render_template("index.html", result=debug, grid=grid)
    else:
        debug = str(initiate())
        
        b_start = services.chess.Board(START_POSITION).board_data
        for i in range(2,11):
            for j in range(2,12):
                grid[j-2][i-2] = DISPLAY_POSITION_PIECE.get(b_start[j][i], "")
                print(b_start[i][j])

        return render_template("index.html", result=b_start, grid=grid)
    
def initiate():
    return services.chess.initiate_html()
    
def update(position):
    return services.chess.update_html(position)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
