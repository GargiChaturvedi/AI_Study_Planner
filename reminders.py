from datetime import datetime

def check_reminders(tasks):
    alerts = []
    today = datetime.today()

    for task in tasks:
        deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")
        days_left = (deadline - today).days

        if days_left <= 1:
            alerts.append(f"⚠️ {task['task_name']} is due soon!")

    return alerts