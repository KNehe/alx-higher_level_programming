$('#toggle_header').click(function () {
  $('header').addClass('red');

  if ($('header').hasClass('red')) {
    $('header').toggleClass('green');
  }

  if ($('header').hasClass('green')) {
    $('header').toggleClass('red');
  }
});
