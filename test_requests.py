import requests, json

headers = {
  'User-Agent': 'CrowBot v1.0'
}

webhook_url = "https://discord.com/api/webhooks/1521467779562082314/e4_f5HC-_8K8yFUMla1vBoClXLnk8UCv362A7Gf4tWQI3v7a5I5GKOJGOWeM3JSP3Hms"
url = 'https://commons.wikimedia.org/wiki/Special:Random'

r = requests.get(url, headers=headers, allow_redirects=False)
link = r.headers['Location']
new_link = link.split('/')[4]
new_link = 'https://commons.wikimedia.org/w/rest.php/v1/file/' + new_link

response = requests.get(new_link, headers=headers)
data = response.json()
ready_link = data["preferred"]["url"]

discord_message = requests.post(webhook_url, data={'content':ready_link})

print(ready_link+"\n")
print(response.status_code)