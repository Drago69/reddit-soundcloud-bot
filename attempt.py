import time

import praw

r = praw.Reddit('Soundcloud Link Bot Version 1'
                'https://github.com/aethos/reddit-soundcloud-bot.git')
r.login('SCBOTDEMO', 'sardines')
already_done = set()

activateStr = "!SCLINKBOT"

while True:
    subreddit = r.get_subreddit('test')
    for submission in subreddit.get_new(limit=10):
        flat_comments = praw.helpers.flatten_tree(submission.comments)
        # has_link = any(string in op_text for string in prawWords)
        for comment in flat_comments:
            if comment.body == "Hello" and comment.id not in already_done:
                comment.reply(' world!')
                already_done.add(comment.id)
    time.sleep(1800)

# while True:
# subreddit = r.get_subreddit('test')
# for submission in subreddit.get_new(limit=10):
#     op_text = submission.selftext.lower()
#     has_praw = any(string in op_text for string in prawWords)
#     # Test if it contains a PRAW-related question
#     if submission.id not in already_done and has_praw:
#         msg = '[PRAW related thread](%s)' % submission.short_link
#         r.send_message('_Daimon_', 'PRAW Thread', msg)
#         already_done.append(submission.id)
# time.sleep(1800)