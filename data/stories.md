## Simple stories
## Greet
* greet
    - utter_greet
    - export

## Bye
* goodbye
    - utter_goodbye
    - action_reset_slot
    - export

## No Input
* 
    - utter_default
    - export

## No Input
* 
    - utter_default
* 
    - utter_default
* 
    - utter_default
    - export


## Generated Story 3610933134170833992
* greet
    - utter_greet
* search_restaurant
    - utter_ask_location
* search_restaurant{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* search_restaurant{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* search_restaurant{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"search_results": "has_text"}
    - slot{"found_results": true}
    - utter_query_ask_email
* send_details{"email": "abc@def.com"}
    - slot{"email": "abc@def.com"}
    - action_email
    - utter_goodbye
    - action_reset_slot
    - export

## Generated Story 388558728549701728
* greet
    - utter_greet
* search_restaurant{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_validate_location
    - slot{"location": null}
    - slot{"valid_location": false}
* search_restaurant{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_validate_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* search_restaurant{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* search_restaurant{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"search_results": "text"}
    - slot{"found_results": true}
    - utter_query_ask_email
* deny
    - utter_goodbye
    - action_reset_slot
    - export

## Generated Story 3819246282420587981
* greet
    - utter_greet
* search_restaurant{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* search_restaurant{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* search_restaurant{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_restaurant
    - slot{"search_results": "text"}
    - slot{"found_results": true}
    - utter_query_ask_email
* affirm
    - utter_ask_email
* send_details{"email": "someone@somewhere.com"}
    - slot{"email": "someone@somewhere.com"}
    - action_email
    - slot{"email_sent": true}
    - utter_goodbye
    - action_reset_slot
    - export

## Generated Story 5952315894912500283
* greet
    - utter_greet
* search_restaurant
    - utter_ask_location
* search_restaurant{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_validate_location
    - slot{"location": null}
    - slot{"valid_location": null}
* search_restaurant{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* search_restaurant{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* search_restaurant{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"search_results": "text"}
    - slot{"found_results": true}
    - utter_query_ask_email
* affirm
    - utter_ask_email
* send_details{"email": "email@someserver.com"}
    - slot{"email": "email@someserver.com"}
    - action_email
    - slot{"email_sent": true}
    - utter_goodbye
    - action_reset_slot
    - export

## Generated Story -5001997364761453290
* greet
    - utter_greet
* search_restaurant{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_location
    - slot{"valid_location": true}
    - utter_ask_budget
* search_restaurant{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"search_results": "text"}
    - slot{"found_results": true}
    - utter_query_ask_email
* deny
    - utter_goodbye
    - action_reset_slot
    - export

## Not providing budget
* search_restaurant{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_location
    - slot{"valid_location": true}
    - utter_ask_budget
* 
    - utter_default
* 
    - utter_default
    - export


## Generated Story -4831472538080396003
* greet
    - utter_greet
* 
    - utter_default
* search_restaurant
    - utter_ask_location
* 
    - utter_default
* search_restaurant{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* 
    - utter_default
* search_restaurant{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* 
    - utter_default
* search_restaurant{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_restaurant
    - slot{"search_results": "text"}
    - slot{"found_results": false}
* search_restaurant{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"search_results": "text"}
    - slot{"found_results": true}
    - utter_query_ask_email
* deny
    - utter_goodbye
    - action_reset_slot
    - export

## Generated Story 5286903957715011224
* greet
    - utter_greet
* search_restaurant
    - utter_ask_location
* search_restaurant{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* search_restaurant{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* search_restaurant{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_restaurant
    - slot{"search_results": "text"}
    - slot{"found_results": false}
* deny
    - utter_goodbye
    - action_reset_slot
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"budget": null}
    - slot{"email": null}
    - slot{"valid_location": false}
    - slot{"search_results": null}
    - slot{"found_results": null}
    - slot{"email_sent": null}
    - export