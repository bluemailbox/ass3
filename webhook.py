from flask import Flask, request
import wikipedia
app = Flask(__name__)

@app.route('/') # this is the home page route
def hello_world(): # this is the home page function that generates the page code
    return "Hello world!"
    
@app.route('/webhook', methods=['POST'])
def webhook():
  req = request.get_json(silent=True, force=True)
  fulfillmentText = ''
  sum = 0
  query_result = req.get('queryResult')
  if query_result.get('action') == 'read.wiki':
    topic = str(query_result.get('parameters').get('person'))
    sum = str(wikipedia.summary(topic, sentences = 2))
    fulfillmentText = sum
  return {
        "fulfillmentText": fulfillmentText,
        "source": "webhookdata"
    }
    
   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080) # This line is required to run Flask on repl.it