visits = 0
active_users = set()

def add_visit():
    global visits
    visits += 1

def add_active(user_id):
    active_users.add(user_id)

def get_stats():
    return {
        "total_visits": visits,
        "active_users": len(active_users)
    }
