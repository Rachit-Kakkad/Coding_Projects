tasks = []

def show_menu():
    print("\n📋 To-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter your task: ")
    tasks.append({"task": task, "done": False})
    print("✅ Task added successfully!")

def view_task():
    if not tasks:
        print("❌ No tasks yet! Please add some.")
    else:
        print("\n📃 ----- Your Task List -----")
        for i, t in enumerate(tasks):
            status = "✅" if t["done"] else "❌"
            print(f"{i+1}. {t['task']} [{status}]")

def delete_task():
    view_task()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"🗑️ Removed: {removed['task']}")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Enter a valid number!")

# Main Loop
while True:
    show_menu()
    try:
        choice = int(input("Enter your choice (1 to 4): "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("👋 Exiting... Catch you later!")
            break
        else:
            print("❌ You have selected an invalid option!")
    except ValueError:
        print("❌ Please enter a number between 1 and 4.")
