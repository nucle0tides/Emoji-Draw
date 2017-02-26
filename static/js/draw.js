var canvas = new fabric.Canvas('drawing-canvas');

var img_loader = document.getElementById('img_load');
img_loader.addEventListener('change', handle_img, false); 

// $('.emoji').click(function(){
//     // console.log($(this).attr('id')); 
//     console.log('click'); 
//     fabric.Image.fromURL('static/images/emojis/' + $(this).attr('id') + '.png', function(img) {
//       img.perPixelTargetFind = true;
//       img.targetFindTolerance = 4;
//       img.hasControls = img.hasBorders = true;

//       canvas.add(img);
//     });
// });

$(document).on('click', '.emoji', function () {
    // console.log($(this).attr('id')); 
    console.log('click'); 
    fabric.Image.fromURL('static/images/emojis/' + $(this).attr('id') + '.png', function(img) {
      img.perPixelTargetFind = true;
      img.targetFindTolerance = 4;
      img.hasControls = img.hasBorders = true;

      canvas.add(img);
    });
});

$('#save_img').click(function() { 
    if(!window.localStorage){alert("This function is not supported by your browser."); return;}
    // to PNG
    window.open(canvas.toDataURL('png'));
})


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
  var xhttp = new XMLHttpRequest();
  var emojis = null;  
  var emoji_list = new XMLHttpRequest();
  emoji_list.onreadystatechange = function() {
    if (emoji_list.readyState == 4 && emoji_list.status == 200) { 
      emojis = emoji_list
      // console.log(emojis.responseText); 
      // console.log(JSON.parse(emojis.responseText));
      emojis = JSON.parse(emojis.responseText); 
      place_emojis(emojis); 
    }
  };
  var emoji_search = document.getElementById('emoji_search').value
  if(emoji_search){ 
    emoji_list.open("GET", "/getEmojiByCategory/" + emoji_search, true);
    emoji_list.send();
  }
  else{ 
    console.log("no emojis");
  }
}

// bleeding
// i am BLEEDING
function place_emojis(list_o_emojis) { 
    var html_to_place = ''; 
    for(var i = 0; i < list_o_emojis.length; i++) {  
        if (i % 5 != 0) { 
            html_to_place += '<div class="col s2"><img src="/static/images/emojis/' + list_o_emojis[i] + '.png" class="emoji" id="' + list_o_emojis[i] +'"></div>'; 
        } 
        else { 
            html_to_place += '<div class="col s2"><img src="/static/images/emojis/' + list_o_emojis[i] + '.png" class="emoji" id="' + list_o_emojis[i] +'"></div>';
        }
    }
    console.log(html_to_place); 
    $('.emoji-lists').children().remove(); 
    $('.emoji-lists').append(html_to_place); 
}

$(document).ready(function(){

});