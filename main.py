import pylast
import PySimpleGUI as sg
API_KEY = ''#LAST FM API KEY
API_SECRET = ''#LAST FM API SECRET

username = '' #LAST FM USERNAME
password_hash = pylast.md5('') #LAST FM PASSWORD

network = pylast.LastFMNetwork(api_key=API_KEY,api_secret=API_SECRET,username=username,password_hash=password_hash)
user = network.get_user(username)

def playing_now():
    now_playing = user.get_now_playing()
    return now_playing
def song_played_amount():
    songs_played = user.get_playcount()
    return songs_played
def your_name():
    name = user.get_name(properly_capitalized=True)
    return name
def sub():
    sub_check = user.is_subscriber()
    return sub_check
def recent_played():
    recent_track = user.get_recent_tracks(limit=2)
    return(recent_track[0][0])
def top_ablums():
    top_album = user.get_top_albums(limit=2)
    return(top_album[0][0])
def top_tracks():
    top_track = user.get_top_tracks(limit=2)
    return(top_track[0][0])

layout = [
    [sg.Text("Your username is: {} Subscriber: {}".format(your_name(),sub()),key="NAME_SUB")],
    [sg.Text("Playing Now: {}".format(playing_now()),key="PLAYING_NOW")],
    [sg.Text("Recent Played: {}".format(recent_played()),key="RECENT_PLAY")],
    [sg.Text("Top Album: {}".format(top_ablums()),key="TOP_ALBUM")],
    [sg.Text("Top Track: {}".format(top_tracks()),key="TOP_TRACK")],
    [sg.Text("Songs Playcount: {}".format(song_played_amount()),key="PLAYCOUNT")],
    [sg.Button("Refresh"),sg.Button("Close")]
]

window = sg.Window('Music Info', layout)
while True:
    event, value = window.read()
    if event == "Refresh":
        window.Element('NAME_SUB').Update("Your username is: {} Subscriber: {}".format(your_name(),sub()))
        window.Element('RECENT_PLAY').Update("Recent Played: {}".format(recent_played()))
        window.Element('TOP_ALBUM').Update("Top Album: {}".format(top_ablums()))
        window.Element('TOP_TRACK').Update("Top Track: {}".format(top_tracks()))
        window.Element('PLAYING_NOW').Update("Playing Now: {}".format(playing_now()))
        window.Element('PLAYCOUNT').Update("Songs Playcount: {}".format(song_played_amount()))
    elif event == "Close":
        window.close()
        break

