import json, os, requests, time
from dotenv import load_dotenv

load_dotenv()

headers = {
  'User-Agent': 'WikimediaBot v1.0'
}

webhook_url = os.getenv('TOKEN')
url = 'https://commons.wikimedia.org/wiki/Special:Random'

# ~~~~~~~~~~~~~~~~~ Sends a new link X times
for i in range(5):
  r = requests.get(url, headers=headers, allow_redirects=False)
  link = r.headers['Location']
  if link.startswith('//') == True:
    link = 'https:' + link
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
    ready_link = 'https:' + ready_link
  print('Ready link: ' + ready_link)
  print('Link: ' + link)
  time.sleep(2)

  discord_message = requests.post(webhook_url, json={
    'embeds': [
      {
      'title': location.replace('_', '\\_'),
      'url': link
      },
      {
      'image': {
        'url': ready_link
      }
      }
    ]
  })
  if discord_message.status_code != 204:
    print(discord_message.json())
  print(discord_message.status_code)
  print(data)

# ~~~~~~~~~~~~~~~~~ Checks whether the file is an image
# if format in format_image:
#     print('The format of the file is ' + format + '.\n' + ready_link)
# else:
#     print('This file is not an image.')