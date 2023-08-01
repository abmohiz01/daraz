import requests
import json

def get_access_token():
    # You need to implement this function to get the API access token
    # Return the access token here
    return "YOUR_ACCESS_TOKEN"

def get_email_finder():
    token = get_access_token()
    params = {
        'access_token': token,
        'domain': 'https://www.linkedin.com/in/mianzainlatif/',
        'firstName': 'Mian Zain',
        'lastName': 'Latif'
    }

    res = requests.post('https://api.snov.io/v1/get-emails-from-names', data=params)

    return json.loads(res.text)

# Call the function to get the result
result = get_email_finder()
print(result)
