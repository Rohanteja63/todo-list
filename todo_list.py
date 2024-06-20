def add_task(tasks):
    task_name = input("Enter task name: ")
    due_date = input("Enter due date(optional, format YYYY-MM-DD): ")
    tasks.append({'tasks':task_name,'status': 'pending','due_date':due_date})
    print("Tasks added sucessfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks):
            print(f"{idx + 1}. Task: {task['task']}, Status: {task['status']}, Due Date: {task['due_date']}")

def update_task(tasks):
    task_number = int(input("Enter the task number to update: "))
    if 1 <= task_number <= len(tasks):
        task = tasks[task_number - 1]
        print(f"Current details: Task: {task['task']}, Status: {task['status']}, Due Date: {task['due_date']}")
        task['task'] = input("Enter new task name (or press enter to keep current): ") or task['task']
        task['status'] = input("Enter new status (pending/completed, or press enter to keep current): ") or task['status']
        task['due_date'] = input("Enter new due date (optional, format YYYY-MM-DD, or press enter to keep current): ") or task['due_date']
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    task_number = int(input)("Enter the task number to delete: ")
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number -1)
        print("Task deleted sucessfully.")
    else:
        print("Invalid task number.")

def main():
    tasks=[]
    while True:
        print("\nTo Do-List Application")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Update Tasks")
        print("4. Delete Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()