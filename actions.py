from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
# import zomatopy
import json

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		# config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
		# zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		# location_detail=zomato.get_location(loc, 1)
		# d1 = json.loads(location_detail)
		# lat=d1["location_suggestions"][0]["latitude"]
		# lon=d1["location_suggestions"][0]["longitude"]
		# cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		# results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		# d = json.loads(results)
		response="this is a test response"
		# if d['results_found'] == 0:
			# response= "no results"
		# else:
			# for restaurant in d['restaurants']:
				# response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

class SendEmail(Action):
	def name(self):
		return 'action_email'
		
	def run(self, dispatcher, tracker, domain):
		# config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
		# zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		email = tracker.get_slot('email')
		# location_detail=zomato.get_location(loc, 1)
		# d1 = json.loads(location_detail)
		# lat=d1["location_suggestions"][0]["latitude"]
		# lon=d1["location_suggestions"][0]["longitude"]
		# cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		# results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		# d = json.loads(results)
		response="this is a test response"
		# if d['results_found'] == 0:
			# response= "no results"
		# else:
			# for restaurant in d['restaurants']:
				# response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('email',email)]

class ValidateLocation(Action):
	def name(self):
		return 'action_validate_location'
		
	def run(self, dispatcher, tracker, domain):
		# config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
		# zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')

		valid_locs = ["Bangalore",
          "Chennai",
          "Delhi",
          "Hyderabad",
          "Kolkata",
          "Mumbai",
          "Agra",
          "Ajmer",
          "Aligarh",
          "Amravati",
          "Amritsar",
          "Asansol",
          "Aurangabad",
          "Ahmedabad",
          "Bareilly",
          "Belgaum",
          "Bhavnagar",
          "Bhiwandi",
          "Bhopal",
          "Bhubaneswar",
          "Bikaner",
          "Bokaro Steel City",
          "Chandigarh",
          "Coimbatore",
          "nagpur",
          "Cuttack",
          "Dehradun",
          "Dhanbad",
          "Durg-Bhilai Nagar",
          "Durgapur",
          "Erode",
          "Faridabad",
          "Firozabad",
          "Ghaziabad",
          "Gorakhpur",
          "Gulbarga",
          "Guntur",
          "Gurgaon",
          "Guwahati",
          "Gwalior",
          "Hubli-Dharwad",
          "Indore",
          "Jabalpur",
          "Jaipur",
          "Jalandhar",
          "Jammu",
          "Jamnagar",
          "Jamshedpur",
          "Jhansi",
          "Jodhpur",
          "Kannur",
          "Kanpur",
          "Kakinada",
          "Kochi",
          "Kottayam",
          "Kolhapur",
          "Kollam",
          "Kota",
          "Kozhikode",
          "Kurnool",
          "Lucknow",
          "Ludhiana",
          "Madurai",
          "Malappuram",
          "Mathura",
          "Goa",
          "Mangalore",
          "Meerut",
          "Moradabad",
          "Mysore",
          "Nanded",
          "Nashik",
          "Nellore",
          "Noida",
          "Palakkad",
          "Patna",
          "Pondicherry",
          "Prayagraj",
          "PuneRaipur",
          "Rajkot",
          "Rajahmundry",
          "Ranchi",
          "Rourkela",
          "Salem",
          "Sangli",
          "Siliguri",
          "Solapur",
          "Srinagar",
          "Sultanpur",
          "Surat",
          "Thiruvananthapuram",
          "Thrissur",
          "Tiruchirappalli",
          "Tirunelveli",
          "Tiruppur",
          "Tiruvannamalai",
          "Ujjain",
          "Bijapur",
          "Vadodara",
          "Varanasi",
          "Vasai-Virar City",
          "Vijayawada",
          "Visakhapatnam",
          "Vellore",
          "Warangal"]

		valid_locs = [name.casefold() for name in valid_locs]

		if loc.casefold() in valid_locs: 
			return [SlotSet('valid_location', True)]
		else:
			return [SlotSet('location', None), SlotSet('valid_location', False)]

