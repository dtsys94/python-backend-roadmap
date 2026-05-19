tasks = []

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")

    choice = int(input("Choose your option  "))

    if choice == 4:
        print("Bye")
        break

    elif choice == 1:
        add_task = input("What would you like to add?  ")
        tasks.append(add_task)
        print("Task added")
    
    elif choice == 2:
        if len(tasks) == 0:
            print("The list is empty")
        else:
            #print(*tasks, sep="\n")
            for task in tasks:
                print(task)
    
    elif choice == 3:
        if len(tasks) == 0:
            print("The list is empty")
        else:            
            print(*tasks, sep="\n")
            task_remove = input("Which task would you like to remove? ")
            tasks.remove(task_remove)
            print(*tasks, sep="\n")

    else:
        print("Invalid choice. Please pick 1-4.") 
      
        


