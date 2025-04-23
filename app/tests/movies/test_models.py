# app/tests/movies/test_models.py

import pytest

from movies.models import Movie

# @pytest.mark.django_db
# def test_movie_model():
#     movie = Movie(title="Raising Arizona", genre="comedy", year="1987")
#     movie.save()
#     assert movie.title == "Raising Arizona"
#     assert movie.genre == "comedy"
#     assert movie.year == "1987"
#     assert movie.created_date
#     assert movie.updated_date
#     assert str(movie) == movie.title

@pytest.mark.django_db
def test_add_movie(client):
    # movies = Movie.objects.all()
    # assert len(movies) == 0
    res = client.post(
        "/api/movies/",
        {
            "title": "Raising Arizona",
            "genre": "comedy",
            "year": "1987"
        },
        content_type="application/json",
    )
    assert res.status_code == 201
    assert res.data["title"] == "Raising Arizona"

    movies = Movie.objects.all()
    assert len(movies) == 1



