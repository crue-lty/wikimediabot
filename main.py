import ctypes, os, requests, time
from dotenv import load_dotenv
from urllib.parse import unquote

load_dotenv() # Opens the window

headers = {
  'User-Agent': 'CrowBot'
}

webhook_url = os.getenv('TOKEN')
url = 'https://commons.wikimedia.org/wiki/Special:Random'

# ~~~~~~~~~~~~~~~~~ Sends a new link X times ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for i in range(10):
  r = requests.get(url, headers=headers, allow_redirects=False)
  link = r.headers['Location']
  if link.startswith('//') == True:
    link = 'https:' + link
  location = link.split('/')[4]
  embed_title = unquote(location.replace('_', ' ')).split(':')[-1].split('.')[0:-1]
  embed_title = str('.'.join(embed_title))

  new_link = 'https://commons.wikimedia.org/w/rest.php/v1/file/' + location
  
  # ~~~~~~~~~~~~~~~~~ Pull a new link out of the hat, show the status code ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  response = requests.get(new_link, headers=headers)
  print(response.status_code)
  if response.status_code == 429:
    time.sleep(10)
    continue
  data = response.json()
  ready_link = data['preferred']['url']

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
  print(str(i + 1) + ' | Ready link: ' + ready_link)
  print(str(i + 1) + ' | Link: ' + link)
  print(str(i + 1) + ' | This is the embedded title: ' + embed_title)
  time.sleep(4)

  # ~~~~~~~~~~~~~~~~~ Webhook ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  discord_message = requests.post(webhook_url, json={
    'embeds': [
      {
      'title': embed_title,
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

# MessageBox = ctypes.windll.user32.MessageBoxW
# MessageBox(None, ':)', 'Check me out!!!', 0)