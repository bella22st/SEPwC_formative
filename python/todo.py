import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Function: add_task
    
    Adds a task to out save file

    Input - a task to add to the list
    Return - nothing
    """

    print("Your item is: " + str(task))

    f = open(TASK_FILE, "a")
    x = f.write(task + "\n")
    f.close()

    print("Wrote " + str(x) + " characters to the file")


def list_tasks():
    """Function: list_tasks

    Lists all of the tasks saved to the file
    
    Input - nothing
    Return - Nothing 
    
    """
    f = open(TASK_FILE, "r")
    lines = f.readlines()
    f.close()




    return
    


def remove_task(index):
    return
    
def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
