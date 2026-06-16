#FUNCTIONS:

#load_tasks(tasks)
def load_tasks(tasks):
    with open('tasks_v3.txt','r') as file:
        for task in file:
            task = task.strip()
            tasks.append(task)


#add task
def add_task(tasks):
    new_task = input("Type your task ")
    if len(new_task.strip()) > 0:
        tasks.append(new_task.strip())
    else:
        print("You did not add task")

#view tasks
def view_tasks(tasks):
    if len(tasks) == 0:
        print("The list is empty")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

#remove task
def remove_task(tasks):
    if len(tasks) == 0:
        print("The list is empty")
        return
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

        user_remove = int(input("Type the number of task to remove "))
        if user_remove < 1 or user_remove > len(tasks):
            print("Wrong number")
        else: 
            tasks.pop(user_remove - 1)

def save_tasks(tasks):
    with open('tasks_v3.txt','w') as file:
        for task in tasks:
            file.write(f"{task}\n")

tasks =[]

#load_tasks(tasks)
load_tasks(tasks)



#menu
while True :
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove tasks")
    print("4. Quit")

    user_choice = int(input("Choose your option, type the number"))


    if user_choice == 1:
        add_task(tasks)


    elif user_choice == 2:
        view_tasks(tasks)


    elif user_choice == 3:
        remove_task(tasks)

    elif user_choice == 4:
        save_tasks(tasks)
        print("Bye")
        break
    

    else:
        print("Wrong number")

