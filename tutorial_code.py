# Python 3
# Get today's date in YYYY-MM-DD format.
import datetime

today = datetime.datetime.now()
date = today.strftime('%Y/%m/%d')

# Choose your language, and get today's featured content.
import requests
import json

language = 'en' # English Wikipedia
headers = {
  'User-Agent': 'YOUR_APP_OR_USER_NAME (YOUR_EMAIL_OR_CONTACT_PAGE)'
}

url = 'https://api.wikimedia.org/feed/v1/wikipedia/' + language + '/featured/' + date
response = requests.get(url, headers=headers)
data = response.json()
