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


current_data = data
dog_list = []
dog_list_old = []
flag = True
categories = ['weight', 'height', 'breed_group', 'temperament']
print("Welcome to my dog breed recommendation app!")
while flag:
    dog_list = []
    # User input to choose a category
    user_category = input("Which category would you like to consider? "
                          "weight / height / breed_group / "
                          "temperament ").lower()
    
    # Check whether user input is recognised
    if user_category in categories:
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
                  "match, keep searching, your perfect dog is out there!")
        else:
            print("We have matched you with these dogs breeds:")
            for dog in dog_list:
                print(dog['name'])
    else:
        current_data = dog_list
# I might want the dog list to store         
print(dog_list)

print(data)
        
