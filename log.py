from variables import BOT_TOKEN, ADMIN, GROUP, COMMANDS, AUTHORIZED_USER_IDS, VOICES, last_update_id, last_sent_time

def log_unauth(update):
    return update
def ignore():
    return 1
def log_ignore(update):
    return update
def log_auth(update):
    return update
