var wordCount = $('.word_count').html();

$(function() {
  if (wordCount < 50) {
    $('.word-cloud').css('width', '200px');
    $('.word-cloud').css('line-height', '.6');
    // $('.word-cloud').css('border-radius', '50%');
  } else if (wordCount < 100) {
    $('.word-cloud').css('width', '260px');
    $('.word-cloud').css('line-height', '.6');
    // $('.word-cloud').css('border-radius', '50%');
  } else if (wordCount < 400) {
    $('.word-cloud').css('width', '500px');
    $('.word-cloud').css('line-height', '.6');
    // $('.word-cloud').css('border-radius', '50%');
  } else if (wordCount < 800) {
    $('.word-cloud').css('width', '700px');
    $('.word-cloud').css('line-height', '.6');
    // $('.word-cloud').css('border-radius', '50%');
  } else {
    $('.word-cloud').css('width', '80%');
    $('.word-cloud').css('line-height', '.4');
    // $('.word-cloud').css('border-radius', '50%');
  }
});