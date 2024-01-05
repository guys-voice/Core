from variables import BOT_TOKEN, AUTHORIZED_USER_IDS, voices

def send_show_options_to_users():
    for user_id in AUTHORIZED_USER_IDS:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        # Get all values from voices[1]
        options = [voice[1] for voice in voices]

        keyboard = {
            'keyboard': [[option] for option in options],
            'one_time_keyboard': True,
            'resize_keyboard': True
        }

        text = "Choose a voice title:"
        data = {
            'chat_id': user_id,
            'text': text,
            'reply_markup': json.dumps(keyboard)
        }

        response = requests.post(url, data=data)
        if response.status_code != 200:
            print(f"Failed to send options to user {user_id}: {response.content}")
        else:
            print(f"Successfully sent to user {user_id}")
