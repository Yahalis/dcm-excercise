# dcm-excercise
Dynamic campaign management exercise

## Overview
- Simplified state machine to handle events coming from a campaign system
- Acting upon the events based on rules and activating pluggable actions.
- Sending messages based on Template and event context - event data, campaign, prospect and rules
- Mock data is located in a google spreadsheet [here](https://docs.google.com/spreadsheets/d/1gKBEgk9HPkg-ZXrHzQtXHubBNW9g_0JdAYQVhoBpxvQ/edit#gid=1639723702)

## How to run and test
- Clone the project to a local directory
- open in an IDE
- Set the dcm-excercise as source-root
- run test_events_handler.py (this is the main test and will process the events on the google sheet)

## Some implementation comments
- Templates are processed by the Jija2 package
- Pluging dynamic loading is performed using a simple factory based on importlib. all actions are dynamic plugins. They basically print what they were suppose to do (e.g. send_mail, linkedin message etc.)
- The context builder is basically mocking context based on the event and data from the sheet. it does show the concept of how the real builder will work in the system.


