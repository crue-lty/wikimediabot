import requests, json

headers = {
  'User-Agent': 'CrowBot v1.0'
}

webhook_url = "https://discord.com/api/webhooks/1521467779562082314/e4_f5HC-_8K8yFUMla1vBoClXLnk8UCv362A7Gf4tWQI3v7a5I5GKOJGOWeM3JSP3Hms"
url = 'https://commons.wikimedia.org/wiki/Special:Random'

r = requests.get(url, headers=headers, allow_redirects=False)
link = r.headers['Location']
new_link = link.split('/')[4]

format_audio = ('mp3', 'ogg', 'flac', 'wav', 'wave', 'midi', 'wma', 'aiff', 'aac', 'alac')
format_image = ('jpg', 'jpeg', 'png', 'tif', 'tiff', 'bmp', 'svg', 'gif', 'webp', 'xcf', 'dng', 'raw', 'ico', 'avif')
format_text = ('djvu', 'pdf', 'txt', 'doc', 'docx', 'epub')

new_link = 'https://commons.wikimedia.org/w/rest.php/v1/file/' + new_link

response = requests.get(new_link, headers=headers)
print(response.status_code)
data = response.json()
ready_link = data['preferred']['url']
format = ready_link.split('.')[-1]

# If there's no 'https:' at the beginning:
if ready_link.startswith('https') == False:
  fixed_link = 'https:' + ready_link
  print(fixed_link)
else:
  print(ready_link)

# # for i in range(5):
# #   r = requests.get(url, headers=headers, allow_redirects=False)
# #   link = r.headers['Location']
# #   new_link = link.split('/')[4]
# #   print(new_link)
# #   i = i + 1

# # print(response.status_code)

# if format in format_image:
#     print('The format of the file is ' + format + '.\n' + ready_link)
# else:
#     print('This file is not an image.')

discord_message = requests.post(webhook_url, data={'content':ready_link})
