import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'

def get_token():
    token = util.prompt_for_user_token(<Username>, scope)
    return token