"""
Testing the EventsHandler class.
"""
import os
import pandas as pd

from dynamic_campaign import EventsHandler
def test_events_handler():
    """
    reading the events from the google-sheet and handling in a loop.
    :return:
    """
    eh = EventsHandler()
    eventsDF=pd.read_csv('https://docs.google.com/spreadsheets/d/1gKBEgk9HPkg-ZXrHzQtXHubBNW9g_0JdAYQVhoBpxvQ/export?format=csv&gid=1009633338').fillna('')
    for i,row in eventsDF.iterrows():
        event=dict(row)
        eh.handle_event(event)
        print('=========================================================================================================================================================================================================')

if __name__ == '__main__':
    os.environ['TEMPLATES_ROOT']='{}/templates/'.format(os.getcwd())
    test_events_handler()
