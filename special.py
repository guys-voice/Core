import requests
from variables import ADMIN


def special(message):
  if 1==1: #message[:12] == 'SEND_MESSAGE':
    data = {
      'chat_id': ADMIN,
      'text': f"id: {message[13:23]} and message: {message[24:]}",
      'parse_mode': 'Markdown'
    }
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data=data)
    data = {
      'chat_id': int(message[13:23]),
      'text': message[24:],
      'parse_mode': 'Markdown'
    }
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data=data)
    return
  elif message[:10] == 'SEND_FILE':
    # need to ellaborate on that further
    return
  else:
    return
