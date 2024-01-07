import requests
from variables import ADMIN


def special(message):
  if message[:12] == 'SEND_MESSAGE':
    data = {
      'chat_id': ADMIN,
      'text': f"id: {message[14:23]} and message: {message[25:]}",
      'parse_mode': 'Markdown'
    }
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data=data)
    data = {
      'chat_id': int(message[14:23]),
      'text': message[25:],
      'parse_mode': 'Markdown'
    }
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data=data)
    return
  elif message[:10] == 'SEND_FILE':
    # need to ellaborate on that further
    return
  else:
    return
