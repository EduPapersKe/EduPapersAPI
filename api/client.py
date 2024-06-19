import requests
import json

""" 
if you want to use a python script to consume the api this will help,run it outside the app or just here 
it dosent need the server its just a standalone script. it will be updated to have all endpoints
for now it only gets CRUD for comments and get/list for resource,  
"""

API_URL = 'http://127.0.0.1:5000/api/v1'

API_KEY = '04beef4d-11f8-46f9-9511-eef8c7014d00' 

def auth():
    endpoint = f'{API_URL}/users/login/'
    headers={"API-KEY": API_KEY} 
    json={"username":"adminbedah",
          "password":"Were254#" ,
        }
    response = requests.post(endpoint,json,headers=headers)
    if response.status_code == 200 :
        token=response
        return token.json()
    return response.json()

token=auth()['token']

def getCommentsorResources():
    headers={"API-KEY": API_KEY} 
    endpoint = f'{API_URL}/comments/' #for resources change to : /resources/ 
    response = requests.get(endpoint,headers=headers)
    #put this in a list if you need the info like comment id later
    return response.json()

def createUpdate():
    headers = {"API-KEY":API_KEY}
    endpoint = f'{API_URL}/comments/create/' #change to:  comments/{commentid}/update  -> when updating
    payload = {
        "text": "api call from a python script",
        "resource": "511621d3-db7a-4e16-9855-4408c81b245f",
    }
    
    response = requests.post(endpoint, headers=headers, json=payload)
    
    if response.status_code == 201:
        print("Comment created/updated successfully.")
    else:
        print(f"Failed to create/update comment. Status code: {response.status_code}")
        print(response.json)  # Print the error details if available
    
    return response

def delete_comment(comment_id):
        headers = {'API-KEY':API_KEY}
        endpoint = f'{API_URL}/comments/{comment_id}delete/'
        response = requests.delete(endpoint, headers=headers)
        
        if response.status_code == 204:
            print("Comment deleted successfully.")
        elif response.status_code == 404:
            print("Comment not found.")
        else:
            print(f"Failed to delete comment. Status code: {response.status_code}")
            print("Response:", response.json())
            
#print(delete_comment("replace with commentid"))

#print(createUpdate())

print(getCommentsorResources())

#print(auth())
