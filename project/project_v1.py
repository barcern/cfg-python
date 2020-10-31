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
    """User input to choose a category"""
    user_category = input("Which category would you like to consider? "
                          "weight / height / breed_group / "
                          "temperament ").lower()
    return user_category

def get_dog_detail(breed):
    """Function to pull data for a specific breed from the API based on
    the breed's name
    """
    endpoint_dog_detail = "https://api.thedogapi.com/v1/breeds/search"
    query_params_dog_detail = {
        'api-key' : '42131d49-f92a-441c-8f40-4ade8c01a4ee',
        'q' : breed,
    }
    response_dog_detail = requests.get(endpoint_dog_detail, 
                                       params=query_params_dog_detail)    
    data_dog_detail = json.loads(response_dog_detail.content)
    return data_dog_detail

def format_dog_detail(data_dog_detail):
    """Return detailed breed information in a user-friendly format"""
    data = data_dog_detail
    weight = f"Weight is {data[0]['weight']['metric']} kg."
    height = f"Height is {data[0]['height']['metric']} cm."
    message = f"Here are some facts about {data[0]['name']}:"
    message += f"\n\t- {weight} \n\t- {height}"
    return message

def list_options(dog_list, user_category):
    """Create a list of available options so that users can choose a 
    characteristic which is available
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
    and show options if chosen
    """
    user_question = input("Would you like to see all available options? y/n ")
    if user_question == 'y':
        options = list_options(dog_list, user_category)
        print(options)
        return options
    else:
        pass
        
# test_data = [{'weight': {'imperial': '15 - 22', 'metric': '7 - 10'}, 'height': {'imperial': '10 - 11', 'metric': '25 - 28'}, 'id': 256, 'name': 'West Highland White Terrier', 'bred_for': 'Fox, badger, vermin hunting', 'breed_group': 'Terrier', 'life_span': '15 - 20 years', 'temperament': 'Hardy, Friendly, Alert, Independent, Gay, Active, Courageous'},
# {'weight': {'imperial': '25 - 35', 'metric': '11 - 16'}, 'height': {'imperial': '18 - 22', 'metric': '46 - 56'}, 'id': 257, 'name': 'Whippet', 'bred_for': 'Coursing, racing', 'breed_group': 'Hound', 'life_span': '12 - 15 years', 'temperament': 'Friendly, Affectionate, Lively, Gentle, Intelligent, Quiet'},
# {'weight': {'imperial': '60 - 85', 'metric': '27 - 39'}, 'height': {'imperial': '22 - 25', 'metric': '56 - 64'}, 'id': 258, 'name': 'White Shepherd', 'life_span': '12 – 14 years', 'temperament': 'Self-confidence, Aloof, Fearless, Alert, Companionable, Eager'},
# {'weight': {'imperial': '15 - 19', 'metric': '7 - 9'}, 'height': {'imperial': '13 - 16', 'metric': '33 - 41'}, 'id': 259, 'name': 'Wire Fox Terrier', 'bred_for': 'Vermin hunting, fox bolting', 'life_span': '13 – 14 years', 'history': ' England', 'temperament': 'Fearless, Friendly, Bold, Keen, Alert, Quick'},
# {'weight': {'imperial': '45 - 70', 'metric': '20 - 32'}, 'height': {'imperial': '20 - 24', 'metric': '51 - 61'}, 'id': 260, 'name': 'Wirehaired Pointing Griffon', 'bred_for': 'Gundog, "swamp-tromping", Flushing, pointing, and retrieving water fowl & game birds', 'breed_group': 'Sporting', 'life_span': '12 - 14 years', 'temperament': 'Loyal, Gentle, Vigilant, Trainable, Proud'},
# {'weight': {'imperial': '45 - 65', 'metric': '20 - 29'}, 'height': {'imperial': '21.5 - 25', 'metric': '55 - 64'}, 'id': 261, 'name': 'Wirehaired Vizsla', 'breed_group': 'Sporting', 'life_span': '12 - 14 years'},
# {'weight': {'imperial': '9 - 31', 'metric': '4 - 14'}, 'height': {'imperial': '10 - 23', 'metric': '25 - 58'}, 'id': 262, 'name': 'Xoloitzcuintli', 'breed_group': 'Non-Sporting', 'life_span': '12 - 14 years', 'temperament': 'Cheerful, Alert, Companionable, Intelligent, Protective, Calm'},
# {'weight': {'imperial': '4 - 7', 'metric': '2 - 3'}, 'height': {'imperial': '8 - 9', 'metric': '20 - 23'}, 'id': 264, 'name': 'Yorkshire Terrier', 'bred_for': 'Small vermin hunting', 'breed_group': 'Toy', 'life_span': '12 - 16 years', 'temperament': 'Bold, Independent, Confident, Intelligent, Courageous'}]
        
# show_options(test_data, 'temperament')

current_data = data
#print(current_data)
dog_list = []
dog_list_old = []
flag = True
categories = ['weight', 'height', 'breed_group', 'temperament']
print("Welcome to my dog breed recommendation app!")
while flag:
    dog_list = []
    # User input to choose a category
    user_category = user_choose_category()
    # Check whether user input is recognised
    if user_category in categories:
        # Allow user to view available options
        options = show_options(current_data, user_category)        
        # If user input is valid, find user input for the category
        user_selection = input(f"What {user_category} would you like your "
                               "dog to be? ").title()
        for dog in current_data:
            try: 
                dog[user_category]
            except KeyError:
                pass
            else:
                if dog[user_category].find(user_selection) != -1:
                    print(dog['name'])
                    dog_list.append(dog)
        user_dog_detail = input("Would you like to learn more about any of "
                                "the dogs? y/n ")
        if user_dog_detail == 'y':
            flag_dog_detail = True
        else:
            flag_dog_detail = False
        while flag_dog_detail == True:
            user_breed = input("Which breed would you like to "
                                           "learn more about? ").title()
            dog_detail = get_dog_detail(user_breed)
            print(format_dog_detail(dog_detail))
            user_dog_detail = input("Would you like to learn more about any "
                                "other dogs? y/n ")
            if user_dog_detail == 'n':
                flag_dog_detail = False
    
    else:
        print("I'm sorry but we don't recognise this category.")
        
    # If there is only one dog available, this is the perfect match
    if len(dog_list) == 1:
        print("Good news, we have found your perfect match!")
        # Add in here API call for dog pic
        flag = False
        break
    print(f"We have found {len(dog_list)} matches.")
    user_continue = input("Would you like to continue with your search? y/n ")
    if user_continue == "n":
        flag = False
        if len(dog_list) == 0:
            print("We are sorry to say that we haven't found your perfect "
                  "match. Keep searching, your perfect dog is out there!")
        else:
            print("We have matched you with these dogs breeds:")
            for dog in dog_list:
                print(dog['name'])
    else:
        current_data = dog_list
# I might want the dog list to store         
print(dog_list)

        
