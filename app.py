import streamlit as st
from planner import prioritize_tasks, generate_study_plan
from reminders import check_reminders

st.title("🤖 AI Study Planner")

tasks = []

st.header("Add a Task")
with st.form("task_form"):
    task_name = st.text_input("Task Name")
    subject = st.text_input("Subject")
    deadline = st.date_input("Deadline")
    difficulty = st.slider("Difficulty", 1, 5)
    time_required = st.number_input("Estimated Time (hrs)", 1)
    user_priority = st.slider("Your Priority", 1, 5)
    submit = st.form_submit_button("Add Task")

    if submit:
        tasks.append({
            "task_name": task_name,
            "subject": subject,
            "deadline": str(deadline),
            "difficulty": difficulty,
            "time_required": time_required,
            "user_priority": user_priority
        })
        st.success("Task Added!")

if tasks:
    st.header("📌 Prioritized Tasks")
    prioritized = prioritize_tasks(tasks)
    st.write(prioritized)

    st.header("📅 Today's Study Plan")
    daily_hours = st.slider("Available Study Hours", 1, 10)
    plan = generate_study_plan(prioritized, daily_hours)
    st.write(plan)

    st.header("⏰ Reminders")
    reminders = check_reminders(tasks)
    for r in reminders:
        st.warning(r)