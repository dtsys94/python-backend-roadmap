# functions:

# function add task
def add_tasks(tasks):
    add_task = input("Type in your task: ")
    if len(add_task.strip()) > 0:
            tasks.append(add_task.strip())
    else:
            print("The input is empty, add task") 

# function view tasks 
def view_tasks(tasks):
        if len(tasks) == 0:
            print("The list is empty")
        else:
            for index, task in enumerate(tasks, start= 1):
                print (f"{index}. {task}")

# function remove task
def remove_task(tasks):
        if len(tasks) == 0:
            print("The list is empty")  
        else:
            for index, task in enumerate(tasks, start=1):
                print (f"{index}. {task}")
                   
            user_remove = int(input("Choose task number to remove: "))

            if user_remove < 1 or user_remove > len(tasks):
                print("Invalid task number")
        
            else: 

                tasks.pop(user_remove - 1)

                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
            
                print("That`s it")
     
# function load tasks
def load_tasks(tasks):
    with open ('week0/day1/tasks_v2.txt','r') as file:
        for line in file:
            tasks.append(line.strip())

# function save tasks
def save_tasks(tasks):
        with open('week0/day1/tasks_v2.txt','w') as file:
            for task in tasks:
                file.write(f"{task}\n")

        print("Thank you, bye!")     
     

# empty list  
tasks = [] 

# load file
load_tasks(tasks)

# menu
while True :
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")

# User input
    user_choice = int(input("Choose your option, type in number: "))

# 1. Add task
    if user_choice == 1:
        add_tasks(tasks)


# 2. View tasks
    elif user_choice == 2:
        view_tasks(tasks)



# 3. Remove task
    elif user_choice == 3:
        remove_task(tasks)

# 4. Quit 
    elif user_choice == 4:
        save_tasks(tasks)
        
        break

# Wrong choice
    else:
        user_choice_repeat=int(input("Invalid choice. Please pick 1-4. ")) 