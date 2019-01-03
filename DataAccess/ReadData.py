##ur Oath1 keys, remember to update for every push, better yet do some credential handling

client_key = 'IM5rJesuLG3qMyn4B72Cn9jrn'
client_secret = 'E5xAx5Ap5elnn26d8Ub8x7l8zJrvA0jHz1WIFM8q0suXCcTgXd'

import base64

key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')


import requests

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

# Check status code okay
print(auth_resp.status_code)

access_token = auth_resp.json()['access_token']

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

#the search_params specify the data request parameter
search_params = {'query': '#Metoo lang:en place_country:us',
                 'maxResults': '100',
                 'fromDate': '201703010000',
                 'toDate': '201812310000',
                 }

search_url = '{}1.1/tweets/search/fullarchive/tutorial.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

#check search response
print(search_resp.status_code)

tweet_data = search_resp.json()
# ... tweet_data

#pull out 100 Tweets from Sun Dec 30 23:59:56 +0000 2018 to Sun Dec 30 00:39:11 +0000 2018
for val in tweet_data['results']:
    print(val)

print('')

#get the next parameter for the next query
print(tweet_data['next'])
