var EventHandler = (function(){

    function find(data, item){
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
               $("#other").attr('href', '/store/review_all/' + item);
            },
            error: function(e){

            }
        });
    }

    return {
        find: find
    }
})();
