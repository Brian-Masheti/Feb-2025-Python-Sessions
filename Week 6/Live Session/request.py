import requests

response = requests.get('https://api.github.com')
print('Status Code: ', response.status_code)  # 200

# Print the data from the API
data = response.json()  # Parse the JSON response
print('Response Data:', data)

