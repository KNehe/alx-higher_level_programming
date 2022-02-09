$(function () {
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    const ul = $('ul.my_list li');
    ul[ul.length - 1].remove();
  });
  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
