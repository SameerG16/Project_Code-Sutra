from flask import Blueprint, request, jsonify
from app.utils import send_telegram_notification

main = Blueprint('main', __name__)

@main.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    repo = data.get('repository', {}).get('full_name')
    pusher = data.get('pusher', {}).get('name')
    commit = data.get('head_commit', {}).get('message')
    send_telegram_notification(f"New push to {repo} by {pusher}: {commit}")
    return jsonify({"status": "Notification sent"})
