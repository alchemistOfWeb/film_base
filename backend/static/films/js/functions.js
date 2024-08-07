function add_message(msg_content, type) {
    msg_html = `<div class="alert alert-${type} alert-dismissible fade show" role="alert">${msg_content}<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>`

    $messages_container = $('.messages')

    $messages_container.append(msg_html)
}