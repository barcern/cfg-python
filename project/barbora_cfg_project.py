# This project is modelled on project 2 - search. However, instead of looking
# up recipes based on ingredients, it attempts to match you to your ideal
# dog breed based on the input which you provide.
# The required tasks are fulfilled in the get_breed_detail() function, since
# it runs an API call using the user's input. Further functions are then 
# involved to ensure that the results are nicely formatted.

import requests
import json
from datetime import datetime

# Get all breed info via an API call to dog API
# More info here https://thedogapi.com/ and https://docs.thedogapi.com/
# Convert data to json
endpoint = "https://api.thedogapi.com/v1/breeds"
query_params = {
    'api-key' : '42131d49-f92a-441c-8f40-4ade8c01a4ee',
    'attach_breed' : '0'
}
response = requests.get(endpoint, params=query_params)
data = json.loads(response.content)

# Manipulate data for ease of use
# Convert everything to lower case, excluding height and weight since this
# would cause complications with classifying breeds by size 
for breed in data:
    for key in breed:
        if key not in ['weight', 'height']:
            try:
                value = str(breed[key])
            except AttributeError:
                pass
            else:
                breed.update({key : str(breed[key]).lower()})

# Classify dogs by size
# Weight is provided as a string e.g. '45 - 65' 
# so using the higher value to classify the breeds
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
    
# Functions used within the programme below
def get_breed_detail(breed):
    """Function to pull data for a specific breed from the API based on
    the breed's name.
    This function uses a user's input to pull relevant information, fulfiling
    required tasks for the search project.
    """
    endpoint_breed_detail = "https://api.thedogapi.com/v1/breeds/search"
    query_params_breed_detail = {
        'api-key' : '42131d49-f92a-441c-8f40-4ade8c01a4ee',
        'q' : breed,
    }
    response_breed_detail = requests.get(endpoint_breed_detail, 
                                       params=query_params_breed_detail)    
    data_breed_detail = json.loads(response_breed_detail.content)
    # The API returns 200 even if the call returns no data, hence flag 
    # invalid data
    if len(data_breed_detail) == 0:
        data_breed_detail = 'false'
    return data_breed_detail

def check_validity_breed_detail_num(data, key):
    """Check whether a key is present in the breed's dictionary and 
    return an appropriate response to be displayed for the user.
    This function is intended for weight and height categories only since they
    are structured differently to the remaining categories.
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
    """Check whether a key is present in the breed's dictionary and 
    return an appropriate response to be displayed for the user.
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
    """Return detailed breed information in a user-friendly format.
    Use the formatting functions to achieve this.
    """ 
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

def list_options(breed_list, user_category):
    """Create a list of available options so that users can choose a 
    characteristic which is available and will lead to results.
    Also to be used to verify validity of options during user input.
    """
    options = []
    for breed in breed_list:
        try: 
            breed[user_category]
        except KeyError:
            pass
        else:
            # Ensure that breeds are not repeated in a list even if they 
            # match multiple characteristics
            string = breed[user_category]
            string_split = string.split(", ")
            for item in string_split:
                if item in options:
                    pass
                else:
                    options.append(item)
    options.sort()
    options.append("any")
    return options

def show_options(breed_list, user_category):
    """Show available options to the user."""
    options = list_options(breed_list, user_category)
    print(f"\nWe are now going to choose your dog's {user_category}. "
          "Here are your available options:")
    for item in options:
        # Ensure that empty strings are not displayed
        if len(item) != 0:
            print("\t\t" + item.title())
    return options

def user_input_value(question, value_list, multi_values=True):
    """Prompt user to select a value and call a function to verify the
    validity of the user's choice. Choose between allowing for one input
    value only, or multiple values separated by a comma.
    """
    flag = True
    while flag:
        user_input = input(question).lower()
        # Create a list of input values separated by a comma
        user_input_list = user_input.split(", ")
        flag = check_validity_user_input(value_list, user_input_list, 
                                         multi_values)
    return user_input_list
    
def check_validity_user_input(value_list, user_input_list, multi_values):
    """Check whether the user has picked valid and available options."""
    for user_input in user_input_list:
        # Break the loop in user_input_value() if the user's input matches
        # an available option, repeat the loop
        if user_input in value_list:
            flag = False
        else:
            print("Sorry, we do not recognise your input. Please try again.")
            flag = True
            break
    # Verify whether only one value is submitted for single-value questions
    if multi_values == False and len(user_input_list) > 1:
        print("Sorry, we can only accept one answer.")
        flag = True
    return flag

def create_breed_list(data, dict_key, user_input_list):
    """Append suitable breeds to a list."""
    breed_list = []
    # If the user selects 'any', do not refine the list
    if 'any' in user_input_list:
        breed_list = data
    else:
        for user_input in user_input_list:
            for breed in data:
                try: 
                    breed[dict_key]
                except KeyError:
                    pass
                else:
                    # If the characteristic is available for the breed and
                    # the breed is not already on the list,
                    # add the breed to the list
                    if (breed[dict_key].find(user_input) != -1 
                        and breed not in breed_list):
                        breed_list.append(breed)
    return breed_list

def show_breeds(breed_list):
    """Display breeds stored in a breed list in a user-friendly format.
    Ensure results are displayed in alphabetical order.
    """
    print("The following breeds fulfil your criteria:")
    # Create a list of breed names only
    temp_list = []
    for breed in breed_list:
        temp_list.append(breed['name'])
    # Order breed names alphabetically, then print
    temp_list = sorted(temp_list)
    for breed in temp_list:
        print("\t- " + breed.title())

