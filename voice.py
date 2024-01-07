def message_unauth(user_id):
    text = (f"Hmm, I understand that you are very curious, but I can not share anything with you right now! Try "
             f"contacting @boot_to_root . Your ID: {user_id}.")
    data = {
        'chat_id': user_id,
        'text': text
    }
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data=data)

def message_auth_voice(user_id, message):
    for i in range(len(VOICES)):
        if message == VOICES[i][1]:
            data = {
                'chat_id': user_id,
                'voice': VOICES[i][0],
                'caption': f"Suggest what should be written here.",
                'parse_mode': 'Markdown',
            }
            requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendVoice", json=data)
