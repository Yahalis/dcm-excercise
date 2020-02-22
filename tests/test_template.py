"""
Testing the TemplateManager class. should print the templates correctly with context data replacing variables.
"""
import os
from dynamic_campaign import TemplatManager

def test_template():
    tm = TemplatManager()
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
        },
        'general': {
            'next_business_day': 'Monday'
        }
    }
    for template in ['t1.html', 't3.html', 't4.txt', 't51.txt']:
        body = tm.realize_template(template, context)
        print ('Instantiate template {}:\n{}'.format(template, body))
        print("=======================================================================================================================================")

if __name__ == '__main__':
    os.environ['TEMPLATES_ROOT']='{}/templates/'.format(os.getcwd())
    test_template()
