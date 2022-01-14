import yaml
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yaml
from pprint import pprint
from tqdm.notebook import tqdm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import credential

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=credential.my_id,
    client_secret=credential.my_secret),
    language='ja')

weekly_top_playlist_ids_dict = dict(
    Global='37i9dQZEVXbNG2KDcFcKOF',  # グローバル
    Japan='37i9dQZEVXbKqiTGXuCOsB',  # 日本
    Korea='37i9dQZEVXbJZGli0rRP3r',  # 韓国
    America='37i9dQZEVXbLp5XoPON0wI',  # アメリカ
    Italy='37i9dQZEVXbJUPkgaWZcWG',  # イタリア
    India='37i9dQZEVXbMWDif5SCBJq',  # インド
    Brazil='37i9dQZEVXbKzoK95AbRy9',  # ブラジル
)


def get_playlist_tracks(playlist_ids: dict, playlist_len: int):

    tracks_df = pd.DataFrame(np.zeros((playlist_len*len(playlist_ids.keys()), 5)),
                             columns=['country', 'weekly_rank', 'artist', 'title', 'uri'])
    for i, country in enumerate(tqdm(playlist_ids.keys())):
        playlist = sp.playlist(playlist_id=playlist_ids[country], market='JP')
        print(playlist['description'])
        tracks = playlist['tracks']['items']
        for j, track in enumerate(tracks):
            idx = (i*50) + j
            track_info = track['track']
            tracks_df.loc[idx, 'country'] = country
            tracks_df.loc[idx, 'weekly_rank'] = int(j+1)
            tracks_df.loc[idx, 'artist'] = track_info['artists'][0]['name']
            tracks_df.loc[idx, 'title'] = track_info['name']
            tracks_df.loc[idx, 'uri'] = track_info['uri']
    return tracks_df


tracks_df = get_playlist_tracks(
    playlist_ids=weekly_top_playlist_ids_dict, playlist_len=50)

print(tracks_df)
