$('#add_item').click(function () {
  const li = document.createElement('li');
  li.textContent = 'Item';
  $('ul.my_list').append(li);
});
