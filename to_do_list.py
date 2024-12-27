tasks = []

while True:
    print("\nTo-Do List")
    print("1. Add List")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice(1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Your task is added to the list")

    elif choice == "2" :
        if not tasks:
            print("List is empty")
        else:
            print("\nYour tasks") 
            for i in range(len(task)):
                print(f"{i+1}.{tasks[i]}")
    
    elif choice == "3":
        if not tasks:
            print("list is empty")
        else:
            print("\Your Tasks")
            for i in range(len(tasks)):
                print(f"{i+1}.{tasks[i]}")
            task_num = int(input("Enter the task number to delete"))
            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num - 1)
                print("Task is deleted")
            else:
                print("invalid task number")   
    elif choice == "4":
        print("Good Bye !")
        break
    else:
        print("Invalid choice. Try again")