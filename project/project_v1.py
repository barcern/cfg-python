import requests
import json

endpoint = "https://api.thedogapi.com/v1/breeds"
query_params = {
    'api-key' : '42131d49-f92a-441c-8f40-4ade8c01a4ee',
    'attach_breed' : '0'
}

response = requests.get(endpoint, params=query_params)
print(response.status_code)
data = json.loads(response.content)

def user_choose_category():
    """User input to choose a category."""
    user_category = input("Which category would you like to consider? "
                          "breed_group / "
                          "temperament ").lower()
    return user_category

def get_breed_detail(breed):
    """Function to pull data for a specific breed from the API based on
    the breed's name.
    """
    endpoint_breed_detail = "https://api.thedogapi.com/v1/breeds/search"
    query_params_breed_detail = {
        'api-key' : '42131d49-f92a-441c-8f40-4ade8c01a4ee',
        'q' : breed,
    }
    response_breed_detail = requests.get(endpoint_breed_detail, 
                                       params=query_params_breed_detail)    
    data_breed_detail = json.loads(response_breed_detail.content)
    if len(data_breed_detail) == 0:
        data_breed_detail = 'false'
    return data_breed_detail

def check_validity_breed_detail_num(data, key):
    """Check whether a key is present in the dog's dictionary and 
    return an appropriate response.
    This function is intended for weight and height categories only.
    """
    try: 
        val = data[0][key]['metric']
    except KeyError:
        outcome = f"{key.title()} is not available."
    else:
        if key == 'weight':
            outcome = f"{key.title()} is {val} kg."
        else:
            outcome = f"{key.title()} is {val} cm."
    return outcome

def check_validity_breed_detail_string(data, key):
    """Check whether a key is present in the dog's dictionary and 
    return an appropriate response.
    This function is intended for all keys except for weight and height.
    """
    try: 
        val = data[0][key]
    except KeyError:
        outcome = f"{key.title()} is not available."
    else:
        outcome = f"{key.title()} is {val}."
    return outcome

def format_breed_detail(data):
    """Return detailed breed information in a user-friendly format.""" 
    weight = check_validity_breed_detail_num(data, 'weight')
    height = check_validity_breed_detail_num(data, 'height')
    bred = check_validity_breed_detail_string(data, 'bred_for')
    group = check_validity_breed_detail_string(data, 'breed_group')
    life_span = check_validity_breed_detail_string(data, 'life_span')
    temperament = check_validity_breed_detail_string(data, 'temperament')
    message = f"Here are some facts about {data[0]['name']}:"
    message += f"\n\t- {weight} \n\t- {height} \n\t- {bred} \n\t- {group}"
    message += f"\n\t- {life_span} \n\t- {temperament}"
    return message

def list_options(dog_list, user_category):
    """Create a list of available options so that users can choose a 
    characteristic which is available.
    """
    options = []
    for dog in dog_list:
        try: 
            dog[user_category]
        except KeyError:
            pass
        else:
            string = dog[user_category]
            string_split = string.split(", ")
            for item in string_split:
                if item in options:
                    pass
                else:
                    options.append(item)
    options.sort()
    return options

def show_options(dog_list, user_category):
    """Ask the user if they would like to see available options
    and show options if chosen.
    """
    options = list_options(dog_list, user_category)
    user_question = input("Would you like to see all available options? y/n ")
    if user_question == 'y':
        print(options)
    else:
        print("") 
    return options

def user_choose_value():
    """Prompt user to select a charasteric value."""
    user_value = input(f"What {user_category} would you like your "
                               "dog to be? ").title()
    return user_value
    
def check_validity_user_choice(value_list, user_choice):
    """Check whether the user has picked out of the available options."""
    if user_choice in value_list:
        flag_choice = True
    else:
        flag_choice = False
    return flag_choice
    
def check_validity_user_yn(user_choice):
    """Check whether the user has selected yes or no."""
    if user_choice == 'y':
        flag_choice = False
    elif user_choice == 'n':
        flag_choice = False
    else:
        print("Sorry, we do not recognise your input.")
        flag_choice = True
    return flag_choice

def user_choose_yn(question):
    """Prompt user to choose a yes-no option."""
    flag = True
    while flag:
        user_input = input(question)
        flag = check_validity_user_yn(user_input)
    return user_input

# def check_validity_user_yninv(user_choice):
#     """Check whether the user has selected yes or no."""
#     if user_choice == 'y':
#         flag_choice = 'true'
#     elif user_choice == 'n':
#         flag_choice = 'false'
#     else:
#         flag_choice = 'invalid'
#     return flag_choice

def end_search_early(dog_list):
    """Carry out final tasks when user chooses to end search early."""
    if len(dog_list) == 0:
        print("We are sorry to say that we haven't found your perfect "
              "match. Keep searching, your perfect dog is out there!")
    else:
        print("We haven't found your perfect match yet, but we believe that "
              "the following breeds would suit you well:")
        for dog in dog_list:
            print("- " + dog['name'])

current_data = data
flag = True
categories = ['weight', 'height', 'breed_group', 'temperament']

