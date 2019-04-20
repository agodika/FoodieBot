from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import pandas as pd
import re
# Import the email modules
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):

		config={ "user_key":"f207a84eb81c174a12735f568cffd505"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price_range = tracker.get_slot('budget')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,'mexican':73,'south indian':85,'north indian':50,'american':1,'italian':55}

		dispatcher.utter_message("---------------------------------------")
		dispatcher.utter_message("Searching for restaurants...")

		results_df = pd.DataFrame(columns=['Restaurant_Name','Address','Avg_budget','Rating'])
		results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 0, 20, "rating", "desc")
		matching_results_found = False

		d = results
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:results_df = results_df.append({'Restaurant_Name':restaurant['restaurant']['name'],'Address': restaurant['restaurant']['location']['address'],'Avg_budget':restaurant['restaurant']['average_cost_for_two'],'Rating':restaurant['restaurant']['user_rating']['aggregate_rating']},ignore_index=True)
				#response=response+ "Restaurant Name: "+ restaurant['restaurant']['name']+ " Address: "+ restaurant['restaurant']['location']['address']+" Average budget for two people: "+restaurant['restaurant']['average_cost_for_two']+" Zomato user rating: "+ restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"	

		if price_range=="<300" or price_range == "300":
			price_results = results_df[results_df['Avg_budget'] <= 300]
			if len(price_results)==0:
				response=response+" Sorry couldn't find any restaurants in price range. Try a different price range?"
			else:
				matching_results_found = True
				for index, row in price_results.head(5).iterrows():
					response = response+row['Restaurant_Name']+" in "+ row['Address']+" has been rated "+str(row['Rating'])+"\n"
		elif(price_range=="300-700"):
			price_results = results_df[(results_df['Avg_budget'] >300) & (results_df['Avg_budget'] < 700)]
			if(len(price_results)==0):
				response=response+" Sorry couldn't find any restaurants in price range. Try a different price range?"
			else:
				matching_results_found = True
				for index, row in price_results.head(5).iterrows():
					response = response+row['Restaurant_Name']+" in "+ row['Address']+" has been rated "+str(row['Rating'])+"\n"		  #" Price per 2 person "+str(row['Avg_budget'])+
		else:
			price_results = results_df[(results_df['Avg_budget'] >=700)]
			if(len(price_results)==0):
				response=response+" Sorry couldn't find any restaurants in price range."
			else:
				matching_results_found = True
				for index, row in price_results.head(5).iterrows():
					response = response+row['Restaurant_Name']+" in "+ row['Address']+" has been rated "+str(row['Rating'])+"\n"

		dispatcher.utter_message(response)
		dispatcher.utter_message("---------------------------------------")

		# cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		return [SlotSet('search_results', results), SlotSet('found_results', matching_results_found)]

class SendEmail(Action):
	def name(self):
		return 'action_email'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		email = tracker.get_slot('email')
		results = tracker.get_slot('search_results')

		msg = MIMEMultipart()
		msg['From']="foodbot0@gmail.com"
		msg['To']="foodbot0@gmail.com"
		msg['Subject']="Your Zomato restaurants recommendation are here."

		# if d['results_found'] == 0:
		# 	response= "no restaurants found!!"
		# else:
		# 	for restaurant in d['restaurants']:results_df = results_df.append({'Restaurant_Name':restaurant['restaurant']['name'],'Address': restaurant['restaurant']['location']['address'],'Avg_budget':restaurant['restaurant']['average_cost_for_two'],'Rating':restaurant['restaurant']['user_rating']['aggregate_rating']},ignore_index=True)
		#		 #response=response+ "Restaurant Name: "+ restaurant['restaurant']['name']+ "\nAddress: "+ restaurant['restaurant']['location']['address']+"\nAverage budget for two people: "+str(restaurant['restaurant']['average_cost_for_two'])+"\nZomato user rating: "+ str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\n\n"
		# if(price_range=="1"):
		#	 price_results = results_df[results_df['Avg_budget'] <=300]
		#	 if(len(price_results)==0):
		#		 response=response+" Sorry couldn't find any restaurants in price range. Please re enter different price range "
		#		 msg.attach(MIMEText(response,'html'))
		#	 else:
		#		 msg.attach(MIMEText("Hello User,<br><br><b>Top 10 restaurants for your search,</b> <br><br>",'html'))
		#		 for index, row in price_results.head(10).iterrows():
		#			 response = row['Restaurant_Name']+" in "+ row['Address']+" has been rated "+str(row['Rating'])+"\n"
		#			 msg.attach(MIMEText('<br>'+response+'<br>','html'))
		#		 msg.attach(MIMEText('<br><br>Bon Appetit!!','html'))
		# elif(price_range=="2"):
		#	 price_results = results_df[(results_df['Avg_budget'] >300) & (results_df['Avg_budget'] < 700)]
		#	 if(len(price_results)==0):
		#		 response=response+" Sorry couldn't find any restaurants in price range. Please re enter different price range "
		#		 msg.attach(MIMEText(response,'html'))
		#	 else:
		#		 msg.attach(MIMEText("Hello User,<br><br><b>Top 10 restaurants for your search,</b> <br><br>",'html'))
		#		 for index, row in price_results.head(10).iterrows():
		#			 response = row['Restaurant_Name']+" in "+ row['Address']+" has been rated "+str(row['Rating'])+"\n"
		#			 msg.attach(MIMEText('<br>'+response+'<br>','html'))
		#		 msg.attach(MIMEText('<br><br>Bon Appetit!!','html'))

		# elif(price_range=="3"):
		#	 price_results = results_df[(results_df['Avg_budget'] >=700)]
		#	 if(len(price_results)==0):
		#		 response=response+" Sorry couldn't find any restaurants in price range. Please re enter different price range "
		#		 msg.attach(MIMEText(response,'html'))
		#	 else:
		#		 msg.attach(MIMEText("Hello User,<br><br><b>Top 10 restaurants for your search,</b> <br><br>",'html'))
		#		 for index, row in price_results.head(10).iterrows():
		#			 response = row['Restaurant_Name']+" in "+ row['Address']+" has been rated "+str(row['Rating'])+"\n"
		#			 msg.attach(MIMEText('<br>'+response+'<br>','html'))
		#		 msg.attach(MIMEText('<br><br>Bon Appetit !!','html'))

		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(msg['From'],"bot12345")
		server.sendmail(msg['From'],msg['To'], results) # msg.as_string())
		server.quit()

		return [SlotSet('email_sent', True)]

class ValidateLocation(Action):
	def name(self):
		return 'action_validate_location'
		
	def run(self, dispatcher, tracker, domain):
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
			"Allahabad",
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
			"Pune", "Raipur",
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
			"Vijayapura",
			"Vijayawada",
			"Visakhapatnam",
			"Vellore",
			"Warangal"]

		valid_locs = [name.casefold() for name in valid_locs]

		if loc.casefold() in valid_locs: 
			return [SlotSet('valid_location', True)]
		else:
			return [SlotSet('location', None), SlotSet('valid_location', False)]

