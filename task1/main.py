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
listbox = tk.Listbox(window,width=60, height=15,selectmode=tk.EXTENDED)
listbox.pack(pady=10)

#function to add,delete and complete task
def add_task():
    task =entry_task.get()
    if task:
        to_do.append(task)
        listbox.insert(tk.END,task)
        entry_task.delete(0,tk.END)
 
window.mainloop()