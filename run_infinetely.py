data1 = {
  'chat_id': ADMIN,
  'text': "I will be running, until I say I have finished.",
  'parse_mode': 'Markdown'
}
requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data=data)
try:
  subprocess.run(['python3', 'main.py'])
except Exception as e:
  data = {
    'chat_id': ADMIN,
    'text': f"I have finished. Error executing command: {e}",
    'parse_mode': 'Markdown'
  }
  requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data=data)
