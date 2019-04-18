# sample code to fetch a list of restaurants using zomatopy

import pprint, json
import zomatopy
import pandas as pd

# specify location and cuisine
loc = 'Bangalore'
cuisine = 'Italian'
price_range='3'

# provide API key and initialise a 'zomato app' object
config={ "user_key":"f207a84eb81c174a12735f568cffd505"}
zomato = zomatopy.initialize_app(config)

# get_location gets the lat-long coordinates of 'loc'
location_detail=zomato.get_location(loc, 1)

# store retrieved data as a dict
d1 = json.loads(location_detail)

# separate lat-long coordinates
lat=d1["location_suggestions"][0]["latitude"]
lon=d1["location_suggestions"][0]["longitude"]

# cuisines code (used by zomatopy)
cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}

# fetch and print results
#results =zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5,"rating","desc")
#d = json.loads(results)
#pprint.pprint(d)
results_df = pd.DataFrame(columns=['Restaurant_Name','Address','Avg_budget','Rating'])
results =zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 80,"rating","desc")
d = json.loads(results)
response=""
if d['results_found'] == 0:
	response= "no restaurants found!!"
else:
	for restaurant in d['restaurants']:results_df = results_df.append({'Restaurant_Name':restaurant['restaurant']['name'],'Address': restaurant['restaurant']['location']['address'],'Avg_budget':restaurant['restaurant']['average_cost_for_two'],'Rating':restaurant['restaurant']['user_rating']['aggregate_rating']},ignore_index=True)
        #response=response+ "Restaurant Name: "+ restaurant['restaurant']['name']+ "\nAddress: "+ restaurant['restaurant']['location']['address']+"\nAverage budget for two people: "+str(restaurant['restaurant']['average_cost_for_two'])+"\nZomato user rating: "+ str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\n\n"
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



pprint.pprint(response)