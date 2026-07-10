import ctypes, os, requests, time
from dotenv import load_dotenv

load_dotenv() # Opens the window

headers = {
  'User-Agent': 'CrowBot'
}

webhook_url = os.getenv('TOKEN')
url = 'https://commons.wikimedia.org/wiki/Special:Random'

# ~~~~~~~~~~~~~~~~~ Sends a new link X times ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for i in range(1):
  r = requests.get(url, headers=headers, allow_redirects=False)
  link = r.headers['Location']
  if link.startswith('//') == True:
    link = 'https:' + link
  location = link.split('/')[4]
  new_link = 'https://commons.wikimedia.org/w/rest.php/v1/file/' + location

  # ~~~~~~~~~~~~~~~~~ Pull a new link out of the hat, show the status code ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  response = requests.get(new_link, headers=headers)
  print(response.status_code)
  if response.status_code == 429:
    time.sleep(10)
    continue
  data = response.json()
  ready_link = data['original']['url']

  # ~~~~~~~~~~~~~~~~~ File formats ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  format_audio = ''
  format_image = ''
  format_text = ('djvu', 'pdf', 'txt', 'doc', 'docx', 'epub')

  if data['preferred']['mediatype'] == 'AUDIO':
    format_audio = 'audio_file';
  elif data['preferred']['mediatype'] == 'BITMAP':
    format_image == 'image_file';
  format = link.split('.')[-1]

  # ~~~~~~~~~~~~~~~~~ Counter; adds https: to the links as well ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  if ready_link.startswith('https') == False:
    ready_link = 'https:' + ready_link

  file_request = requests.get(ready_link)
  file = file_request.content

  print(str(i + 1) + ' | Ready link: ' + ready_link)
  print(str(i + 1) + ' | Link: ' + link)
  time.sleep(4)

  # ~~~~~~~~~~~~~~~~~ Webhook ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  # discord_message = requests.post(webhook_url, json={
  #   'embeds': [
  #     {
  #     'title': location.replace('_', '\\_'),
  #     'url': link
  #     },
  #     {
  #     'image': {
  #       'url': ready_link
  #     }
  #     }
  #   ]
  # })

  # if discord_message.status_code != 204:
  #   print(discord_message.json())
  # print(discord_message.status_code)

MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, ':)', 'Check me out!!!', 0)