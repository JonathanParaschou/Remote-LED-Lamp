# Remote-LED-Lamp
Based off the '"Friendship Lamp" concept, this is my own take on a similar device

The net file is used to interface with the backend adafruit server setup to store state changes in the lights. Each light color is correlated to a different integer. This also does automactic data polling after a set amount of time

The button file changes the light's colors and signals for the light to make a state change on the adafruit servers. 

Incoming and Outcoming text files keep track of the current states in the server from local access.

The state file keeps track of the light's current state.
