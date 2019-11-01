$( document ).ready(function() {
  console.log( "ready!" );
// using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    $(document).click(function (ev) {
        mouseX = ev.pageX;
        mouseY = ev.pageY;
        console.log(mouseX + ' ' + mouseY);
        var color = 'red';
        var size = '10px';
    //   $('.dot').remove();
        if(mouseX > 0 && mouseX < 825 && mouseY > 0 && mouseY < 375){
            var testg = "True";
            console.log(testg);
            $("#a").append(
                $('<div></div>')
                .css('position', 'absolute')
                .css('top', mouseY - 3 + 'px')
                .css('left', mouseX - 3 + 'px')
                .css('width', size)
                .css('height', size)
                .css('background-color', color)
                .addClass('dot')
            );
        }
    });
});
$( document ).ready(function() {
    console.log( "ready!" );
    $( "img" ).click(function() {
        $( ".pop_up_wrapper" ).removeClass( "display_none" ).addClass( "display_block" );
    });
    $( ".close" ).click(function() {
        $( ".pop_up_wrapper" ).removeClass( "display_block" ).addClass( "display_none" );
    });
    $("#dot").click(function() {
        $( "#new_volunteer_form").removeClass( "display_none" ).addClass(
        "display_block" );
    });
    $( ".close" ).click(function() {
        $( "#new_volunteer_form" ).removeClass( "display_block" ).addClass( "display_none" );
    });
    $(".garden_display").click(function() {
        $( "#new_volunteer_form").removeClass( "display_none" ).addClass(
        "display_block" );
    });
    $( ".close" ).click(function() {
        $( "#new_volunteer_form" ).removeClass( "display_block" ).addClass( "display_none" );
    });
 });