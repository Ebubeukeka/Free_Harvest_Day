$( document ).ready(function() {
  console.log( "ready!" );
  $( "#image_button" ).click(function() {
    $( "#pop_up_wrapper" ).removeClass( "display_none" ).addClass( "display_block" );
  });
 });

 $( document ).ready(function() {
  console.log( "ready!" );
  $( ".close" ).click(function() {
    $( "#pop_up_wrapper" ).removeClass( "display_block" ).addClass( "display_none" );
  });
 });