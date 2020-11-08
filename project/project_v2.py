# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 18:39:32 2020

@author: barbora
"""


import requests
import json
from datetime import datetime

endpoint = "https://api.thedogapi.com/v1/breeds"
query_params = {
    'api-key' : '42131d49-f92a-441c-8f40-4ade8c01a4ee',
    'attach_breed' : '0'
}

response = requests.get(endpoint, params=query_params)
print(response.status_code)
data = json.loads(response.content)

# Classify dogs by size
for breed in data:
    decide_interval = breed['weight']['imperial']
    num_interval = decide_interval.split(' - ')
    try:
        float(num_interval[1])
    except IndexError:
        pass
    else:
        decide_value = float(num_interval[1])
    if decide_value > 100:
        size = 'giant'
    elif decide_value > 50:
        size = 'large'
    elif decide_value > 25:
        size = 'medium'
    else:
        size = 'small'
    breed.update({'size' : size})
    
# Convert everything to lower case
for breed in data:
    for key in breed:
        if key not in ['weight', 'height']:
            try:
                value = str(breed[key])
            except AttributeError:
                pass
            else:
                breed.update({key : str(breed[key]).lower()})
    
# def user_choose_category():
#     """User input to choose a category."""
#     user_category = input("Which category would you like to consider? "
#                           "breed_group / "
#                           "temperament ").lower()
#     return user_category

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
    if len(data) == 1:
        congrats = "Good news, we have found your perfect match! "
    else:
        congrats = ""
    weight = check_validity_breed_detail_num(data, 'weight')
    height = check_validity_breed_detail_num(data, 'height')
    bred = check_validity_breed_detail_string(data, 'bred_for')
    group = check_validity_breed_detail_string(data, 'breed_group')
    life_span = check_validity_breed_detail_string(data, 'life_span')
    temperament = check_validity_breed_detail_string(data, 'temperament')
    message = f"{congrats}Here are some facts about {data[0]['name'].title()}:"
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
    options.append("any")
    return options

def show_options(dog_list, user_category):
    """Ask the user if they would like to see available options
    and show options if chosen.
    """
    options = list_options(dog_list, user_category)
    print(f"\nWe are now going to choose your dog's {user_category}. "
          "Here are your available options:")
    for item in options:
        if len(item) != 0:
            print(item.title())
    return options

def user_input_value(question, value_list):
    """Prompt user to select a charasteric value."""
    flag = True
    while flag:
        user_input = input(question).lower()
        flag = check_validity_user_input(value_list, user_input)
    return user_input
    
def check_validity_user_input(value_list, user_input):
    """Check whether the user has picked out of the available options."""
    if user_input in value_list:
        flag = False
    else:
        print("Sorry, we do not recognise your input. Please try again.")
        flag = True
    return flag

def create_breed_list(data, dict_key, user_input):
    """Append suitable breeds to a list."""
    breed_list = []
    if user_input == 'any':
        breed_list = data
    else:
        for breed in data:
            try: 
                breed[dict_key]
            except KeyError:
                pass
            else:
                if breed[dict_key].find(user_input) != -1:
                    breed_list.append(breed)
    return breed_list

def show_breeds(breed_list):
    """Display breeds stored in a breeds list."""
    for breed in breed_list:
        print(breed['name'].title())

def run_search(question, category, breed_list):
    """Obtain user input, run search and return a new list."""
    category_list = show_options(breed_list, category)
    user_category = user_input_value(question, category_list)
    breed_list = create_breed_list(breed_list, category, user_category)
    return breed_list

def show_matches(breed_list):
    """Show how many matches there are."""
    matches = f"We have found {len(breed_list)} matches."
    return matches

def end_search_early(dog_list):
    """Carry out final tasks when user chooses to end search early."""
    if len(dog_list) == 0:
        message = "We are sorry to say that we haven't found your perfect "
        message += "match. Keep searching, your perfect dog is out there!"
    else:
        message = "We haven't found your perfect match yet, but we believe that "
        message += "the following breeds would suit you well:"
        for dog in dog_list:
            message += "\n\t- " + dog['name'].title()
    return message
            
def save_to_file(final_result, now):
    """Save the outcome of the programme to a text file."""
    filename = f"{now}-search.txt"
    with open(filename, "w") as f:
        f.write(str(final_result))
    return "Your final result has been saved to a local file."

def get_breed_img(breed_id):
    """Function to pull image of a specific breed from the API based on
    the breed's id.
    """
    endpoint_breed_img = "https://api.thedogapi.com/v1/images/search"
    query_params_breed_img = {
        'api-key' : '42131d49-f92a-441c-8f40-4ade8c01a4ee',
        'breed_id' : breed_id,
    }
    response_breed_img = requests.get(endpoint_breed_img, 
                                       params=query_params_breed_img)    
    data_breed_img = json.loads(response_breed_img.content)
    try:
        data_breed_img_url = data_breed_img[0]['url']
    except IndexError:
        data_breed_img_url = None
    else:
        return data_breed_img_url

def save_breed_img(breed_name, breed_img_url, now):
    """Save an image of a breed."""
    if breed_img_url != None:
        response_img = requests.get(breed_img_url)
        breed_img = response_img.content
        filename = f"{now}-{breed_name}-img.jpg"
        with open(filename, "wb") as f:
            f.write(breed_img)
    else:
        print("Unfortunately there are no pictures available for this breed.")
        
def user_data(breed_list, question, characteristic):
    """"""
    if len(list_options(breed_list, characteristic)) > 2:
        breed_list = run_search(question, characteristic, breed_list)
        show_breeds(breed_list)
        print(show_matches(breed_list))
    else:
        current_char = list_options(breed_list, characteristic)[0]
        print(f"\nAll your current matches are {current_char} {characteristic}.")
    return breed_list
        
breed_list = data
flag = True
categories = ['size', 'breed_group', 'temperament']

print("Welcome to my dog breed recommendation programme!")
while flag:
    # Deal with size
    size_question = "What size dog would you like? "
    breed_list = user_data(breed_list, size_question, 'size')

    # Deal with breed_group
    breed_group_question = "What breed group would you like? "
    breed_list = user_data(breed_list, breed_group_question, 'breed_group')
    # breed_list = run_search(breed_group_question, 'breed_group', breed_list)
    # show_breeds(breed_list)
    # print(show_matches(breed_list))
    
    # Deal with temperament
    temperament_question = "What temperament should your dog have? "
    breed_list = user_data(breed_list, temperament_question, 'temperament')
    # breed_list = run_search(temperament_question, 'temperament', breed_list)
    # show_breeds(breed_list)
    # print(show_matches(breed_list))
    
    if len(breed_list) == 1:
        final_result = format_breed_detail(breed_list)
        print(final_result)
    else:
        final_result = end_search_early(breed_list)
        print(final_result)
    
    next_steps_question = "Would you like to learn more about any of these "
    next_steps_question += "dogs, refine your search, start a new search or "
    next_steps_question += "exit the programme? "
    next_steps_question += "learn/refine/new/exit "
    next_steps_options = ['learn', 'refine', 'new', 'exit']
    user_next_steps = user_input_value(next_steps_question, next_steps_options)
    
    while user_next_steps == 'learn':
        breed_question = "Which breed would you like to learn more about? "
        breed_options = list_options(breed_list, 'name')
        user_breed = user_input_value(breed_question, breed_options)
        breed_detail = get_breed_detail(user_breed)
        print(format_breed_detail(breed_detail))
        user_next_steps = user_input_value(next_steps_question, next_steps_options)
    if user_next_steps == 'refine':
        pass
    elif user_next_steps == 'exit' or user_next_steps == 'new':    
        # if len(breed_list) == 1:
        #     final_result = format_breed_detail(breed_list)
        #     print(final_result)
        # else:
        #     final_result = end_search_early(breed_list)
        #     print(final_result)
        now = datetime.now().strftime("%Y%m%d-%H%M")
        print(save_to_file(final_result, now))
        if len(breed_list) < 5:
            img_yn_question = "Would you like to save a picture of your "
            img_yn_question += "matched breed(s)? y/n "
            user_img_yn = user_input_value(img_yn_question, ['y', 'n'])
            if user_img_yn == 'y':
                for breed in breed_list:
                    breed_img_url = get_breed_img(breed['id'])
                    save_breed_img(breed['name'], breed_img_url, now)
                print("Picture(s) have been saved to a local file.")
            else:
                pass
        print("Thank you for using my dog recommendation programme!")
        if user_next_steps == 'exit':
            flag = False
        else:
            breed_list = data
            
    # Check whether user input is recognised
    #flag_category = check_validity_user_choice(categories, user_category)
    #if flag_category:
    # Allow user to view available options
    # options = show_options(current_data, user_category)  
    # # If user input is valid, find user input for the category
    # user_choice = user_choose_value()
    # # Check whether the user has chosen a valid option
    # flag_choice = check_validity_user_choice(options, user_choice)
    # if flag_choice:

    #     # If there is only one dog available, this is the perfect match
    #     if len(breed_list) == 1:
    #         print("Good news, we have found your perfect match!")
    #         # Add in here API call for dog pic
    #         print(format_breed_detail(breed_list))
    #         flag = False
    #         break
    #     print(f"We have found {len(breed_list)} matches.")
        
    #     # Breed detail - user to provide y/n answer
    #     breed_yn_question = "Would you like to learn more about any of "
    #     breed_yn_question += "the dogs? y/n "
    #     user_input_breed_yn = user_choose_yn(breed_yn_question)
    #     while user_input_breed_yn == 'y':
    #         user_breed = input("Which breed would you like to "
    #                                        "learn more about? ").title()
    #         breed_detail = get_breed_detail(user_breed)
    #         if breed_detail == 'false':
    #             print("Sorry, we do not recognise your search.")
    #         else:
    #             print(format_breed_detail(breed_detail))
    #         user_input_breed_yn = user_choose_yn(breed_yn_question)
            
    #     current_data = breed_list
    #     #else:
    #     #    print("Sorry, we do not recognise this category.")
    # else:
    #     print("Sorry, we do not recognise this category.")    
    
    # # Next search - user to provide y/n answer 
    # next_search_question = "Would you like to continue with your search? y/n "
    # user_input_next_search = user_choose_yn(next_search_question)
        
    # # Ending search before finding the perfect match
    # if user_input_next_search == "n":
    #     flag = False
    #     end_search_early(breed_list)

        
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
  
# for dog in data:
#     print(dog['size'])
    
#print(data)
#print(data[0]['weight']['metric'])
#print(datetime.now().strftime("%Y%m%d-%H%M"))
        
# for breed in breed_list:
#     breed_id = breed['id']
#     print(breed_id)
# print(breed_list)