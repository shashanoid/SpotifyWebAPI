from flask import Flask, jsonify, make_response, abort
import auth
import spotipy
import random

class Handler:
    app = Flask(__name__)
    token = auth.get_token()
    sp = spotipy.Spotify(auth=token)

    ## Album IDS
    album_ids = []

    ## Song IDs
    track_ids = []

    ## Song URLs
    song_urls = []

    end_data = []

    def __init__(self):
        return None

    def callback(self):
        return "Callback page for spotify"

    def get_new_release_album_ids(self):
        new_releases = self.sp.new_releases('US', 20, 0)
        try:
            albumbs = new_releases["albums"]["items"]
            for album in albumbs:
                album_id = album["uri"].split(":")[2]
                self.album_ids.append(album_id)
        except:
            print "Error fetching albums"

        return make_response(jsonify(new_releases))

    def get_trackids(self):
        for album_id in self.album_ids:
            song_list = self.sp.album_tracks(album_id, 5, 0)
            try:
                songs = song_list["items"]
                for song in songs:
                    song_id = song["id"]
                    self.track_ids.append(song_id)
            except:
                print "Nice"


        return "Fetching"


    def get_tracks(self):
        random.shuffle(self.track_ids)
        all_tracks = self.sp.tracks(self.track_ids)
        tracks = all_tracks["tracks"]

        for track in tracks:
            preview_url = track["preview_url"]
            artist_name = track["artists"][0]['name']
            cover_image = track["album"]["images"][0]["url"]

            if preview_url is not None:
                data = {'artist': artist_name, 'preview_url': preview_url,\
                        'cover_image':cover_image}
                self.end_data.append(data)

        return make_response(jsonify(self.end_data))



if __name__ == '__main__':
    handler = Handler()
    handler.app.add_url_rule('/callback', 'callback', handler.callback)

    #New releases
    handler.app.add_url_rule('/new', 'newReleases', \
                            handler.get_new_release_album_ids, methods=['GET'])
    handler.app.add_url_rule('/list', 'songList',\
                            handler.get_trackids, methods=['GET'])

    #Getting tracks
    handler.app.add_url_rule('/tracks', 'tracks', handler.get_tracks, methods=["GET"])
    handler.app.run(debug=True, port=8000)

