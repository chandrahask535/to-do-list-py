import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = []

        self.task_label = tk.Label(root, text="Task:")
        self.task_label.pack()
        
        self.task_entry = tk.Entry(root, width=90)
        self.task_entry.pack()

        self.priority_label = tk.Label(root, text="Priority:")
        self.priority_label.pack()
        
        self.priority_entry = tk.Entry(root, width=90)
        self.priority_entry.pack()

        self.due_date_label = tk.Label(root, text="Due Date:")
        self.due_date_label.pack()
        
        self.due_date_entry = tk.Entry(root, width=90)
        self.due_date_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_list = tk.Listbox(root, selectmode=tk.SINGLE, width=105)
        self.task_list.pack()

        self.mark_complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.mark_complete_button.pack()

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_entry.get()
        due_date = self.due_date_entry.get()
        status = "Pending"  # Default status

        if task:
            task_details = f"Task: {task}, Priority: {priority}, Due Date: {due_date}, Status: {status}"
            self.tasks.append(task_details)
            self.task_list.insert(tk.END, task_details)
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Task description cannot be empty.")

    def mark_complete(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            task_details = self.tasks[index]
            if "Status: Pending" in task_details:
                task_details = task_details.replace("Status: Pending", "Status: Completed")
                self.tasks[index] = task_details
                self.task_list.delete(index)
                self.task_list.insert(index, task_details)
        else:
            messagebox.showerror("Error", "Please select a task to mark as complete.")

    def update_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.task_entry.get()
            priority = self.priority_entry.get()
            due_date = self.due_date_entry.get()
            status = "Pending"  # Default status
            
            if task:
                task_details = f"Task: {task}, Priority: {priority}, Due Date: {due_date}, Status: {status}"
                self.tasks[index] = task_details
                self.task_list.delete(index)
                self.task_list.insert(index, task_details)
                self.clear_entries()
            else:
                messagebox.showerror("Error", "Task description cannot be empty.")
        else:
            messagebox.showerror("Error", "Please select a task to update.")

    def remove_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            self.task_list.delete(index)
            del self.tasks[index]
        else:
            messagebox.showerror("Error", "Please select a task to remove.")

    def clear_entries(self):
        self.task_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
