incomplete_task = ["Incomplete:", "jogging", "cooking", "swimming", "cleaning"]
completed_task = ["Complete:", ]
user_add = []

def user_interface():
    print("Welcome to the To-Do List App!")
    print("Menu:\n1. Add a task\n2. View task\n3. Mark a task as complete\n4. Delete a task\n5. Quit")

    while True:
        try:
            user_input1 = int(input("Pick an option: "))
            if user_input1 == 1:
                user_add = input("What item would you like to add?: ")
                incomplete_task.append(user_add)  
                print(f'You have now added {user_add}')
            elif user_input1 == 2:
                print(f'Showing you the current tasks: {incomplete_task}')
                print(f'Show your completed tasks: {completed_task}')
            elif user_input1 == 3:
                print(f'Which task should we mark as completed?: {incomplete_task}')
                item_to_move = input("Which task has been completed? ")
                if item_to_move in incomplete_task:
                    incomplete_task.remove(item_to_move)
                    completed_task.append(item_to_move)
                    print(f'These are the incomplete tasks: \n{incomplete_task}')
                    print(f'These are the completed tasks: \n{completed_task}')
                else:
                    print("Task not found in incomplete tasks.")
            elif user_input1 == 4:
                print("Which task would you like to delete?")
                print(f'These are the current tasks: {incomplete_task}') 
                item_to_remove = input("Enter the task you want to remove: ")
                if item_to_remove in incomplete_task:
                    incomplete_task.remove(item_to_remove)
                    print(f'Item {item_to_remove} is no longer in the task list.')
                else:
                    print("Item not found in the list.")
            elif user_input1 == 5:
                print("Have a great day and thank you for using our application!")
                break
            else:
                print("Please choose a valid option from the menu.")
        
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu options.")
        except Exception as e:
            print(f"An error occurred: {e}")

user_interface()
