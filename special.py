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
  elif message[:10] == 'SEND_VOICE':
    data = {
      'chat_id': int(message[10:21]),
      'text': message[23:],
      'parse_mode': 'Markdown'
    }
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data=data)
    return
  else:
    return
