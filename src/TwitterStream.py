import io
import json
import twitter



class TwitterStream(object):

    def __init__(self):
        CONSUMER_KEY = 'J13MHa67p9NthjiIC6qqaFAf5'
        CONSUMER_SECRET = 'EvWGQPRsILvqkUZ9Vtua2CsPGoNuqKxBGWIvfIeYbBkxeQLdbJ'
        OAUTH_TOKEN = '267913941-Ao06Y0QZ8YSb2Pj2bPgQXivhoHbvQ48G211JgQVz'
        OAUTH_TOKEN_SECRET = 'depMgzGtSt6MwAZ1t6kcDr1dO57SaWkUdJL8nw4IdLlVf'
        self.auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

        self.twitter_stream = twitter.TwitterStream(auth=self.auth)

    def get_stream(self, query):

        OUT_FILE = query + ".json"
        print 'Filtering the public timeline for "{0}"'.format(query)
        stream = self.twitter_stream.statuses.filter(track=query)

        print "Writing the stream"
        count=0
        with io.open(OUT_FILE, 'w+', encoding='utf-8', buffering=1) as f:
            for tweet in stream:
                f.write(unicode(u'{0}\n'.format(json.dumps(tweet, ensure_ascii=False))))
                count+=1
                print count
