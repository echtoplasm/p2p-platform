# p2p-platform

## django messaging platform

After switching from te p2p-messaging repo to this one I decided to start from scratch and take a more modular approach.
In changing my approach I decided it would be best to start with the messaging application itself and move to the more
social aspects at a later time (profile, pfp's, and the like). 

## Future Plans 

The hopes for this project is to be able to turn the chat function into a potential chat bot for improved patient/provider
relations in the field of healthcare. Furthermore the ultimate goal for this project is to be able to make a NLP, ML algorithm 
that can take input from a provider and output the relevant documentation in regards to the patient interaction.

## Potential Real-World Applications
I still havent fully realized the exact capacity that this type of application could be applied to. 
I have a semblance of the potential applications but they are still very nuanaced with the main focus just being on the messaging and documentation 
capabilities rather than the interpolation of the two at a later date.

I am still undecided if the NLP HIPPA compliant documenting application should be entirely separate from the messenging application.

## Files of note

docker-compose.yml
chat/consumers.py
chat/routing.py
messenger/settings.py 
requirements.txt

## Projects Current State

The current state of the project is in its infancy, with only te messaging application be built so far. 

The next update will come in the form of refining the messaging functionality, and storing the messages in the postgres db.

## Replication 

I have intentionally set this project up to be replicatable, mainly for myself. 
Anyone with intentions to replicate should refer to the requirements.txt file

