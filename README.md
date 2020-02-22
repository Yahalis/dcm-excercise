# dcm-excercise
Dynamic campaign management exercise

## Overview
- Simplified state machine to handle events coming from a campaign system
- Acting upon the events based on rules and activating pluggable actions.
- Sending messages based on Template and event context - event data, campaign, prospect and rules
- Mock data is located in a google spreadsheet [here](https://docs.google.com/spreadsheets/d/1gKBEgk9HPkg-ZXrHzQtXHubBNW9g_0JdAYQVhoBpxvQ/edit#gid=1639723702)

## How to run and test
Clone the project to a local directory
### Option 1
- open in an IDE
- Set the dcm-excercise as source-root
- run test_events_handler.py (this is the main test and will process the events on the google sheet)
### Option 2
- run install.sh in the top of the tree
- cd tests
- run: python3 test_events_handler.py

## Some implementation comments
- Templates are processed by the Jija2 package
- Pluging dynamic & lazy loading is performed using the factories package that enables to load relevant plugins from directories and name them after the action the will perform.
- The context builder is basically mocking context based on the event and data from the sheet. it does show the concept of how the real builder will work in the system.
- Selection of Jinja2 and factories were made to meet this excercise requirements, for the real world solution I would make a deeper research, consider several options, validate the open-source status etc.


