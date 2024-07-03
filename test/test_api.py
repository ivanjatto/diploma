import requests

def test_authorization(api_token):
    headers = {
        'Authorization': f'Bearer {api_token}',
    }
    response = requests.get('https://api.kinopoisk.dev/v1.3/account/status', headers=headers)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    print("Authorization test passed")

api_token = 'SBQJJPG-MAW4Y7E-HXAT1KZ-9PSDPJC'
test_authorization(api_token)

def test_search_movie(api_token, movie_title):
    headers = {
        'Authorization': f'Bearer {api_token}',
    }
    params = {
        'query': movie_title,
    }
    response = requests.get('https://api.kinopoisk.dev/v1.3/movie/search', headers=headers, params=params)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    search_results = response.json()
    assert 'docs' in search_results, "No movies found in search results"
    print("Search movie test passed")

test_search_movie(api_token, 'Inception')

def test_get_popular_movies(api_token):
    headers = {
        'Authorization': f'Bearer {api_token}',
    }
    response = requests.get('https://api.kinopoisk.dev/v1.3/movie/popular', headers=headers)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    popular_movies = response.json()
    assert 'docs' in popular_movies, "No popular movies found in response"
    print("Get popular movies test passed")

test_get_popular_movies(api_token)
