import requests
import json
def view_all():
    response = requests.get('http://localhost:8000/api/tasks/')
    print("\nRemaining tasks:")
    for task in response.json()['tasks']:
        print(f"  ID {task['id']}: {task['title']} - Completed: {task['completed']}")

def add_task():
    while True:
        title = input("Enter title of task: ")
        if len(title) == 0:
            print("title can't be empty")
        else:
            break
    response = requests.post(
    'http://localhost:8000/api/tasks/',
    json={'title': title}
    )
    print("Created:", response.json())

def update_task():
    while True:
        task_id = input("\nEnter task ID to Update: ")
        if task_id.isdigit():
            task_id = int(task_id)
            break
        else:
            print("Not a number")
    response = requests.patch(
        f'http://localhost:8000/api/tasks/{task_id}/',
        json={'completed': True}
    )
    print("Updated:", response.json())

def delete_task():
    while True:
        task_id = input("\nEnter task ID to delete: ")
        if task_id.isdigit():
            task_id = int(task_id)
            break
        else:
            print("Not a number")

    response = requests.delete(f'http://localhost:8000/api/tasks/{task_id}/')
    print("Delete response:", response.json())


# View All Tasks
response = requests.get('http://localhost:8000/api/tasks/')
print("All tasks:")
for task in response.json()['tasks']:
    print(f"  ID {task['id']}: {task['title']} - Completed: {task['completed']}")

#menu
while True:
    print("Menu:")
    print("select from 1-5")
    print("1.View All Tasks")
    print("2.Add Task")
    print("3.Update Task")
    print("4.Delete Task")
    print("5.Exit")
    sel_men = input("select from menu")
    try:
        sel_men = int(sel_men)
        if sel_men == 1:
            view_all()
        elif sel_men == 2:
            add_task()
        elif sel_men == 3:
            update_task()
        elif sel_men == 4:
            delete_task()
        elif sel_men == 5:
            print("Exiting task-book")
            break
        else:
            print("Enter from 1-5")
    except ValueError:
        print("Invalid value, please enter NUMBER from 1-5")

