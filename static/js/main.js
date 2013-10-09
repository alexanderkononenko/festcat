$(document).ready(function() {
    var sort = 'date_start-desc';

    $('#filter_name').keyup(function() {
        if ($(this).val().length >= 2 || $(this).val().length == 0) {
            loadPage($(this).val(), sort);
        }
    });

    var loadPage = function (filter, order) {
        $("#contentWrapper").html('Loading...');
        $.ajax('/list/?filter='
                +encodeURIComponent(filter)
                +'&order='+encodeURIComponent(order)).done(function (data) {
            if (data != ''){
                $("#contentWrapper").html(data);
                $('a.sort').click(function() {
                    sort = $(this).attr('data-sort');
                    loadPage($('#filter_name').val(), sort);
                    return false;
                });
            } else {
                $("#contentWrapper").html('Something wrong!');
            }
        });
    }
    
    loadPage('', 'date_start+desc');
});
