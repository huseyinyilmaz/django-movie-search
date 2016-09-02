from movies import testdata

get_movie_valid_response = testdata.GetMovieValidResponse.decorate
get_movie_404_response = testdata.GetMovieValidResponse.decorate(status=404)
get_movie_503_response = testdata.GetMovieValidResponse.decorate(status=503)
