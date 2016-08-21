import indicoio
import operator

indicoio.config.api_key = '0be0c4a7f985a316fcade08931b747d4'

'''''''''''''''''''''
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs


#Twitter API Things
REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = 'NLp5m34YodDJemlmVsQ0H07Df'
CONSUMER_SECRET = '2IsklKGmJmcs8ewwT11vxTOCa96GTqVMB7JfHIzjxVtZWf1Kqk'

OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

def setup_oauth():
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)

    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]

    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key

    verifier = raw_input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret

def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print "OAUTH_TOKEN: " + token
        print "OAUTH_TOKEN_SECRET: " + secret
        print
    else:
        oauth = get_oauth()
        show_url = "https://api.twitter.com/1.1/statuses/show.json?id="
        tweet_id = '767071509567250433' #get from PHP URL
        tweet_url = show_url + tweet_url
        print tweet_url
        r = requests.get(tweet_url, auth=oauth)
        print r.json()
'''''''''''''''''''''

#Retrieve Image from Social Media (Twitter Implemented for Demo)
#see above code - may move to PHP

#Key Value Pairs of Indico Tags and Associated Task ID
#Note: this is not ideal and for proof of concept only

#Task Variables (for easy reading)
DoYouHaveTheBalls = 1
SoakUpTheSun = 2
SuitUp = 3
MusicMadness = 4
BeatTheHeat = 5
NoPainNoGain = 6
OnTheWater = 7
TeamSpirit = 8
FreeWheelin = 9
RunningInStyle = 10
EatHealthyBeHealthy = 11
CampOut = 12
PopPop = 13

tag2task = {'puck, hockey puck':DoYouHaveTheBalls,
            'golf ball':DoYouHaveTheBalls,
            'tennis ball':DoYouHaveTheBalls,
            'basketball':DoYouHaveTheBalls,
            'ball player, baseball player':DoYouHaveTheBalls,
            'rugby ball':DoYouHaveTheBalls,
            'ping-pong ball':DoYouHaveTheBalls,
            'soccer ball':DoYouHaveTheBalls,
            'sunglasses, dark glasses, shades':SoakUpTheSun,
            'sunglass':SoakUpTheSun,
            'suit, suit of clothes':SuitUp,
            'electric guitar':MusicMadness,
            'drum, membranophone, tympan':MusicMadness,
            'sax, saxophone':MusicMadness,
            'grand piano, grand':MusicMadness,
            'banjo':MusicMadness,
            'trombone':MusicMadness,
            'cello, violoncello':MusicMadness,
            'violin, fiddle':MusicMadness,
            'swimming trunks, bathing trunks':BeatTheHeat,
            'bathing cap, swimming cap':BeatTheHeat,
            'bikini, two-piece':BeatTheHeat,
            'barbell':NoPainNoGain,
            'paddle, boat paddle':OnTheWater,
            'canoe':OnTheWater,
            'speedboat':OnTheWater,
            'jersey, T-shirt, tee shirt':TeamSpirit,
            'tricycle, trike, velocipede':FreeWheelin,
            'bicycle-built-for-two, tandem bicycle, tandem':FreeWheelin,
            'mountain bike, all-terrain bike, off-roader':FreeWheelin,
            'unicycle, monocycle':FreeWheelin,
            'running shoe':RunningInStyle,
            'cucumber, cuke':EatHealthyBeHealthy,
            'pineapple, ananas':EatHealthyBeHealthy,
            'Granny Smith':EatHealthyBeHealthy,
            'pomegranate':EatHealthyBeHealthy,
            'broccoli':EatHealthyBeHealthy,
            'sleeping bag':CampOut,
            'mountain tent':CampOut,
            'pop bottle, soda bottle':PopPop
            }

#Function to Perform Image Recognition and Match Image to Task
def processImages(imageUrl, selectedTask):
    result = indicoio.image_recognition(imageUrl)
    
    #print result
    
    topTag = max(result.iteritems(), key=operator.itemgetter(1))[0]
    print topTag
    
    try:
        taskID = tag2task[topTag]
        print taskID
        if taskID == selectedTask:
            return True
        else:
            return False
    except KeyError, e:
        print 'Photo is not of a task'
        return False



url = 'https://pbs.twimg.com/media/CqXt7XdVIAEQVZ5.jpg'
print processImages(url,1)

