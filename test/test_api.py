import requests

def test_authorization(api_token):
    headers = {
        'Authorization': f'OAuth {api_token}',
    }
    response = requests.get('https://api.music.yandex.net/account/status', headers=headers)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    print("Authorization test passed")

api_token = 'your_api_token'
test_authorization(api_token)

def test_search_track(api_token, track_name):
    headers = {
        'Authorization': f'OAuth {api_token}',
    }
    params = {
        'text': track_name,
        'type': 'track',
    }
    response = requests.get('https://api.music.yandex.net/search', headers=headers, params=params)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    search_results = response.json()
    assert 'tracks' in search_results['result'], "No tracks found in search results"
    print("Search track test passed")

test_search_track(api_token, 'Imagine Dragons')

def test_create_and_edit_playlist(api_token):
    headers = {
        'Authorization': f'OAuth {api_token}',
    }
    
    # Create playlist
    create_data = {
        'title': 'Test Playlist',
    }
    create_response = requests.post('https://api.music.yandex.net/users/{user_id}/playlists/create', headers=headers, json=create_data)
    assert create_response.status_code == 200, f"Expected status code 200, but got {create_response.status_code}"
    playlist_id = create_response.json()['result']['playlist']['kind']
    
    # Add track to playlist
    add_track_data = {
        'kind': playlist_id,
        'trackIds': ['12345678'],  # Example track ID
    }
    add_response = requests.post(f'https://api.music.yandex.net/users/{user_id}/playlists/{playlist_id}/change-relative', headers=headers, json=add_track_data)
    assert add_response.status_code == 200, f"Expected status code 200, but got {add_response.status_code}"
    
    print("Create and edit playlist test passed")

test_create_and_edit_playlist(api_token)

def test_offline_tracks(api_token):
    headers = {
        'Authorization': f'OAuth {api_token}',
    }
    response = requests.get('https://api.music.yandex.net/account/offlineTracks', headers=headers)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    offline_tracks = response.json()
    assert 'result' in offline_tracks, "No offline tracks found"
    print("Offline tracks test passed")

test_offline_tracks(api_token)

def test_radio_stations(api_token):
    headers = {
        'Authorization': f'OAuth {api_token}',
    }
    response = requests.get('https://api.music.yandex.net/rotor/stations/list', headers=headers)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    stations = response.json()
    assert 'result' in stations, "No radio stations found"

    # Play a specific radio station (example station id)
    station_id = stations['result'][0]['id']
    play_response = requests.get(f'https://api.music.yandex.net/rotor/station/{station_id}/tracks', headers=headers)
    assert play_response.status_code == 200, f"Expected status code 200, but got {play_response.status_code}"
    
    print("Radio stations test passed")

test_radio_stations(api_token)