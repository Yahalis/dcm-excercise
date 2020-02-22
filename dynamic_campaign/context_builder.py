"""
Mockup package for context building.
It does showcase how the building might take place as it relies on pre-defined "tables" in google-spreadsheet
see: https://docs.google.com/spreadsheets/d/1gKBEgk9HPkg-ZXrHzQtXHubBNW9g_0JdAYQVhoBpxvQ/edit#gid=1639723702
"""
import pandas as pd
import random

from dynamic_campaign import logger

class ContextBuilder:
    def __init__(self):
        """
        reading sample rules and prospects from a google sheet.
        """
        self.rulesDF = pd.read_csv(
            'https://docs.google.com/spreadsheets/d/1gKBEgk9HPkg-ZXrHzQtXHubBNW9g_0JdAYQVhoBpxvQ/export?format=csv&gid=1639723702')
        self.prospectsDF = pd.read_csv(
            'https://docs.google.com/spreadsheets/d/1gKBEgk9HPkg-ZXrHzQtXHubBNW9g_0JdAYQVhoBpxvQ/export?format=csv&gid=0')

    def get_context(self, event:dict)->dict:
        """
        based on the event data - creating a relevant context with prospect and rules related to the event.
        :param event:
        :return:
        """
        context=dict()
        if event['data']:
            event['data']=eval(event['data'])
        context['event']=event
        #
        # Rules query - similar to what would happen if the rules were in a DB table.
        query='account=="{account}" and campaign_id=={campaign_id} and step_id in [0, {step_id}]'.format(**event)
        rulesDF=self.rulesDF.query(query)
        context['rules']=list()
        for i,rule in rulesDF.iterrows():
            context['rules'].append(dict(rule))
        # getting the relevant prospect for this campaign.
        prospectsDF=self.prospectsDF.query('prospect_id=={prospect_id}'.format(**event))
        if prospectsDF.shape[0]>0:
            context['prospect']=dict(prospectsDF.iloc[0])
            context['prospect']['data']=eval(context['prospect']['data'])
            context['prospect']['actions']=dict()
            if context['event']['event_type']=='open':
                context['prospect']['actions']['open']=random.randint(2,5)
        else: # basically should not happen in a real system, will cause errors in handling the event...
            logger.error ("Prospect id {} does not exist".format(event['prospect_id']))

        # Filling up the below fields to avoid crush in the template realization.
        # in the real system these will be calculated correctly.
        context["general"]=dict()
        context["general"]["next_business_day"]='Monday'
        context["campaign"]=dict()
        context["campaign"]["manager_first_name"]='Johnny'
        return context

if __name__ == '__main__':
    pd.set_option('display.max_columns', 25)
    pd.set_option('display.max_rows', 2500)
    pd.set_option('display.width', 2000)
    cb=ContextBuilder()
    print(cb.rulesDF)