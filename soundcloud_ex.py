# client 13a223ddeda36f5e79f37680ae26e4ab

import soundcloud

client = soundcloud.Client(client_id='13a223ddeda36f5e79f37680ae26e4ab')

tracks = client.get('/tracks', q="Saturday Sessions", limit=3)


def getURLS(trackList):
    urls = ""
    for track in trackList:
        urls+= track.permalink_url
    return trackURLS

print getURLS(tracks)