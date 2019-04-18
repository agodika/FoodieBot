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
		price_range = tracker.get_slot('price')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,'mexican':73,'south indian':85,'north indian':50,'american':1,'italian':55}

		results_df = pd.DataFrame(columns=['Restaurant_Name','Address','Avg_budget','Rating'])
		results =zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),100,"rating","desc")
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:results_df = results_df.append({'Restaurant_Name':restaurant['restaurant']['name'],'Address': restaurant['restaurant']['location']['address'],'Avg_budget':restaurant['restaurant']['average_cost_for_two'],'Rating':restaurant['restaurant']['user_rating']['aggregate_rating']},ignore_index=True)
				#response=response+ "Restaurant Name: "+ restaurant['restaurant']['name']+ " Address: "+ restaurant['restaurant']['location']['address']+" Average budget for two people: "+restaurant['restaurant']['average_cost_for_two']+" Zomato user rating: "+ restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"	
		if(price_range=="1"):
		    price_results = results_df[results_df['Avg_budget'] <=300]
		    if(len(price_results)==0):
		        response=response+" Sorry couldn't find any restaurants in price range. Please re enter different price range "
		    else:
		        for index, row in price_results.head(5).iterrows():
		            response = response+row['Restaurant_Name']+" in "+ row['Address']+" has been rated "+str(row['Rating'])+"\n"
		elif(price_range=="2"):
		    price_results = results_df[(results_df['Avg_budget'] >300) & (results_df['Avg_budget'] < 700)]
		    if(len(price_results)==0):
		        response=response+" Sorry couldn't find any restaurants in price range. Please re enter different price range "
		    else:
		        for index, row in price_results.head(5).iterrows():
		            response = response+row['Restaurant_Name']+" in "+ row['Address']+" has been rated "+str(row['Rating'])+"\n"          #" Price per 2 person "+str(row['Avg_budget'])+
		elif(price_range=="3"):
		    price_results = results_df[(results_df['Avg_budget'] >=700)]
		    if(len(price_results)==0):
		        response=response+" Sorry couldn't find any restaurants in price range. Please re enter different price range "
		    else:
		        for index, row in price_results.head(5).iterrows():
		            response = response+row['Restaurant_Name']+" in "+ row['Address']+" has been rated "+str(row['Rating'])+"\n"
		dispatcher.utter_message("---------------------------------------")
		dispatcher.utter_message(response)
		dispatcher.utter_message("---------------------------------------")
		return [SlotSet('location',loc)]
	
class ActionValidateLocation(Action):
	def name(self):
		return 'validate_location'
		
	def run(self, dispatcher, tracker, domain):
		city_list = ['ahmedabad', 'bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai', 'pune',
					'agra', 'ajmer', 'aligarh', 'allahabad', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'belgaum', 
					'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bokaro steel city', 'chandigarh', 'coimbatore', 
					 'cuttack', 'dehradun', 'dhanbad', 'durg-bhilai nagar', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 
					 'gorakhpur', 'gulbarga', 'guntur', 'gurgaon', 'guwahati', 'gwalior', 'hubli-dharwad', 'indore', 'jabalpur', 'jaipur', 
					 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kannur', 'kanpur', 'kakinada', 'kochi', 'kottayam', 
					 'kolhapur', 'kollam', 'kota', 'kozhikode', 'kurnool', 'lucknow', 'ludhiana', 'madurai', 'malappuram', 'mathura', 'goa', 
					 'mangalore', 'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'palakkad', 'patna', 
					 'pondicherry', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'siliguri', 'solapur', 
					 'srinagar', 'sultanpur', 'surat', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirunelveli', 'tiruppur', 
					 'ujjain', 'vijayapura', 'vadodara', 'varanasi', 'vasai-virar city', 'vijayawada', 'visakhapatnam', 'warangal']
		loc = tracker.get_slot('location')
		response = ""
		if(loc == None):
			dispatcher.utter_template("utter_invalid_location")
			return [SlotSet('location',None)]
		elif(loc.lower() not in city_list):
			dispatcher.utter_template("utter_invalid_location")
			return [SlotSet('location',None)]
		else:
			return [SlotSet('location',loc)]

