import sys
import twitter
import jsonpickle

#format command line input
consumerKey = str(sys.argv[1])
consumerSecretKey = str(sys.argv[2])
accessKey = str(sys.argv[3])
accessSecretKey = str(sys.argv[4])
queryString = str(sys.argv[5])
city = str(sys.argv[6])
miles = str(sys.argv[7])
outputFilePath = str(sys.argv[8])

#execute Twitter search via RESTful API
twitterApiClient = twitter.Api(consumer_key=consumerKey, consumer_secret=consumerSecretKey, access_token_key=accessKey, access_token_secret=accessSecretKey)
#TODO: tinker with query format in advanced search URL
formattedQuery = "q={0}".format(queryString, city, miles)
tweets = twitterApiClient.GetSearch(formattedQuery)

#write tweets to file
jsonString = ""
outputFile = open(outputFilePath, "w")
for tweet in tweets:
    jsonString += str(jsonpickle.encode(tweet))
outputFile.write(jsonString)
outputFile.close()

#analyze tweets
#TODO: execute command for b4msa