import requests
from variables import BOT_TOKEN, ADMIN, GROUP, COMMANDS, AUTHORIZED_USER_IDS, VOICES, last_update_id, last_sent_time

def commands(user_id, name, message):
    if message == '/start':
        if not any(user_id in line for line in open('users.txt')):
        with open('users.txt', 'a') as file:
            file.write(f"{user_id} {name}\n")
    elif message == '/show':
        return
    elif message == '/users':
        return
    elif message == '/stats':
        return
    elif message == '/neon':
        return
    else:
        return

def send_show_options_to_users(user_id):
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
# stats, users, neon kabi functionla shu yerda bo'ladi bulani ham webdan ham botdan turib ishlatsa bo'ladi preferable webdan faqat keep alivega ishlataman va qolganini sirli commandla bilan qilaman.
