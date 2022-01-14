import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import credential

artist_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

my_id = credential.my_id
my_secret = credential.my_secret
ccm = SpotifyClientCredentials(client_id=my_id, client_secret=my_secret)
spotify = spotipy.Spotify(
    client_credentials_manager=ccm)
results = spotify.artist_top_tracks(artist_uri)

# print(results)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
