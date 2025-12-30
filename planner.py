from datetime import datetime
from ml_model import predict_priority

def calculate_priority(task):
    today = datetime.today()
    deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")
    days_left = max((deadline - today).days, 1)

    return predict_priority(
        days_left,
        task["difficulty"],
        task["time_required"],
        task["user_priority"]
    )

def prioritize_tasks(tasks):
    for task in tasks:
        task["priority_score"] = calculate_priority(task)

    return sorted(tasks, key=lambda x: x["priority_score"], reverse=True)


def generate_study_plan(tasks, daily_hours):
    plan = []
    remaining_hours = daily_hours

    for task in tasks:
        if remaining_hours <= 0:
            break

        allocated = min(task["time_required"], remaining_hours)
        plan.append({
            "task": task["task_name"],
            "subject": task["subject"],
            "hours": allocated
        })
        remaining_hours -= allocated

    return plan
