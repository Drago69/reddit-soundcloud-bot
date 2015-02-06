# client 13a223ddeda36f5e79f37680ae26e4ab

import soundcloud

client = soundcloud.Client(client_id='13a223ddeda36f5e79f37680ae26e4ab')

tracks = client.get('/tracks', q="Saturday Sessions", limit=3)


def getInfo(trackList):
   # ex. [Artist - Title](url)
    res = ""
    for track in trackList:
		res+= "[" + track.user['username'] + " - **" + track.title + "**](" + track.permalink_url + ")\n\n"
    return res

print getInfo(tracks)