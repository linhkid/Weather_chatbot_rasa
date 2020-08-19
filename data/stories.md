## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## Ask Name
* greet
  - utter_greet
* my_name_is
  - utter_hello_name


## Ask Weather 1
* greet
  - utter_greet
* my_name_is
  - utter_hello_name
* inform{"location": "Singapore"}
    - slot{"location": "Singapore"}
    - action_weather
    - slot{"location": "Singapore"}
* goodbye
    - utter_goodbye
    - export

## Generated Story -3351152636827275381
* greet
    - utter_greet
* inform{"location": "London"}
    - slot{"location": "London"}
    - action_weather
* goodbye
    - utter_goodbye
    - export

## Ask weather 2
* greet
   - utter_greet
* inform
   - utter_ask_location
* inform{"location":"Lithuania"}
   - slot{"location": "Lithuania"}
   - action_weather
* goodbye
   - utter_goodbye
   - export

## Ask Weather 3
* greet
  - utter_greet
* inform{"location": "Singapore"}
    - slot{"location": "Singapore"}
    - action_weather
    - slot{"location": "Singapore"}
* my_name_is
  - utter_hello_name
* goodbye
    - utter_goodbye
    - export
