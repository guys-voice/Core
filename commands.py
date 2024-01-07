import json
import requests
from variables import BOT_TOKEN, ADMIN, GROUP, COMMANDS, AUTHORIZED_USER_IDS, VOICES, last_update_id, last_sent_time

def commands(user_id, name, message):
    if message == '/start':
        if not any(str(user_id) in line for line in open('users.txt')):
            with open('users.txt', 'a') as file:
                file.write(f"{user_id} {name}\n")
        data = {
            'chat_id': user_id,
            'text': f"Welcome {name}. Happy to see here.",
            'parse_mode': 'Markdown'
        }
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data=data)
            
    elif message == '/show':
        options = [voice[1] for voice in VOICES]
        keyboard = {
            'keyboard': [[option] for option in options],
            'one_time_keyboard': True,
            'resize_keyboard': True
        }
        data = {
            'chat_id': user_id,
            'text': "Choose a voice title. I will send the voice message.",
            'reply_markup': json.dumps(keyboard)
        }
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data=data)
        
    elif message == '/users':
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            number_of_users = len(lines)
        data = {
            'chat_id': user_id,
            'text': f"Currently, we have {number_of_users} users.",
            'parse_mode': 'Markdown'
        }
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data=data)
    elif message == '/stats':
        data = {
            'chat_id': user_id,
            'text': f"We still working on this...",
            'parse_mode': 'Markdown'
        }
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data=data)
    elif message == '/neon':
        data = {
            'chat_id': user_id,
            'text': f"Hello {name}, you have successfully logged in as a root user!",
            'parse_mode': 'Markdown'
        }
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data=data)
    else:
        return
# stats, users, neon kabi functionla shu yerda bo'ladi bulani ham webdan ham botdan turib ishlatsa bo'ladi preferable webdan faqat keep alivega ishlataman va qolganini sirli commandla bilan qilaman.
