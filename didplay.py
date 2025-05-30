# Simple To-Do List Manager
def display_menu():
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def main():
    tasks = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            task = input("Enter task: ")
            tasks.append(task)
            print(f"Task '{task}' added!")
        
        elif choice == '2':
            if tasks:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks yet!")
        
        elif choice == '3':
            if tasks:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    index = int(input("Enter task number to remove: ")) - 1
                    if 0 <= index < len(tasks):
                        removed_task = tasks.pop(index)
                        print(f"Task '{removed_task}' removed!")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number!")
            else:
                print("No tasks to remove!")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()