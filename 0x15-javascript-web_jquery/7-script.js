$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (res, status) {
  if (status === 'success') {
    $('#character').text(res.name);
  }
});
