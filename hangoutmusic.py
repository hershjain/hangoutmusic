import sys
import os
import spotipy
import spotipy.util as util

username = 'tdj2fiuw0x44mkd5zo5p31bbn'


def sp_auth():
    sp_clientID = '4a93618e0d40470f83a765af142c2f84'
    sp_client_secret = '53e487a74e754e1f95c63a4ec4026fc2'
    sp_redirect_uri = 'http://localhost/'

    scope = 'user-library-read'

    token = util.prompt_for_user_token(username, scope, sp_clientID, sp_client_secret, sp_redirect_uri)
    return token

def get_artist_name(art_uri):
    artist = sp.artist(art_uri)
    print(artist['name'])

def get_top_artist_name(num,time_frame):

    # num means the number of artists (max = 20)
    # time_frame means the time frame of top artists (short_term, medium_term, long_term)

    top_artists = sp.current_user_top_artists(num, 0, time_frame)
    for artists in top_artists['items']:
        print(artists['name'])


if __name__ == "__main__":
    t = sp_auth()
    if t:
        sp = spotipy.Spotify(auth=t)
        sp.trace = True
        tracks = sp.current_user_top_tracks(10, 0, 'short_term')
        for x in tracks['items']:
            print(x['name'] + ' : ' + str(x['popularity']))


    else:
        print("Can't get token for", username)