class ActionSendEmail(Action):
	##
	## Refered the youtube video for sending email with python
	## link: https://www.youtube.com/watch?v=GHrTSKtfzx8
	def name(self):
		return 'action_email'
		
	def run(self, dispatcher, tracker, domain):
		price_range = tracker.get_slot('price')
		email = tracker.get_slot('email')
		if(email==None):
			dispatcher.utter_message("email id not found")
			return[SlotSet('email',None)]
			
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
		
		results_df = pd.DataFrame(columns=['Restaurant_Name','Address','Avg_budget','Rating'])
		results =zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 100,"rating","desc")
		d = json.loads(results)
		response=""
		#list_email = re.findall('([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)',email)
		#Email
		msg = MIMEMultipart()
		msg['From']="foodbot0@gmail.com"
		msg['To']="foodbot0@gmail.com"
		msg['Subject']="Your Zomato restaurants recommendation are here."

		if d['results_found'] == 0:
			response= "no restaurants found!!"
		else:
			for restaurant in d['restaurants']:results_df = results_df.append({'Restaurant_Name':restaurant['restaurant']['name'],'Address': restaurant['restaurant']['location']['address'],'Avg_budget':restaurant['restaurant']['average_cost_for_two'],'Rating':restaurant['restaurant']['user_rating']['aggregate_rating']},ignore_index=True)
		        #response=response+ "Restaurant Name: "+ restaurant['restaurant']['name']+ "\nAddress: "+ restaurant['restaurant']['location']['address']+"\nAverage budget for two people: "+str(restaurant['restaurant']['average_cost_for_two'])+"\nZomato user rating: "+ str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\n\n"
		if(price_range=="1"):
		    price_results = results_df[results_df['Avg_budget'] <=300]
		    if(len(price_results)==0):
		        response=response+" Sorry couldn't find any restaurants in price range. Please re enter different price range "
		        msg.attach(MIMEText(response,'html'))
		    else:
		        msg.attach(MIMEText("Hello User,<br><br><b>Top 10 restaurants for your search,</b> <br><br>",'html'))
		        for index, row in price_results.head(10).iterrows():
		            response = row['Restaurant_Name']+" in "+ row['Address']+" has been rated "+str(row['Rating'])+"\n"
		            msg.attach(MIMEText('<br>'+response+'<br>','html'))
		        msg.attach(MIMEText('<br><br>Bon Appetit!!','html'))
		elif(price_range=="2"):
		    price_results = results_df[(results_df['Avg_budget'] >300) & (results_df['Avg_budget'] < 700)]
		    if(len(price_results)==0):
		        response=response+" Sorry couldn't find any restaurants in price range. Please re enter different price range "
		        msg.attach(MIMEText(response,'html'))
		    else:
		        msg.attach(MIMEText("Hello User,<br><br><b>Top 10 restaurants for your search,</b> <br><br>",'html'))
		        for index, row in price_results.head(10).iterrows():
		            response = row['Restaurant_Name']+" in "+ row['Address']+" has been rated "+str(row['Rating'])+"\n"
		            msg.attach(MIMEText('<br>'+response+'<br>','html'))
		        msg.attach(MIMEText('<br><br>Bon Appetit!!','html'))

		elif(price_range=="3"):
		    price_results = results_df[(results_df['Avg_budget'] >=700)]
		    if(len(price_results)==0):
		        response=response+" Sorry couldn't find any restaurants in price range. Please re enter different price range "
		        msg.attach(MIMEText(response,'html'))
		    else:
		        msg.attach(MIMEText("Hello User,<br><br><b>Top 10 restaurants for your search,</b> <br><br>",'html'))
		        for index, row in price_results.head(10).iterrows():
		            response = row['Restaurant_Name']+" in "+ row['Address']+" has been rated "+str(row['Rating'])+"\n"
		            msg.attach(MIMEText('<br>'+response+'<br>','html'))
		        msg.attach(MIMEText('<br><br>Bon Appetit !!','html'))

		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(msg['From'],"bot12345")
		server.sendmail(msg['From'],msg['To'],msg.as_string())
		server.quit()
		
		dispatcher.utter_template("utter_email_sent_successfully")
		return[SlotSet('email',email)]
