from yandex_music import Client
import requests
import os

def sanitize_filename(filename):
    forbidden_chars = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
    for char in forbidden_chars:
        filename = filename.replace(char, '_')
    return filename

def download_like(token, path):
    client = Client(token).init()
    
    number = 0
    while True:
        track = client.users_likes_tracks()[number].fetch_track()
        title = track.title
        sanitized_title = sanitize_filename(title)
        download_path = f'{path}\\{sanitized_title}.mp3'
        track.download(download_path)
        number += 1

def album_download(token, id, path):
    client = Client(token).init()
    album = client.albums_with_tracks(id)
    tracks = []

    for i, volume in enumerate(album.volumes):
        if len(album.volumes) > 1:
            tracks.append(f'Диск {i + 1}')
        tracks += volume

    for track in tracks:
        if isinstance(track, str):
            continue

        track_id = track['id']
        download_info = client.tracks_download_info(track_id, get_direct_links=True)

        if not download_info:
            print(f'Не удалось получить информацию о скачивании для трека {track_id}')
            continue

        download_url = download_info[0].direct_link

        response = requests.get(download_url)
        
        if response.status_code == 200:
            sanitized_title = sanitize_filename(track["title"])
            download_path = os.path.join(path, f'{sanitized_title}.mp3')
            try:
                with open(download_path, 'wb') as file:
                    file.write(response.content)
                print(f'Трек {track["title"]} скачан')
            except Exception as e:
                print(f'Ошибка при скачивании трека {track["title"]}: {e}')
                continue
        else:
            print(f'Не удалось скачать трек {track["title"]}')

def song_download():
    from yandex_music import Client
import requests
import os

def sanitize_filename(filename):
    forbidden_chars = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
    for char in forbidden_chars:
        filename = filename.replace(char, '_')
    return filename

def download_like(token, path):
    client = Client(token).init()
    
    number = 0
    while True:
        track = client.users_likes_tracks()[number].fetch_track()
        title = track.title
        sanitized_title = sanitize_filename(title)
        download_path = f'{path}\\{sanitized_title}.mp3'
        track.download(download_path)
        number += 1

def album_download(token, id, path):
    client = Client(token).init()
    album = client.albums_with_tracks(id)
    tracks = []

    for i, volume in enumerate(album.volumes):
        if len(album.volumes) > 1:
            tracks.append(f'Диск {i + 1}')
        tracks += volume

    for track in tracks:
        if isinstance(track, str):
            continue

        track_id = track['id']
        download_info = client.tracks_download_info(track_id, get_direct_links=True)

        if not download_info:
            print(f'Не удалось получить информацию о скачивании для трека {track_id}')
            continue

        download_url = download_info[0].direct_link

        response = requests.get(download_url)
        
        if response.status_code == 200:
            sanitized_title = sanitize_filename(track["title"])
            download_path = os.path.join(path, f'{sanitized_title}.mp3')
            try:
                with open(download_path, 'wb') as file:
                    file.write(response.content)
                print(f'Трек {track["title"]} скачан')
            except Exception as e:
                print(f'Ошибка при скачивании трека {track["title"]}: {e}')
                continue
        else:
            print(f'Не удалось скачать трек {track["title"]}')

def song_download(token, track_id, path):
    client = Client(token).init()
    track = client.tracks([track_id])[0]
    
    download_info = client.tracks_download_info(track_id, get_direct_links=True)
    
    if not download_info:
        print(f'Не удалось получить информацию о скачивании для трека {track_id}')
        return

    download_url = download_info[0].direct_link

    response = requests.get(download_url)
    
    if response.status_code == 200:
        sanitized_title = sanitize_filename(track.title)
        download_path = os.path.join(path, f'{sanitized_title}.mp3')
        try:
            with open(download_path, 'wb') as file:
                file.write(response.content)
            print(f'Трек {track.title} скачан')
        except Exception as e:
            print(f'Ошибка при скачивании трека {track.title}: {e}')
    else:
        print(f'Не удалось скачать трек {track.title}')

