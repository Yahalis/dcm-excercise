"""
Template realization module, based on Jinja2.
"""
import os

from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import UndefinedError, TemplateNotFound

from dynamic_campaign import logger

class TemplatManager:
    def __init__(self):
        """
        Initialize the root-dir and the template filesystem loader.
        """
        rootDir=os.environ['TEMPLATES_ROOT']
        self.__env=Environment(loader=FileSystemLoader(rootDir))

    def realize_template(self, templateFile:str, context:dict) -> str:
        """
        Based on a template filename and context - realize the template and return.
        :param templateFile: template file
        :param context: inputs to the template
        :return:
        """
        try:
            templateFile = self.__env.get_template(templateFile)
            output = templateFile.render(context=context)
        except TemplateNotFound as e:
            logger.error('Template {} not found.'.format(templateFile))
            raise e
        except UndefinedError as e:
            logger.error('Error occured while creating template for context {}'.format(context))
            raise e

        return output
