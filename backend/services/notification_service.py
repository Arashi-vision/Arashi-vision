notifications = {}

def push_notification(user_id, message):
    if user_id not in notifications:
        notifications[user_id] = []
    notifications[user_id].append({"msg": message})

def get_notifications(user_id):
    return notifications.get(user_id, [])
