var canvas = new fabric.Canvas('drawing-canvas');

var img_loader = document.getElementById('img_load');
img_loader.addEventListener('change', handle_img, false);

$('.emoji').click(function(){
    console.log($(this).attr('id')); 

    for (var i = 0, len = 15; i < len; i++) {
        fabric.Image.fromURL('static/images/emojis/' + $(this).attr('id') + '.png', function(img) {
          img.set({
            left: fabric.util.getRandomInt(0, 600),
            top: fabric.util.getRandomInt(0, 500),
            angle: fabric.util.getRandomInt(0, 90)
          });

          img.perPixelTargetFind = true;
          img.targetFindTolerance = 4;
          img.hasControls = img.hasBorders = false;

          img.scale(fabric.util.getRandomInt(50, 100) / 100);

          canvas.add(img);
        });
    }  
});


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

function get_emojis()
{
  var emojis = null; 
  var xhttp = new XMLHttpRequest();
  
  var emoji_list = new XMLHttpRequest();
  emoji_list.onreadystatechange = function() {
    if (emoji_list.readyState == 4 && emoji_list.status == 200) { 
      emojis = emoji_list
      console.log(emojis) 
    }
  };
  var emoji_search = document.getElementById('emoji_search').value
  if(emoji_search){ 
    emoji_list.open("GET", "/getEmojiByCategory/" + user, true);
    emoji_list.send();
  }
  else{ 
    console.log("no emojis");
  }
}

$(document).ready(function(){

});