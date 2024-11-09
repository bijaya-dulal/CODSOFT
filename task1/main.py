import tkinter as tk

#initialise main window
window = tk.Tk()
window.title('TO-DO-List')
window.geometry('600x600')

#define a task list
to_do =[]

#task  input
entry_task =tk.Entry(window,width=40)
entry_task.pack(pady=10)


#list box to display task
listbox = tk.Listbox(window,width=60, height=15,selectmode=tk.SINGLE)
listbox.pack(pady=10)

#function to add,delete and complete task
def add_task():
    task =entry_task.get()
    if task:
        to_do.append(task)
        listbox.insert(tk.END,task)
        entry_task.delete(0,tk.END)

def  delete_task():
    selt_task_indx = listbox.curselection()
    if selt_task_indx:
        task_index = selt_task_indx[0]
        to_do.pop(task_index)
        listbox.delete(task_index)

def complete_task():
    selt_task_indx = listbox.curselection()
    if selt_task_indx:
        task_index =selt_task_indx[0]
        task = to_do[task_index]
        to_do[task_index] = f"{task} - Completed"
        listbox.delete(task_index)
        listbox.insert(task_index, to_do[task_index])



#buttons        
add_button = tk.Button(window, text="Add Task", width=10, command=add_task)
add_button.pack(pady=5)        
 
delete_button = tk.Button(window, text="delete task", width=10, command=delete_task)
delete_button.pack(pady=5)

complete_button = tk.Button(window, text="Complete Task", width=10, command=complete_task)
complete_button.pack(pady=5)

window.mainloop()