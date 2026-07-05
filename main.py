import streamlit as st

st.title("📝 To-Do List App")

# session storage (temporary memory)
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ADD TASK
task = st.text_input("Enter your task")

if st.button("Add Task"):
    if task != "":
        st.session_state.tasks.append({"task": task, "done": False})
        st.success("Task Added!")

# SHOW TASKS
st.subheader("Your Tasks")

for i, t in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([5, 2, 2])

    col1.write(t["task"])

    if t["done"]:
        col2.write("✅ Done")
    else:
        if col2.button("Mark Done", key=i):
            st.session_state.tasks[i]["done"] = True

    if col3.button("Delete", key="d"+str(i)):
        st.session_state.tasks.pop(i)
        st.rerun()