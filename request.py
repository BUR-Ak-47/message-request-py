import requests

# https://discord.com/api/vw9/channels/CHANEL_ID/messages

payload = {
  'content': "hello world"
}

header = {
  'authorization': 'TOKEN'
}

r = requests.post ("https://discord.com/api/v9/channels/CHANEL_ID/messages", data=payload, headers=header)
