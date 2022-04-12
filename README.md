
[![Social banner for Chatbot agent](https://github.com/COSC310-Team-23/assignment2/blob/main/assets/banner.png)](https://github.com/COSC310-Team-23/assignment2.git)

# **COSC 310 - Assignment 3** <img src="https://media3.giphy.com/media/S60CrN9iMxFlyp7uM8/giphy.gif?cid=ecf05e4704yigthbkvnneq2y40zp98jkeohqhlc8vuqhhpgk&rid=giphy.gif&ct=g" width="45px">

## 🔗 Link to our Github

<https://github.com/COSC310-Team-23/assignment2.git>

This is the Assignment 3 for Group 23 in COSC 310. The assignment's purpose is to create a simple chat agent. Our agent is a restaurant server that simulates ordering food at a restaurant.

## 📗 Our Chatbot is organized into Intents and Entities
 
Intents are descriptors that allow the chatbot to determine how to respond to your prompt. Intents are made up of a few sample phrases that a user might say to the chatbot, and a response delegated for those sample phrases. Ex: if you wanted to pay the bill at a restaurant you might say, “Can I have the bill”, “Check please”, or “We’re ready to leave”. A human might interpret all those things as the same but the chatbot needs to be taught to recognize that all of these phrases result in requiring the bill. Intents are the pointers that tell the chatbot where to carry the conversation based on inputs coming from the user.

Entities are lists or categories of miscellaneous objects or categories that the chatbot might need to understand. These are also written into the chatbot so it can understand the specifics of what you might be asking for. The chatbot needs this data written into it because it might possibly have to refer back to it later. Ex: We may have a list of entities, called $drinks. In this list may be some options like water, soda, wine etc. When we reference drinks asking what drinks are available to the chatbot, it needs to be able to give us options in that category (parameter type)  and will recite what is written in. Another use case is having the chatbot capable of repeating an entity back to you in conversation. Ex: “What would you like to drink?” “I’ll have water” “Sure, $drinks coming up.” The chatbot here recognizes water as a value in entity @drink and returns the JSON object {“drinks” : “water”}, and in its response we can use the $drinks variable to reference the user's choice. 

## 📕 Features - NEW
***added Twitter API as well as Wikipedia API***
users are now able to search wikipedia by name for any summary on a person. This feature is used by stating something along the line of "show wiki 'person name'"
"read wikipedia 'person name'"
Twitter features include link to a developer twitter account. Upon being granted additional clearance, users can post and review tweets under the developer account name

* New and improved GUI
* Extra topic added
* Voice-to-speech ability
* Detect and handle spelling mistakes, using machine learning from Google DialogFlow
* Extra responses created to help the flow of conversation
* More responses created for extraneous inputs
* Entity matching Toolkit applied
* Synonym matching Toolkit applied
* Second language (French) Toolkit applied
* Connected to Botium Unit Testing via Google Cloud for unit testing conversation

## 📘 GUI

The chatbot GUI resembles a simple ‘Facebook Messenger’ style chat window with full customizability. Built-in to the API is a sleek minimizable chat window with color scheme selection, chatbot profile options and full scalability for any device. Modifying the chatbot to fit in on any website is as easy as tweaking the CSS to your liking.

To use our chatbot without the HTML: You can also view it right on a web browser! Just follow this link: <https://bot.dialogflow.com/15436cfd-7c75-416d-9244-8014e6f10d41>

## 📙 Extra Topic

Our second topic is a coffee shop. Now, users can either order from the restaurant or order from the coffee shop. At the beginning of the Chatbot, we changed the welcome message to indicate that there is now a second topic. Users can also go to the other topic once finishing with one. For example, they can order from the coffee shop and after they finish their order, they can talk to the restaurant.

## 📗 Voice-to-speech

Voice-to-speech allows for the user to talk into the microphone instead of typing. We enabled this ability within Google DialogFlow API.

## 📕 Handling Spelling

We used the Automatic Spell Correction from Google to detect incorrect spelling. The software uses Machine Learning to learn what spelling mistakes are common for our conversation. We train Machine Learning as we test our chatbot and make mistakes. Then, the Spell Correction learns over time what the response should be according to common mistakes.

## 📘 More responses

We added more responses to our ChatBot to handle various tasks. Our chatbot now responds to extraneous inputs with a variety of responses such as “Sorry, I don’t understand, could you repeat that?” and “what do you mean?” There are 12 responses to handle extraneous input. Another type of response that we added was to respond to small talk. The user is able to ask the chatbot questions and input like, “Are you there?” and “You’re so clever.” The chatbot can handle a variety of small talk inputs, around 50.

## 📙 Toolkits

The Google entity matching/listing toolkit allows us to create entities that make it easier for us to match responses and outputs. For example, if a user inputs ‘Hummus plate’ into our Chatbot when responding to a question, the starters entity type would be matched and the chatbot is not able to extract this value as the JSON value {“starter”: “Hummus plate”}, which we can use as an output. The Google synonym match toolkit allows for us to match inputs with other similar inputs. For example, if the user inputs S when asked what size drink they want, the chatbot will know that S means size small. There is also ‘fuzzy matching’ enabled, which allows for the chatbot to approximately match each word in case the user misspells a word. The French Language toolkit allows for us to accommodate users who speak French, which is the other official language of Canada. We are able to toggle between languages currently in our API environment.

## 📗 Unit Testing
     
We used Botium Box for our automated unit testing. We attached our chatbot to a Google Cloud server and created a service account in Google Cloud to connect our chatbot to Botium Box via a JSON connection file. This was important because as we update our chatbot, it will update in real time in Botium and we can test the new conversation or edits that we make for more efficient automated testing. Then, we created three test cases for our chatbot to test the different flows of conversation, or regression testing. The tests are created within the Botium Box engine, written using BotiumScript, the language used for writing test cases in Botium.

Aside from regression testing we also performed NLP Unit testing, Natural Language Processing Unit testing. NLP testing uses the Botium AI to go through every possible conversation flow and to test the efficiency of the conversation flow. For this testing, we did not have to do any extra coding, we just needed to connect our bot to the Botium testing interface. This was helpful in finding any conversation flows that got distracted. After testing, we were able to look at each conversation flow in an interactive environment, allowing us to view the possible conversations in a diagram format.

The results from the test are in the form of graphs, XML, and CSV. Information such as the time for each test to run and the success of each test we performed was recorded.
https://www.botium.ai 
https://github.com/codeforequity-at/botium-core.git

## 📕 Features that could be extracted with others as API

* The use of entities to easily and accurately detect user inputs for reuse
* The use of a Second Language Toolkit to adapt to French speaking users
* The use of Botium Unit Testing to test conversations
* Voice-to-speech ability
* Use of Machine Learning for spelling from Google DialogFlow

## 📘 DFDs

* **Level 0 DFD**

![](https://github.com/COSC310-Team-23/assignment2/blob/main/assets/DFD_Level_0.jpg)

This diagram explains the data flow between the 0 level components of our bot. The data received from the user is delivered to the Chatbot server, and
the responses are received from the database, further the server provides the responses to the user.

* **Level 1 DFD**

![](https://github.com/COSC310-Team-23/assignment2/blob/main/assets/DFD_Level_1.jpg)

This diagram explains the data flow between the Level 1 components of our bot.
The chatbot is event driven, in that as the user inputs data, the chatbot will constantly access the 
database and respond to each input with an action through the API service we used, Google Dialogflow.
The bot will know which action to use based on matching the input to a response each time. 

## 📗 Limitations of our ChatBot

* The chatbot is only able to support single text inputs. The chatbot cannot handle more complex input like images, hyperlinks, or several sequential text inputs.

* There are still some inputs that the chatbot could get confused by, for example inputting the same thing over and over again could make the bot lose its place in the conversation.
