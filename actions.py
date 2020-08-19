# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests

class ActionWeather(Action):
    def name(self):
        return 'action_weather'
        
    def run(self, dispatcher, tracker, domain):
        #weatherstack api key
        api_key = 'baec0948c69bdfe824247df8b2f8632f'
        print(api_key)
        loc = tracker.get_slot('location')
        print(loc)
        api_address='http://api.weatherstack.com/current?access_key={}&query={}'.format(api_key,loc) #for json data     
        current = requests.get(api_address).json()
        print(current)
        country = current['location']['country']
        city = current['location']['name']
        #condition = current['current']['condition']['text']
        temperature_c = current['current']['temperature']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_speed']

        response = """The temperature in {} is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(city, temperature_c, humidity, wind_mph)
                        
        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]