
$(document).ready(function(){
    $('#search_form input[type=text]').keypress(function(){

            var data = $('input[type=text]').val();

            EventHandler.find(({request: data}));
    });

    $('a, #modal, input[type=submit]').click(function(){
        $('#list_for_found_items, #modal').fadeOut();
    });

    $('.filter').click(function(){
        EventHandler.find(filter());
    });
    $('.input_filter').click(function(){
        $(this).blur(function(){
            EventHandler.find(filter());
        });
    });
});

function filter(){
    var data = new Object()

    return(
    {
        cathegorie:   $('select[name=cathegories]').val(),
        mark:         $('select[name=mark]').val(),
        low_price:    $('input[name=low_price]').val(),
        high_price:   $('input[name=high_price]').val(),
        availability: $('input[name=availability]').is(":checked"),
        hdd:          $('input[name=hdd]').val(),
        proccesor:    $('input[name=proccesor]').val(),
        os:           $('input[name=os]').val(),
        diagonal:     $('input[name=diagonal]').val()

    });
}