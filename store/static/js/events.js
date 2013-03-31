var EventHandler = (function(){

    function find(data){
        $.ajax({
            url:'/store/products/',
            data: data,
            type: 'POST',
            dataType: "html",
            success: function(data){
                var result = $('#list_for_found_items');
                result.show();

               $('#modal').show();
               result.html(data);
               $("#other").attr('href', '/store/review/' + $('#search_form input[type=text]').val());
            },
            error: function(e){
                console.log(e.error())
            }
        });
    }

    return {
        find: find
    }
})();
