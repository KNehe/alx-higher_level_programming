-- Lists all genres and shows linked to each genre
SELECT tv_genres.anme AS genre, COUNT(*) AS 'number_of_shows' FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY genre ORDER BY number_of_shows DESC;
