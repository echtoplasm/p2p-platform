# p2p platform // chatbot 

## Change of focus for the project

The main purpose of this project is to build a fullstack template for replicatable web applications and web pages for the purpose 
of reselling the layout/template to business with their specifications for a website to be built to the template standards, with the implication being that 
the customer would implment Chatbot and AI functions into their website.

## Chatbot Specs 

Frontend chat function was made using websocket, jscript, daphne channels, and twisted.

I didnt include the staticfiles which includes the jscript and css needed for rendering the chat
function in a user friendly way.

The chatbot has been built upon openAI's 3.5 chatGPT turbo using a API key.

## Backend 

The backend for this web application has been based on a postgresql database using docker, with the only consumer model being the chatconsumer.

## Future Plans
The plans moving forward with this application would be to include the messages themselves in the database,
and to train the chatbot on a specifc set of data. 

 
 
