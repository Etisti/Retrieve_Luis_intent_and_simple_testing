import requests
import json
class retrieve_luis_intent(object):
    ''' 
    Class that retrieves the intent from luis engine

    Arguments:
        - appId : The App ID GUID found on the www.luis.ai Application Settings page.
        - prediction_key : YOUR-PREDICTION-KEY: Your LUIS prediction key, 32 character value.
        - prediction_endpoint : endpoint url of the api Luis engine
        - utterance : 'I want two large pepperoni pizzas on thin crust please'

    optimise:
        -  Should also retrieve Prediction score
        - add Batch testing
        - testing endpoint for different versions of your luis engine (not want the utterance logged, use the logging=false in the query string configuration.)
        - check the api doc for more stuffs like asynchronous call etc => https://westus.dev.cognitive.microsoft.com/docs/services/5890b47c39e2bb17b84a55ff/operations/5890b47c39e2bb052c5b9c2f
    ''' 
    def __init__(self,appId,prediction_key,prediction_endpoint,utterance):
        self.= appId # 0b357e74-7e04-4ee5-b2e0-b49bb9b06e59 YOUR-APP-ID
        self.= prediction_key # a7c9d220241d4fcb9051bad4e27a989e 
        self.= prediction_endpoint # https://etienneluis.cognitiveservices.azure.com/
        self.= utterance # 'I want two large pepperoni pizzas on thin crust please'
    
    def get_intent(self):

        try:

        # The URL parameters to use in this rest api call.
        params ={
            'query': utterance,
            'timezoneOffset': '0',
            'verbose': 'true',
            'show-all-intents': 'true',
            'spellCheck': 'false',
            'staging': 'false',
            'subscription-key': prediction_key
        }

        # Make the rest api call.
        response = requests.get(f'{prediction_endpoint}luis/prediction/v3.0/apps/{appId}/slots/production/predict', headers=headers, params=params)
        
        # Export the response json file
        with open('pizza_intent_response.json', 'w') as f:
            json.dump(response, f, indent=4)

        except Exception as e:
            # Display the error string.
            print(f'{e}')


