import sys
import twitter

consumerKey = str(sys.argv[1])
consumerSecretKey = str(sys.argv[2])
accessKey = str(sys.argv[3])
accessSecretKey = str(sys.argv[4])

twitterApiClient = twitter.Api(consumer_key=consumerKey, consumer_secret=consumerSecretKey, access_token_key=accessKey, access_token_secret=accessSecretKey)
results = twitterApiClient.GetSearch("q=twitter%20&result_type=recent&since=2018-01-21&count=100")
print(results)