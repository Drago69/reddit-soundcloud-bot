import time
import praw
import soundcloud
import auth

r = praw.Reddit('Soundcloud Link Bot Version 1'
                'https://github.com/aethos/reddit-soundcloud-bot.git')
r.login(username, password)
already_done = set()

client = soundcloud.Client(client_id='13a223ddeda36f5e79f37680ae26e4ab')

activateStr = "SCLB!"
defaultLimit = 5


def getInfo(trackList):
   # ex. [Artist - Title](url)
    if not trackList: #checks if list is empty
        return ""
    res = "---------------\n\n"
    for track in trackList:
        res+= "[" + track.user['username'] + " - **" + track.title + "**](" + track.permalink_url + ")"
        res+= "\n\n---------------\n\n"
    return res

def composeComment(trackInfos, is_formatted, has_results):
    text = ""
    # print trackInfos
    # print "fmt?: " + str(is_formatted)
    # print "valid?: " + str(has_results)
    if not is_formatted:
        # text = "not formatted"
        text = "Looks like that wasn't formatted right. "
        text += "Remember to put your search terms in quotes!"
    elif is_formatted and not has_results:
        # text = "no results"
        text = "Sorry, looks like I couldn't find anything!"
    elif is_formatted and has_results:
        # text = "results"
        text = trackInfos
    text += "\n\n[What is this?](info_url)" + "\t[Feedback?](http://www.reddit.com/message/compose/?to=TopHatz)"
    return text

while True:
    subreddit = r.get_subreddit('SCLB_Test')
    for submission in subreddit.get_new(limit=1):
        flat_comments = praw.helpers.flatten_tree(submission.comments)
        for comment in flat_comments:
            text = comment.body
            trackInfos = ""
            has_results = False
            is_formatted = True
            is_search = False
            while activateStr in text and comment.id not in already_done:
                # print "started loop"
                text = text[text.find(activateStr):]
                try:
                    is_search = True
                    first = text.index("\"") + 1
                    second = text.index("\"", first, len(text))
                    query = text[first:second]
                    if query != "":
                        tracks = client.get('/tracks', q=query, limit=defaultLimit)
                        trackInfos+= getInfo(tracks)
                        # print "text: " + text
                        # print "query: " + query
                        # print trackInfos
                        # print "splice attempt: " + text[second:]

                    text = text[second:]
                    is_formatted = True
                    if trackInfos != "":
                        has_results = True
                    # break
                except ValueError:
                    is_formatted = False
                    text = ""
                # print "completed loop"
            if is_search:
                comment.reply(composeComment(trackInfos, is_formatted, has_results))
                print "made comment"
            already_done.add(comment.id)
        # time.sleep(600001)


