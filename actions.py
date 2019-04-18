from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f207a84eb81c174a12735f568cffd505"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price_range = tracker.get_slot('price')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,'mexican':73,'south indian':85,'north indian':50,'american':1,'italian':55}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Restaurant Name: "+ restaurant['restaurant']['name']+ " Address: "+ restaurant['restaurant']['location']['address']+" Average budget for two people: "+restaurant['restaurant']['average_cost_for_two']+" Zomato user rating: "+ restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

