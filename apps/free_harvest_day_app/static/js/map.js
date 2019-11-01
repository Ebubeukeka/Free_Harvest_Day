$( document ).ready(function() {
    console.log( "ready!" );
    $(".map").on("click",function(e){
        var top=e.pageY-$(this).position().top, left=e.pageX-$(this).position().left;
        $('.imgajoutee').remove();
        $(this).append("<img src='../images/click_test.png' class='imgajoutee' style='top:"+top+"px;left:"+left+"px;'/>");
        console.log(top);
        console.log(left);
});
});