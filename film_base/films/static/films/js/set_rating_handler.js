function add_message(msg_content, type) {
    msg_html = `<div class="alert alert-${type} alert-dismissible fade show" role="alert">${msg_content}<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>`

    $messages_container = $('.messages')

    $messages_container.append(msg_html)
}

$(()=>{
    

    $('input[name=rating]').change('change', function(){
        $film_card = $(this).closest('.film-card');
        url = $(this).closest('form').attr('action');
        film_id = $film_card.attr('data-film-id');
        rating = $(this).attr('value');
        csrf_token = $film_card.find('input[name=csrfmiddlewaretoken]').attr('value');

        $.ajax({
            url,
            method: 'post',
            dataType: 'json',
            data: {film_id, rating, csrfmiddlewaretoken: csrf_token},
            context: $film_card,
            success: function(data) {
                console.info(`status: ${data.status}\n${data.average_score}\nuser: ${data.user}\nmessage: ${data.message}` )
            
                $(this).find('label[for=average-score]>span').text(data.average_score)
            },
            error: function(err) {
                if (err.status == 403) {
                    add_message('You need to login to rate films!', 'danger')
                }

            }
        });
    });

})