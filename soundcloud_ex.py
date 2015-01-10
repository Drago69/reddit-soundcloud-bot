# client 13a223ddeda36f5e79f37680ae26e4ab

import soundcloud

client = soundcloud.Client(client_id='13a223ddeda36f5e79f37680ae26e4ab')

tracks = client.get('/tracks', q="Saturday Sessions", limit=3)

for track in tracks:
	print track.permalink_url