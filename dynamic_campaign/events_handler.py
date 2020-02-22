"""
Event handler module.
"""
from dynamic_campaign import ContextBuilder
from dynamic_campaign import ActionsManager
from dynamic_campaign import logger

class EventsHandler:
    def __init__(self):
        self.cb = ContextBuilder()
        self.am = ActionsManager()

    def handle_event(self, event):
        """
        this is the main event-handling function of the system.
        it will:
        - report the event to DB/Audit
        - Get the event context
        - Check the rules for relevant actions
        - Activate the relevant plugin for the function
        :param event: the event to handle.
        :return:
        """
        # reporting the handling of the event. in real system this will write to events-db
        logger.debug('Handling event: ', event)

        # get the context:
        context = self.cb.get_context(event)
        logger.debug('Context:', context)

        # handling the event:
        # Check the rules:
        for rule in context['rules']:
            try:
                isRule = eval(rule['condition'])
            except Exception as e:
                isRule=False

            if isRule:
                context['parameters'] = eval(rule['parameters'])
                self.am.execute(rule['action'], context)
