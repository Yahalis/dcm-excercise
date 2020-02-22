"""
LinekdIn message plugin
"""
from dynamic_campaign import TemplatManager
from dynamic_campaign import DCMPlugin

class LinkedinMessagePlugin(DCMPlugin):
    name='linkedin_message'
    def __init__(self):
        self.tm = TemplatManager()

    def exceute(self, context: dict) -> None:
        print('Inside linkedin-message handling')
        message=self.tm.realize_template(context['parameters']['template'], context)
        recipient=context['prospect']['email']
        print('Sending LinkedIn message to {} message:\n{}'.format(recipient, message))
