// $( document ).ready(function() {
//     console.log( "ready!" );
//     $("#a").on("click",function(e){
//         var top=e.pageY-$(this).position().top,
//             left=e.pageX-$(this).position().left;
//         $('.imgajoutee').remove();
//         $(this).append("<img src='.//images/click_test.png' class='imgajoutee' style='top:"+top+"px;left:"+left+"px;'/>");
//         console.log(top);
//         console.log(left);
//     });
// });

$(document).ready(function(){ 
    $(document).click(function (ev) {
            mouseX = ev.pageX;
            mouseY = ev.pageY
            console.log(mouseX + ' ' + mouseY);
            var color = 'red';
            var size = '10px';
        //   $('.dot').remove();
            $("body").append(
                $('<div></div>')
                    .css('position', 'absolute')
                    .css('top', mouseY - 3 + 'px')
                    .css('left', mouseX - 3 + 'px')
                    .css('width', size)
                    .css('height', size)
                    .css('background-color', color)
                    .addClass('dot')
            );
        });
     });
    