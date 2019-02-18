$(document).ready(function () {
    $('.message-banner').fadeOut(2000);

    (function worker() {
      $.ajax({
        url: getAnswerUrl,
        success: function(data) {
            var answers = data['answers'];
            if(answers !== ''){
                var list_answers = answers.split(',');
                var $answerWrapper = $('.answers-collected');
                $answerWrapper.html('');
                for(var index in list_answers){
                    $answerWrapper.append('<div class="answer-item">' + list_answers[index] + '</div>');
                }
            }
        },
        complete: function() {
          // Schedule the next request when the current one's complete
          setTimeout(worker, 1000);
        }
      });
    })();

});