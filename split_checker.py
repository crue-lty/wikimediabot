import json, requests, time

headers = {
  'User-Agent': 'WikimediaBot v1.0'
}

webhook_url = "https://discord.com/api/webhooks/1521467779562082314/e4_f5HC-_8K8yFUMla1vBoClXLnk8UCv362A7Gf4tWQI3v7a5I5GKOJGOWeM3JSP3Hms"
url = 'https://commons.wikimedia.org/wiki/Special:Random'

# ~~~~~~~~~~~~~~~~~ Sends a new link X times
for i in range(3):
  r = requests.get(url, headers=headers, allow_redirects=False)
  link = r.headers['Location']
  location = link.split('/')[4]
  new_link = 'https://commons.wikimedia.org/w/rest.php/v1/file/' + location

  response = requests.get(new_link, headers=headers)
  data = response.json()
  ready_link = data['preferred']['url']

  # ~~~~~~~~~~~~~~~~~ File formats
  format_audio = ('mp3', 'ogg', 'flac', 'wav', 'wave', 'midi', 'wma', 'aiff', 'aac', 'alac')
  # format_image = ('jpg', 'jpeg', 'png', 'tif', 'tiff', 'bmp', 'svg', 'gif', 'webp', 'xcf', 'dng', 'raw', 'ico', 'avif')
  format_bitmap = data['preferred']['mediatype']
  format_text = ('djvu', 'pdf', 'txt', 'doc', 'docx', 'epub')
  format = ready_link.split('.')[-1]

  if ready_link.startswith('https') == False:
    fixed_link = 'https:' + ready_link
    print(fixed_link)
  else:
    print("Ready link: " + ready_link)
  time.sleep(3)

  discord_message = requests.post(webhook_url, data={'content':ready_link})

# ~~~~~~~~~~~~~~~~~ Checks whether the file is an image
# if format in format_image:
#     print('The format of the file is ' + format + '.\n' + ready_link)
# else:
#     print('This file is not an image.')