print("Welcome to my dog breed recommendation app!")
while flag:
    breed_list = []
    # User input to choose a category
    user_category = user_choose_category()
    # Check whether user input is recognised
    flag_category = check_validity_user_choice(categories, user_category)
    if flag_category:
        # Allow user to view available options
        options = show_options(current_data, user_category)  
        # If user input is valid, find user input for the category
        user_choice = user_choose_value()
        # Check whether the user has chosen a valid option
        flag_choice = check_validity_user_choice(options, user_choice)
        if flag_choice:
            for dog in current_data:
                try: 
                    dog[user_category]
                except KeyError:
                    pass
                else:
                    if dog[user_category].find(user_choice) != -1:
                        print(dog['name'])
                        breed_list.append(dog)
            # If there is only one dog available, this is the perfect match
            if len(breed_list) == 1:
                print("Good news, we have found your perfect match!")
                # Add in here API call for dog pic
                print(format_breed_detail(breed_list))
                flag = False
                break
            print(f"We have found {len(breed_list)} matches.")
            
            # Breed detail - user to provide y/n answer
            breed_yn_question = "Would you like to learn more about any of "
            breed_yn_question += "the dogs? y/n "
            user_input_breed_yn = user_choose_yn(breed_yn_question)
            while user_input_breed_yn == 'y':
                user_breed = input("Which breed would you like to "
                                               "learn more about? ").title()
                breed_detail = get_breed_detail(user_breed)
                if breed_detail == 'false':
                    print("Sorry, we do not recognise your search.")
                else:
                    print(format_breed_detail(breed_detail))
                user_input_breed_yn = user_choose_yn(breed_yn_question)
                
            current_data = breed_list
        else:
            print("Sorry, we do not recognise this category.")
    else:
        print("Sorry, we do not recognise this category.")    
    
    # Next search - user to provide y/n answer 
    next_search_question = "Would you like to continue with your search? y/n "
    user_input_next_search = user_choose_yn(next_search_question)
        
    # Ending search before finding the perfect match
    if user_input_next_search == "n":
        flag = False
        end_search_early(breed_list)

        
# test_data = [{'weight': {'imperial': '15 - 22', 'metric': '7 - 10'}, 'height': {'imperial': '10 - 11', 'metric': '25 - 28'}, 'id': 256, 'name': 'West Highland White Terrier', 'bred_for': 'Fox, badger, vermin hunting', 'breed_group': 'Terrier', 'life_span': '15 - 20 years', 'temperament': 'Hardy, Friendly, Alert, Independent, Gay, Active, Courageous'},
# {'weight': {'imperial': '25 - 35', 'metric': '11 - 16'}, 'height': {'imperial': '18 - 22', 'metric': '46 - 56'}, 'id': 257, 'name': 'Whippet', 'bred_for': 'Coursing, racing', 'breed_group': 'Hound', 'life_span': '12 - 15 years', 'temperament': 'Friendly, Affectionate, Lively, Gentle, Intelligent, Quiet'},
# {'weight': {'imperial': '60 - 85', 'metric': '27 - 39'}, 'height': {'imperial': '22 - 25', 'metric': '56 - 64'}, 'id': 258, 'name': 'White Shepherd', 'life_span': '12 – 14 years', 'temperament': 'Self-confidence, Aloof, Fearless, Alert, Companionable, Eager'},
# {'weight': {'imperial': '15 - 19', 'metric': '7 - 9'}, 'height': {'imperial': '13 - 16', 'metric': '33 - 41'}, 'id': 259, 'name': 'Wire Fox Terrier', 'bred_for': 'Vermin hunting, fox bolting', 'life_span': '13 – 14 years', 'history': ' England', 'temperament': 'Fearless, Friendly, Bold, Keen, Alert, Quick'},
# {'weight': {'imperial': '45 - 70', 'metric': '20 - 32'}, 'height': {'imperial': '20 - 24', 'metric': '51 - 61'}, 'id': 260, 'name': 'Wirehaired Pointing Griffon', 'bred_for': 'Gundog, "swamp-tromping", Flushing, pointing, and retrieving water fowl & game birds', 'breed_group': 'Sporting', 'life_span': '12 - 14 years', 'temperament': 'Loyal, Gentle, Vigilant, Trainable, Proud'},
# {'weight': {'imperial': '45 - 65', 'metric': '20 - 29'}, 'height': {'imperial': '21.5 - 25', 'metric': '55 - 64'}, 'id': 261, 'name': 'Wirehaired Vizsla', 'breed_group': 'Sporting', 'life_span': '12 - 14 years'},
# {'weight': {'imperial': '9 - 31', 'metric': '4 - 14'}, 'height': {'imperial': '10 - 23', 'metric': '25 - 58'}, 'id': 262, 'name': 'Xoloitzcuintli', 'breed_group': 'Non-Sporting', 'life_span': '12 - 14 years', 'temperament': 'Cheerful, Alert, Companionable, Intelligent, Protective, Calm'},
# {'weight': {'imperial': '4 - 7', 'metric': '2 - 3'}, 'height': {'imperial': '8 - 9', 'metric': '20 - 23'}, 'id': 264, 'name': 'Yorkshire Terrier', 'bred_for': 'Small vermin hunting', 'breed_group': 'Toy', 'life_span': '12 - 16 years', 'temperament': 'Bold, Independent, Confident, Intelligent, Courageous'}]
        
# check_validity_dog_detail(test_data, 'temperament')
    
# test_date = [{'weight': {'imperial': '44 - 66', 'metric': '20 - 30'}, 'height': {'imperial': '30', 'metric': '76'}, 'id': 3, 'name': 'African Hunting Dog', 'bred_for': 'A wild pack animal', 'life_span': '11 years', 'temperament': 'Wild, Hardworking, Dutiful', 'origin': ''}]
# format_dog_detail(test_date)
                