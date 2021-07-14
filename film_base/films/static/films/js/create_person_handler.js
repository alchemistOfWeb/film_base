function add_person(){
    const $dp_menu = $(this).closest(`.dropdown-menu:not(.inner)`) 
    const $search_input = $dp_menu.find('input[type=search]')

    let person_name = $search_input.val()
    
    const $form = $(this).closest('form')
    const url = $form.attr('action')
    const csrf_token = $form.find('input[name=csrfmiddlewaretoken]').val()
    const user_wants = confirm(`Are you sure you want to add a new person with name ${person_name}?`)
    
    if (user_wants) {
        $.ajax({
            url,
            method: 'post',
            dataType: 'json',
            data: {person_name, csrfmiddlewaretoken: csrf_token},
            context: this,
            success: function(data) {
                add_message('Person is added successfuly', 'success')
                console.log('success')
            },
            error: function(err) {
                if (err.status == 403) {
                    add_message('You need to login for this action!', 'danger')
                } else {
                    add_message('Error', 'danger')
                }
                console.log('error')
            }
        })
    }
}

// const $selectpickers = $('.selectpicker')
// $selectpickers.each(function(index, selectpicker){
//     $selectpicker = $(selectpicker)
//     console.log($selectpicker[0])
    
//     $selectpicker.on('loaded.bs.select', function(){
//         $hidden_block = $(`.hidden-block-for-selectpicker[data-for-select=${$(this).attr('id')}]`)
//         console.log($hidden_block.html())
//         $(this).attr('data-none-results-text', $hidden_block.html())
//         // $(this).selectpicker('refresh')
//         // $(this).selectpicker('render')
//     })
// }) 

const $hidden_block_nodes = $('.hidden-block-for-selectpicker')

$hidden_block_nodes.each(function(index, hidden_block) {
    
    $hidden_block = $(hidden_block)
    // console.log($hidden_block[0])
    // console.log($hidden_block.attr('data-for-select'))
    let $selectpicker = $('#'+$hidden_block.attr('data-for-select'))
    
    $selectpicker.attr('data-none-results-text', $hidden_block.html())
    // console.log($selectpicker.attr('data-none-results-text'))
    // console.log($selectpicker[0])
    
    $selectpicker.find('.no-results')
})
