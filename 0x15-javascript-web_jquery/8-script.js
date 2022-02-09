$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (res, status) {
  if (status === 'success') {
    const films = res.results;
    for (const film of films) {
      const li = document.createElement('li');
      li.textContent = film.title;
      $('#list_movies').append(li);
    }
  }
});
