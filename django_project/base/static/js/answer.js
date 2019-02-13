function addAnswer() {
    var $input = $('input[name="answer"]');
    var answer = $input.val();
    if(answer !== ''){
        $input.val('');
        $.ajax({
            type: 'POST',
            url: answerUrl,
            data: {
                'answer': answer,
                'csrfmiddlewaretoken': csrfToken
            },
            success: function () {
                $('.answer-wrapper').append('<div class="answer-item">' + answer + '</div>');
            },
            error: function (xhr) {
                alert(xhr.responseText)
            }
        })
    }
}