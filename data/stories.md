## Generated Story 255706069223404498
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## Generated Story 1993277579540566202
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_restaurant
    - utter_goodbye

## Generated Story 3320800183399695936
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
* goodbye
    - utter_goodbye

## Generated Story -4639179087166749998
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"location": "delhi"}
    - export


## Generated Story 4963448062290237512
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
* affirm
    - utter_goodbye
    - export

## Generated Story 8888421047649199601
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_restaurant
    - slot{"location": "bangalore"}
* affirm
    - utter_goodbye
    - export
## Generated Story 4082258749009225174
* greet
    - utter_greet
* restaurant_search{"price": "3", "cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"price": "3"}
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "aks.rohankar@gmail.com"}
    - slot{"email": "aks.rohankar@gmail.com"}
* restaurant_search
* affirm
    - utter_goodbye
    - export

## Generated Story -2507502301654723261
* greet
    - utter_greet
* restaurant_search{"price": "3", "cuisine": "italian", "location": "hyderabad"}
    - slot{"cuisine": "italian"}
    - slot{"location": "hyderabad"}
    - slot{"price": "3"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "aks.rohankar@gmail.com"}
    - slot{"email": "aks.rohankar@gmail.com"}
    - action_email
    - utter_email_sent_successfully
* affirm
    - utter_goodbye
    - export
## Generated Story -970599645220879304
* greet
    - utter_greet
* restaurant_search{"price": "3", "cuisine": "italian", "location": "hyderabad"}
    - slot{"cuisine": "italian"}
    - slot{"location": "hyderabad"}
    - slot{"price": "3"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "aks.rohankar@gmail.com"}
    - slot{"email": "aks.rohankar@gmail.com"}
    - action_email
    - export

## Generated Story 2755367151704612936
* 
    - utter_greet
* 
    - utter_greet
* 
    - utter_greet
* 
    - utter_greet
* 
    - utter_ask_location
* 
    - validate_location
    - slot{"location": null}
* 
    - utter_ask_location
* 
    - validate_location
    - slot{"location": null}
* send_email{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - validate_location
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "foodbot0@gmail.com"}
    - slot{"email": "foodbot0@gmail.com"}
    - action_email
    - utter_email_sent_successfully
* affirm
    - utter_goodbye
    - export

## Generated Story -9179753622307467029
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - validate_location
    - slot{"location": "agra"}
    - utter_ask_cuisine
* restaurant_search
    - export

