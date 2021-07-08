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

$(".position-grid-cell-div").click(function(){
    

});

function clickGrid(i, j){
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
}
