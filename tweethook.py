from flask import Flask
import tweepy

app = Flask(__name__)

@app.route('/') # this is the home page route
def hello_world(): # this is the home page function that generates the page code
    return "Hello world!"
    
@app.route('/webhook', methods=['POST'])
def webhook():
  api_key = "AFDiO9imXrwS7qyhS2of5xIb9"
  api_secret = "XM0FdP3gwBfDYrrkDujs32MyngvG9VDubRfvQdcPfOEVpQNIgZ"

  access_token = '1511764402218758144-x4AgkFfT64dvVPZNU2FJwGCvAPmnEI'
  access_token_secret = '4UPiwcKrneXwk6VOb2U8cSN8OcDoxxRGwbRx3P1L92bnr'
  
  auth = tweepy.OAuthHandler(api_key, api_secret)
  auth.set_access_token(access_token, access_token_secret)
  
  api = tweepy.API(auth)
  
  public_tweets = api.home_timeline()
  
  return {
        "fulfillmentText": public_tweets[0].text,
        "source": "webhookdata"
    }
    
   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080) # This line is required to run Flask on repl.it