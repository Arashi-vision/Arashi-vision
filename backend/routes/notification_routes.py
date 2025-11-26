from fastapi import APIRouter

router = APIRouter(prefix="/notify")

from services.notification_service import push_notification, get_notifications

@router.get("/{user_id}")
def fetch(user_id: str):
    return {"notifications": get_notifications(user_id)}
