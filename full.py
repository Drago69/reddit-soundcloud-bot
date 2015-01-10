import time

import praw

import soundcloud

r = praw.Reddit('Soundcloud Link Bot Version 1'
                'https://github.com/aethos/reddit-soundcloud-bot.git')
r.login('SCBOTDEMO', 'sardines')
already_done = set()
to_be_done = set()

client = soundcloud.Client(client_id='13a223ddeda36f5e79f37680ae26e4ab')

activateStr = "!SCLB"
defaultLimit = 5


while True:
    subreddit = r.get_subreddit('test')
    for submission in subreddit.get_new(limit=10):
        flat_comments = praw.helpers.flatten_tree(submission.comments)
        # has_link = any(string in op_text for string in prawWords)
        for comment in flat_comments:
            if activateStr in comment.body and comment.id not in already_done:
                tracks = client.get('/tracks', q="Saturday Sessions", limit=defaultLimit)
                comment.reply(tracks)
                already_done.add(comment.id)
            time.sleep(600001)