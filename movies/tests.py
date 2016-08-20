from django.test import TestCase
from movies import api
from movies import testdata


class OMBDAPITestCase(TestCase):

    @testdata.GetMovieValidResponse.decorate
    def test_valid_get_movie_by_title(self):
        title = testdata.GetMovieValidResponse.title
        year = testdata.GetMovieValidResponse.year
        resp = api.get_movie_by_title(title, year)
        expected_response = {'rated': 'R',
                             'language': 'English',
                             'title': 'The Matrix',
                             'imdb_id': 'tt0133093',
                             'director': 'Lana Wachowski, Lilly Wachowski',
                             'imdb_rating': '8.7',
                             'year': '1999'}
        self.assertEqual(resp, expected_response)

    @testdata.GetMovieValidResponse.decorate(status=404)
    def test_404_get_movie_by_title(self):
        title = testdata.GetMovieValidResponse.title
        year = testdata.GetMovieValidResponse.year
        resp = api.get_movie_by_title(title, year)
        expected_response = None
        self.assertEqual(resp, expected_response)

    @testdata.GetMovieValidResponse.decorate(status=503)
    def test_503_get_movie_by_title(self):
        title = testdata.GetMovieValidResponse.title
        year = testdata.GetMovieValidResponse.year
        resp = api.get_movie_by_title(title, year)
        expected_response = None
        self.assertEqual(resp, expected_response)

    @testdata.GetMovieValidResponse.decorate(status=500)
    def test_500_get_movie_by_title(self):
        title = testdata.GetMovieValidResponse.title
        year = testdata.GetMovieValidResponse.year
        resp = api.get_movie_by_title(title, year)
        expected_response = None
        self.assertEqual(resp, expected_response)
