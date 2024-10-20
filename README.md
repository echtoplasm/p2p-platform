# p2p platform // chatbot

## Change of Focus for the Project
The main purpose of this project is to build a fullstack template for replicable web applications and web pages for reselling the layout/template to businesses. The implication is that the customer would implement Chatbot and AI functions into their website.

## Chatbot Specs
The frontend chat function was made using WebSocket, JavaScript, Daphne channels, and Twisted. I didn't include the static files, which contain the JavaScript and CSS needed for rendering the chat function in a user-friendly way. The chatbot has been built upon OpenAI's 3.5 ChatGPT Turbo using an API key.

## Backend
The backend for this web application is based on a PostgreSQL database using Docker, with the only consumer model being the chat consumer.

## Future Plans
Plans moving forward with this application include storing the messages themselves in the database and training the chatbot on a specific set of data.
