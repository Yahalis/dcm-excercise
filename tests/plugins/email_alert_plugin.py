"""
Email alert plugin
"""
from dynamic_campaign import TemplatManager
from dynamic_campaign import DCMPlugin

class EmailAlertPlugin(DCMPlugin):
    name='email_alert'
    def __init__(self):
        self.tm = TemplatManager()

    def exceute(self, context: dict) -> None:
        print('Inside email-alert handling')
        message = self.tm.realize_template(context['parameters']['template'], context)
        recipients = context['parameters']['contacts']
        print('Sending to {} e-mail message:\n{}'.format(recipients, message))
