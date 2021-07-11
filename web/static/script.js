var board_img = document.getElementById("board-img");

function viewport_set(){
    //setting container width
    var board_img_width = board_img.getBoundingClientRect().width; //stackoverflow.com/questions/294250
    document.getElementById("board").style.width = board_img_width+"px";
}

function onLoad(){
    viewport_set();
}

window.onresize = function() {
    viewport_set();
}

function drawBoard(grid){
    for (let i = 0; i < 10; i++){
        for (let j = 0; j < 9; j++){
            var id2draw = "#position-grid-"+i+"-"+j;
            var img2draw = $(id2draw).children("img");
            
            if (img2draw.attr("src") != grid[i][j]){
                img2draw.attr("src", grid[i][j]);
            }
        }
    }
}

$(function() {
    $("td.position-grid-cell-div").on("click", function(e) {
        //e.preventDefault()
        var positionId = $(this).attr("id").match(/\d+/g);
        
        $.ajax({
        type: "PUT",
        url: "/index",
        data: { position: JSON.stringify(positionId) },
        dataType: "json",
        error: function(xhr,status,error){
            alert("ERROR: " + xhr.status + ": " + xhr.statusText + "\n" + status + "\n" + error);
        },
        success: function(result,status,xhr){
            console.log(result);
            var debug = result["debug"];
            var grid = result["grid"];
            $('#debug-text').html(debug);
            drawBoard(grid);
        }
        });
        
        return false;
    });
});

/*function clickGrid(i, j){
    var bgImg = "url(\"images/qi/target.png\")";
    var selector = document.getElementById("position-grid-"+i+"-"+j).style;
    if (!selector.background){
        
        selectorAnnihilator:
        for (let n = 0; n < 9; n++){
            for(let m = 0; m < 10; m++){
                selector_loop = document.getElementById("position-grid-"+m+"-"+n).style
                if(!selector_loop.background||(m==i&&n==j)){}else{
                    selector_loop.background = "";
                    break selectorAnnihilator;
                }
            }
        }
        
        selector.background = bgImg;
        selector.backgroundRepeat = "no-repeat";
        selector.backgroundSize = "100% 100%";
    }else{
        selector.background = "";
    }
}*/
