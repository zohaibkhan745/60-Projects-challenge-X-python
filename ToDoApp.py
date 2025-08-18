class Task:
    def __init__(self, desc):
        self.desc = desc
        self.status = False   # False = Not Done, True = Done

    def complete(self):
        self.status = True

    def __str__(self):
        status = "✔️ Done" if self.status else "❌ Not Done"
        return f"{self.desc} [{status}]"


class TODO:
    def __init__(self):
        self.list = []

    def add(self, desc):
        task = Task(desc)
        self.list.append(task)
        print(f"Task added: {desc}")

    def delete(self, index):
        try:
            removed = self.list.pop(index)
            print(f"{removed.desc} removed")
        except IndexError:
            print("Invalid Index")

    def edit(self, index, desc):
        try:
            self.list[index].desc = desc
            print("Task updated.")
        except IndexError:
            print("Invalid task number")

    def complete(self, index):
        try:
            self.list[index].complete()
            print("Task marked as completed.")
        except IndexError:
            print("Invalid task number.")

    def view(self):
        if not self.list:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.list):
                print(f"{i}. {task}")


def main():
    todo = TODO()

    while True:
        print("\n--- TODO MENU ---")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Edit Task")
        print("4. Mark Completed")
        print("5. View All Tasks")
        print("6. Quit")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if choice == 1:
            desc = input("Enter task desc: ")
            todo.add(desc)
        elif choice == 2:
            index = int(input("Enter Index: "))
            todo.delete(index)
        elif choice == 3:
            index = int(input("Enter Index: "))
            desc = input("Enter New Description: ")
            todo.edit(index, desc)
        elif choice == 4:
            index = int(input("Enter Index: "))
            todo.complete(index)
        elif choice == 5:
            todo.view()
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
