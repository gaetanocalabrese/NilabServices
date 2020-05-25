$('.apireq').click( function() {
    $.ajax({
             url : "http://localhost:8000/longtasksapi",
             dataType: "json",
             success : function (data) {
                      $('#id').text( data[0].id);
                      $('#name').text( data[0].name);
                      $('#result').text( data[0].result);
                      $('#job_id').text( data[0].jpb_id);

                    }
                 });
             });



 function twitter_data()  {
    $.ajax({
             url : "http://localhost:8000/longtasksapi",
             dataType: "json",
             headers: { 'Access-Control-Allow-Origin': '*' },
             success : function (data) {


  var items = [];
  $.each( data, function( key, val ) {
    items.push( "<li id='" + key + "'>" + val + "</li>" );
  });

  $( "<ul/>", {
    "class": "my-new-list",
    html: items.join( "" )
  }).appendTo( "#jsonresp" );

}
});
}