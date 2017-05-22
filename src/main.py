from TwitterStream import TwitterStream

#Driver code for the project

print "Main"
twitter = TwitterStream()
twitter.get_stream("Trump")