"""
Testing the ActionsManager class
Note that the error-printing is OK, just need to make sure it calls the correct functions.
"""
import os
from dynamic_campaign import ActionsManager

def test_action_manager():
    am = ActionsManager()
    context = {
        'prospect': {
            'first_name': 'Rotem',
            'industry': 'finance',
            'company_name': 'RightBound',
            'data': {
                'number_of_open_positions': 25
            }
        },
        'campaign': {
            'id': 123,

            'manager_first_name': 'Yahali'
        }
    }
    ret = am.execute('email_alert', context)
    ret = am.execute('send_email', context)
    ret = am.execute('linkedin_message', {'to': 'a@b.com'})

if __name__ == '__main__':
    os.environ['TEMPLATES_ROOT']='%s/templates/' % os.path.dirname(__file__)
    test_action_manager()
