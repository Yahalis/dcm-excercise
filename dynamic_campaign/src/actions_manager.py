"""
This module will load the plugins for the dynamic campaign excercise.
The configuration is based on the factories library that will load all plugins that inherit from the DCMPlugin base class
Action is identified by the plugin 'name' property
"""
import factories
from dynamic_campaign import logger

class DCMPlugin(object):
    """
    Plugin class that all plugins need to inherit.
    """
    name='DCMPlugin'
    def execute(self, context:dict)->None:
        return ''

class ActionsManager:
    def __init__(self, pluginsRoot:str='./plugins'):
        """
        Initialize the plugin factory.
        Assumptions for this implementations:
        1. plugins are stateless & re-entrant
           i.e. plugIns can be called by multiple threads concurently.
        2. initialization is lazy
        """
        # holds one instance of each plugin class.
        self.plugins=dict()
        self.factory = factories.Factory(
            abstract=DCMPlugin,
            plugin_identifier='name',
        )
        self.add_plugins_root(pluginsRoot)

    def add_plugins_root(self, pluginsRoot:str):
        # default configuration,
        self.factory.add_path(
            pluginsRoot
        )

    def execute(self, action:str, context:dict) -> None:
        """
        execute the action - pass the context to the plugin execute function.
        :param action: action (plugin) identifier
        :param context: the context under which to execute the plugin.
        :return:
        """
        assert action in self.factory.identifiers(), 'Action {} does not exist'.format(action)
        try:
            # instantiate the plugin class on first call to relevant action
            if action not in self.plugins:
                pluginClass=self.factory.request(action)
                self.plugins[action]=pluginClass()
            self.plugins[action].exceute(context)
        except Exception as e:
            logger.exception('Error occured while activating plugin {action} with context {context}'.format(action=action, context=context))

        return
