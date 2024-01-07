import requests

def special(message):
  if message[:12] == 'SEND_MESSAGE':
    data = {
      'chat_id': int(message[14:23]),
      'text': message[25:],
      'parse_mode': 'Markdown'
    }
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data=data)
    return
  elif message[:10] == 'SEND_FILE':
    data = {
      'chat_id': int(message[11:20]),
      'text': message[22:],
      'parse_mode': 'Markdown'
    }
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data=data)
    return
  else:
    return
