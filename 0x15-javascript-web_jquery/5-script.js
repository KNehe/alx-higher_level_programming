$('#add_item').click(function () {
  const li = document.createElement('li');
  li.textContent = 'Item';
  $('my_list').append(li);
});
