var canvas = new fabric.Canvas('drawing-canvas');

var img_loader = document.getElementById('img_load');
img_loader.addEventListener('change', handle_img, false);


function handle_img(e){
    var reader = new FileReader();
    reader.onload = function(event){
        var img = new Image();
        img.onload = function(){
            var f_img = new fabric.Image(img);
            f_img.scaleToWidth(canvas.getWidth());
            canvas.setBackgroundImage(f_img);
            canvas.renderAll();
        }
        img.src = event.target.result;
    }
    reader.readAsDataURL(e.target.files[0]);     
}


$(document).ready(function(){

});