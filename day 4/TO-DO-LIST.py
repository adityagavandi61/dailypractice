class TODOLIST:
    def __init__(self):
        self.tasks = []
        print("Welcome to the TO-DO LIST")
        self.menu()
    def menu(self):
        while True:
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.view_tasks()
            elif choice == 3:
                self.delete_task()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Try again.")

    def add_task(self):
        task = input("Enter the task: ")
        self.tasks.append(task)
        print("Task added successfully.")
    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"\n{i+1}. {task}\n")
            print("-------------------------------")
    def delete_task(self):
        self.view_tasks()
        task_no = int(input("Enter the task number to delete: "))
        del self.tasks[task_no-1]
        print("Task deleted successfully.")

if __name__ == "__main__":
    todolist = TODOLIST()
