## Generated Story -7414492826169334219
* greet
    - utter_greet
* search_restaurant{"cuisine": "mexican", "location": "delhi"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"valid_location": true}
    - utter_ask_budget
* search_restaurant{"budget": "<300"}
    - slot{"budget": "<300"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_query_ask_email
* deny
    - utter_goodbye
    - export

## Generated Story -5090770963368655501
* greet
    - utter_greet
* search_restaurant{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* search_restaurant{"location": "Bhopal"}
    - slot{"location": "Bhopal"}
    - action_validate_location
    - slot{"valid_location": true}
    - utter_ask_budget
* search_restaurant{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_restaurant
    - slot{"location": "Bhopal"}
    - utter_query_ask_email
* affirm
    - utter_ask_email
* send_details{"email": "abc@def.com"}
    - slot{"email": "abc@def.com"}
    - action_email
    - slot{"email": "abc@def.com"}
    - utter_done
    - utter_goodbye
    - export

## Generated Story 6053031762975423584
* greet
    - utter_greet
* search_restaurant{"location": "mysore"}
    - slot{"location": "mysore"}
    - action_validate_location
    - slot{"valid_location": true}
    - utter_ask_budget
* search_restaurant{"budget": "300"}
    - slot{"budget": "300"}
    - utter_ask_cuisine
* search_restaurant
    - utter_ask_cuisine
* search_restaurant
    - utter_ask_cuisine
* search_restaurant{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"search_results": "(I will search restaurant in this action)"}
    - utter_query_ask_email
* deny
    - utter_goodbye
    - export


## Generated Story 6182493262278462731
* greet
    - utter_greet
* search_restaurant
    - utter_ask_location
* search_restaurant{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* search_restaurant{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* search_restaurant{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"search_results": "(I will search restaurant in this action)"}
    - utter_query_ask_email
* affirm
    - utter_ask_email
* send_details{"email": "foo@bar.co.in"}
    - slot{"email": "foo@bar.co.in"}
    - action_email
    - slot{"email_sent": true}
    - utter_done
    - utter_goodbye
    - export

## Generated Story -4298251492318283722
* greet
    - utter_greet
* search_restaurant{"budget": "<300", "cuisine": "italian", "location": "bangalore"}
    - slot{"budget": "<300"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"valid_location": true}
    - action_restaurant
    - slot{"search_results": "(I will search restaurant in this action)"}
    - utter_query_ask_email
* deny
    - utter_goodbye
    - export


######### These stories need to be corrected

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

## Generated Story -4406550421169986531
* greet
    - utter_greet
* search_restaurant
    - utter_ask_location
* specify_location
    - utter_ask_cuisine
* specify_cuisine
    - utter_ask_budget
* specify_budget{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_restaurant
    - slot{"location": null}
    - utter_ask_email
* specify_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_email
    - slot{"email": "ahbcdj@dkj.com"}
    - utter_goodbye
    - export	