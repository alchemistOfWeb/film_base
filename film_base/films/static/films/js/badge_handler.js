$(()=>{
    $('.detach-option-btn').bind('click', function(){
        $att_block = $(this).closest('.attaching-block')

        $attached_list = $(this).closest('.attached-list')
        select_id = $attached_list.attr('data-for-select')
        $select = $(`#${select_id}`)


        att_title = $att_block.find('.selected-option-name').text()
        att_value = $att_block.find('.attaching-option-hidden').val()

        // console.log(select_id)

        $select.append(`<option value="${att_value}" data-tokens="${att_title}">${att_title}</option>`)
        $select.selectpicker('refresh')
        
        $att_block.remove()
    })

    $('.selectpicker').on('changed.bs.select', function(e, clickedIndex, isSelected, previousValue){
        $option = $(this).find(`option:nth-child(${clickedIndex+1})`)

        $attached_list = $(`.attached-list[data-for-select=${$(this).attr('id')}]`)
        $new_bage_blank = $attached_list.find('.attaching-block[hidden]').clone(true, true)
        $new_bage_blank.removeAttr('hidden')
        
        
        attaching_title = $option.text()
        attaching_value = $option.val()

        $new_bage_blank.find('.selected-option-name').text(attaching_title)
        $new_bage_blank.find('.attaching-option-hidden').val(attaching_value).removeAttr('disabled')
        console.log($new_bage_blank[0])
        $attached_list.append($new_bage_blank)

        $option.remove()

        $(this).selectpicker('refresh')
    })
})