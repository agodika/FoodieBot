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

## Generated Story -2052395247833445293
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "warangal"}
    - slot{"location": "warangal"}
    - validate_location
    - slot{"location": "warangal"}
    - utter_ask_cuisine
* restaurant_search{"price": "chinese"}
    - slot{"price": "chinese"}
    - export

## Generated Story 212623072021473962
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - validate_location
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"price": "chinese"}
    - slot{"price": "chinese"}
    - export

## Generated Story 576374693006196103
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - validate_location
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"price": "chinese"}
    - slot{"price": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_send_email
* send_email{"email": "foodbot0@gmail.com"}
    - slot{"email": "foodbot0@gmail.com"}
    - action_email
    - slot{"email": "foodbot0@gmail.com"}
    - export

## Generated Story -2858744304069268934
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* send_email
    - validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - validate_location
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_price
* restaurant_search
    - export
## Generated Story -4195742875257063722
* greet
    - utter_greet
* restaurant_search{"price": "1", "cuisine": "american", "location": "mumbai"}
    - slot{"cuisine": "american"}
    - slot{"location": "mumbai"}
    - slot{"price": "1"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - action_reset_slots
    - reset_slots
    - utter_ask_location
* restaurant_search
    - export
## Generated Story 7316962749142192251
* greet
    - utter_greet
* restaurant_search{"price": "1", "cuisine": "american", "location": "mumbai"}
    - slot{"cuisine": "american"}
    - slot{"location": "mumbai"}
    - slot{"price": "1"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_no_result
    - action_reset_slots
    - reset_slots
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "foodbot0@gmail.com"}
    - slot{"email": "foodbot0@gmail.com"}
    - action_email
    - slot{"email": "foodbot0@gmail.com"}
    - export

## Generated Story 3485837068574057436
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - validate_location
    - slot{"location": "goa"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_restaurant
    - slot{"location": "goa"}
    - utter_ask_send_email
* send_email{"email": "foodbot0@gmail.com"}
    - slot{"email": "foodbot0@gmail.com"}
    - action_email
    - slot{"email": "foodbot0@gmail.com"}
* affirm
    - export

## Generated Story -1321633268197888150
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - utter_ask_price
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_restaurant
    - slot{"location": "goa"}
    - utter_ask_send_email
* deny
    - utter_affirm
    - utter_search_again
* deny
    - utter_affirm
    - export

## Generated Story 1328047474375117198
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "goa"}
    - slot{"cuisine": "american"}
    - slot{"location": "goa"}
    - utter_ask_price
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_restaurant
    - slot{"location": "goa"}
    - utter_ask_send_email
* deny
    - utter_affirm
    - utter_search_again
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - utter_ask_location
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_restaurant
    - slot{"location": "goa"}
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "foodbot0@gmail.com"}
    - slot{"email": "foodbot0@gmail.com"}
    - action_email
    - slot{"email": "foodbot0@gmail.com"}
* affirm
    - utter_search_again
* deny
    - utter_affirm
    - export

