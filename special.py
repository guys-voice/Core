import requests

def special(message):
  if message[:12] == 'SEND_MESSAGE':
    message[14:23]
  elif message[:10] == 'SEND_VOICE':
    message[10:21]
  else:
    return
