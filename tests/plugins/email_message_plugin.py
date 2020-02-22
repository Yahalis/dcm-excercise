"""
Email alert plugin
"""
from dynamic_campaign import TemplatManager
from dynamic_campaign import DCMPlugin

class EmailMessagePlugin(DCMPlugin):
    name='send_email'
    def __init__(self):
        self.tm= TemplatManager()

    def exceute(self, context: dict) -> None:
        print('Inside email-message handling')
        message=self.tm.realize_template(context['parameters']['template'], context)
        recipient=context['prospect']['email']
        print('Sending to {} e-mail message:\n{}'.format(recipient, message))
