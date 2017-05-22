import io
import json
import twitter

CONSUMER_KEY = 'J13MHa67p9NthjiIC6qqaFAf5'
CONSUMER_SECRET = 'EvWGQPRsILvqkUZ9Vtua2CsPGoNuqKxBGWIvfIeYbBkxeQLdbJ'
OAUTH_TOKEN = '267913941-Ao06Y0QZ8YSb2Pj2bPgQXivhoHbvQ48G211JgQVz'
OAUTH_TOKEN_SECRET = 'depMgzGtSt6MwAZ1t6kcDr1dO57SaWkUdJL8nw4IdLlVf'

# The keyword query

QUERY = 'Kushner'

# The file to write output as newline-delimited JSON documents
OUT_FILE = QUERY + ".json"


# Authenticate to Twitter with OAuth

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

# Create a connection to the Streaming API

twitter_stream = twitter.TwitterStream(auth=auth)


print 'Filtering the public timeline for "{0}"'.format(QUERY)

# See https://dev.twitter.com/docs/streaming-apis on keyword parameters

stream = twitter_stream.statuses.filter(track=QUERY)

# Write one tweet per line as a JSON document.

with io.open(OUT_FILE, 'a+', encoding='utf-8', buffering=1) as f:
    for tweet in stream:
        f.write(unicode(u'{0}\n'.format(json.dumps(tweet, ensure_ascii=False))))
        print tweet['text']