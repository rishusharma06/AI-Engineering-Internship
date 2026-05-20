#  using JSONPlaceholder =  
# This free service provides fake API endpoints that send back responses that requests can process.

import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
api_ur = "https://jsonplaceholder.typicode.com/todos"

# GET request
response = requests.get(api_url)
print("GET\n", response.json()) # To viewthe data which comes from an API
print(response.status_code)
print(response.headers["Content-Type"])

# POST request
todo = {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
response = requests.post(api_ur, json = todo)
print("\nPOST\n", response.json())

# PUT request
toadd = {'userId': 100, 'id': 111, 'title': 'Commit Code', 'completed': False}
response = requests.put(api_url, json = toadd)
print("\nPUT\n", response.json())

# PATCH request
toupdate = {'completed' : True}
response = requests.patch(api_url, json = toupdate)
print("\nPATCH\n", response.json())

# DELETE request
response = requests.delete(api_url)
print("\nDELETED\n", response.json())