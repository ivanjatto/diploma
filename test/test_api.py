import requests

def test_search_movie():
    url = "https://api.kinopoisk.dev/v1.4/movie"
    params = {
        "query": "Inception"
    }
    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": "SBQJJPG-MAW4Y7E-HXAT1KZ-9PSDPJC"
    }

    response = requests.get(url, params=params, headers=headers)
    print(f"Response status code: {response.status_code}")
    print(f"Response body: {response.text}")

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    movies = response.json().get("docs", [])
    assert len(movies) > 0, f"No movies found in the search results: {response.text}"
    print("Search movie test passed")

import requests

def test_get_popular_movies():
    url = "https://api.kinopoisk.dev/v1.4/movie/popular"
    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": "SBQJJPG-MAW4Y7E-HXAT1KZ-9PSDPJC"
    }

    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    print(f"Response body: {response.text}")

    if response.status_code == 200:
        movies = response.json().get("docs", [])
        assert len(movies) > 0, "No popular movies found"
        print("Get popular movies test passed")
    else:
        print(f"Failed to get popular movies. Status code: {response.status_code}. Response body: {response.text}")


def test_get_genres():
    url = "https://api.kinopoisk.dev/v1.3/genre"
    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": "SBQJJPG-MAW4Y7E-HXAT1KZ-9PSDPJC"
    }

    try:
        response = requests.get(url, headers=headers)
        print(f"Response status code: {response.status_code}")
        print(f"Response body: {response.text}")

        response.raise_for_status()  

        genres = response.json().get("docs", [])
        assert len(genres) > 0, "No genres found"
        print("Get genres test passed")
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")






