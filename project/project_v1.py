import requests
import json

endpoint = "https://api.thedogapi.com/v1/breeds"
query_params = {
    'api-key' : '42131d49-f92a-441c-8f40-4ade8c01a4ee',
    'attach_breed' : '0'
}

response = requests.get(endpoint, params=query_params)
#print(response.status_code)
print(response.content)

data = json.loads(response.content)
print(data)
print(len(data))



print((data[0]))
current_data = data
flag = True
categories = ['weight', 'height', 'breed_group', 'temperament']
print("Welcome to my dog breed recommendation app!")
while flag:
    # User input to choose a category
    user_category = input("Which category would you like to consider? "
                          "weight / height / breed_group / "
                          "temperament ").lower()
    # Check whether user input is recognised
    if user_category in categories:
        pass
    else:
        print("I'm sorry but we don't recognise this category.")
    # User input for temperament
    user_selection = input(f"What {user_category} would you like your "
                           "dog to be? ")
    for dog in current_data:
        try: 
            dog[user_category]
        except KeyError:
            pass
        else:
            if dog[user_category].find(user_selection) != -1:
                print(dog['name'])
    user_continue = input("Would you like to continue with your serach? y/n ")
    if user_continue == "n":
        flag = False
        
