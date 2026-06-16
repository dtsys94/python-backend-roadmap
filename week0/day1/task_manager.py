tasks = []

with open('week0/day1/tasks.txt', 'r') as r:
    for line in r:
        tasks.append(line.strip())

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")

    choice = int(input("Choose your option  "))

    if choice == 4:

        with open('week0/day1/tasks.txt', 'w') as f:
            for item in tasks:
                f.write(f'{item}\n')

        print("Bye")
        break

    elif choice == 1:
        add_task = input("What would you like to add?  ")
        if len(add_task.strip()) > 0:
            tasks.append(add_task.strip())
            print("Task added")
        else:
            print("The input is empty, add task")
    
    elif choice == 2:
        if len(tasks) == 0:
            print("The list is empty")
        else:
            #print(*tasks, sep="\n")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
    
    elif choice == 3:
        if len(tasks) == 0:
            print("The list is empty")
        else:            
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            
            task_number = int(input("Choose task number "))

            if task_number < 1 or task_number > len(tasks):
                print("Invalid task number")
            else:    
                tasks.pop(task_number - 1)
            
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            

    else:
        print("Invalid choice. Please pick 1-4.") 
      



