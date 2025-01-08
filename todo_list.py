tasks = []

def add_task(task):
    tasks.append(task)
    return tasks



def delete_tasks(task):
    if task in tasks:
        tasks.remove(task)
    else:
        print(f"Task '{task}' not found")
    return tasks


while True:
    taask= input("Enter Your Tasks (or type 'exit' for quit)\n")
    if taask.lower() == "exit":
        break
    add_task(taask)
    print(f"Current Tasks: {tasks}")




while True:
    taask= input("Enter Your Tasks which you want to delete (or type 'exit' for quit)\n")
    if taask.lower() == "exit":
        break
    delete_tasks(taask)
    print(f"Current Tasks: {tasks}")