def run_search(question, category, breed_list):
    """Show available options, obtain user input, run search and 
    return an updated breed list.
    """
    category_list = show_options(breed_list, category)
    user_category = user_input_value(question, category_list)
    breed_list = create_breed_list(breed_list, category, user_category)
    return breed_list

def show_matches(breed_list):
    """Show the number of matches available."""
    matches = f"We have found {len(breed_list)} matches."
    return matches

def end_search_early(breed_list):
    """Carry out final tasks when user chooses to end search early."""
    print("\n")
    if len(breed_list) == 0:
        message = "We are sorry to say that we haven't found your perfect "
        message += "match. Keep searching, your perfect dog is out there!"
    else:
        # Ensure that the final message is formatted and breed are displayed
        # in alphabetical order
        message = "We haven't found your perfect match yet, but we believe that "
        message += "the following breeds would suit you well:"
        temp_list = []
        for breed in breed_list:
            temp_list.append(breed['name'])
        temp_list = sorted(temp_list)
        for breed in temp_list:
            message += "\n\t- " + breed.title()
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
    # Check whether an image is available for the breed
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
    """Ensure that user does not have to select options for categories which
    cannot be further refined (e.g. only large and any is available, so all 
    breeds are large). Used when a user chooses to refine their search.
    """
    if len(list_options(breed_list, characteristic)) > 2:
        breed_list = run_search(question, characteristic, breed_list)
        show_breeds(breed_list)
        print(show_matches(breed_list))
    else:
        current_char = list_options(breed_list, characteristic)[0]
        print(f"\nAll your current matches are {current_char} {characteristic}.")
    return breed_list
        
# Set the breed list to contain all available data at start of programme
# and set flag to True
breed_list = data
flag = True
categories = ['size', 'breed_group', 'temperament']
multi_options = "You can choose one or multiple options. "
multi_options += "Please separate multiple options using a comma, e.g. "
multi_options += "herding, hound "

# Start the programme
print("Welcome to my dog breed recommendation programme!")
while flag:
    # Handle breed size - get user input, verify its validity, display 
    # relevant information, return a refined list of breeds
    size_question = f"What size dog would you like? {multi_options}"
    breed_list = user_data(breed_list, size_question, 'size')

    # Handle breed_group - get user input, verify its validity, display 
    # relevant information, return a refined list of breeds
    breed_group_question = f"What breed group would you like? {multi_options}"
    breed_list = user_data(breed_list, breed_group_question, 'breed_group')
    
    # Handle breed temperament - get user input, verify its validity, display 
    # relevant information, return a refined list of breeds
    temperament_question = f"What temperament should your dog have? "
    temperament_question += f"{multi_options}"
    breed_list = user_data(breed_list, temperament_question, 'temperament')
    
    # Print a different response depending on whether only one match is 
    # available or there are multiple matches
    if len(breed_list) == 1:
        final_result = format_breed_detail(breed_list)
        print(final_result)
    else:
        final_result = end_search_early(breed_list)
        print(final_result)
    
    # User input for next steps
    next_steps_question = "Would you like to learn more about any of these "
    next_steps_question += "dogs, refine your search, start a new search or "
    next_steps_question += "exit the programme? "
    next_steps_question += "learn/refine/new/exit "
    next_steps_options = ['learn', 'refine', 'new', 'exit']
    user_next_steps = user_input_value(next_steps_question, 
                                       next_steps_options, False)
    
    # If user chooses to learn, run an API call based on the user's input
    # and return formatted information
    while user_next_steps[0] == 'learn':
        breed_question = "Which breed would you like to learn more about? "
        breed_options = list_options(breed_list, 'name')
        user_breed = user_input_value(breed_question, breed_options, False)
        breed_detail = get_breed_detail(user_breed)
        print(format_breed_detail(breed_detail))
        # Check the user's next steps, if user chooses learn then stay in
        # the while loop
        user_next_steps = user_input_value(next_steps_question, 
                                           next_steps_options, False)
    
    # If user chooses to refine, go back to the start of the programme
    # retaining the current list of breeds
    if user_next_steps[0] == 'refine':
        pass
    
    # If user chooses to exit or start a new search, save the current results
    # to a file named using timestamp-search
    elif user_next_steps[0] == 'exit' or user_next_steps[0] == 'new':    
        now = datetime.now().strftime("%Y%m%d-%H%M")
        print(save_to_file(final_result, now))
        # If there are fewer than 5 breeds available, offer to save a picture
        # each breed
        if len(breed_list) < 5:
            img_yn_question = "Would you like to save a picture of your "
            img_yn_question += "matched breed(s)? y/n "
            user_img_yn = user_input_value(img_yn_question, ['y', 'n'], False)
            # Run API calls to save relevant pictures, named timestamp-breed
            # name-img
            if user_img_yn[0] == 'y':
                for breed in breed_list:
                    breed_img_url = get_breed_img(breed['id'])
                    save_breed_img(breed['name'], breed_img_url, now)
                print("Picture(s) have been saved to a local file.")
            else:
                pass
        # For exiting, set flag to False and close the programme
        print("Thank you for using my dog breed recommendation programme!")
        if user_next_steps[0] == 'exit':
            flag = False
        # For a new search, set the current list to be all data available
        # and go to the start of the programme
        else:
            breed_list = data
            print("\nWelcome to your new search!")
            