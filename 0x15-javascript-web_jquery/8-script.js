$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (res, status) {
  if (status === 'success') {
    const li = document.createElement('li');
    const films = res.results;
    for (const film of films) {
      li.textContent = film.title;
      $('#list_movies').append(li);
    }
  }
});
