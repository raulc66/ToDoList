import tkinter as tk
import task_manager as tm
import file_manager as fm
from tkinter import messagebox, Listbox, Scrollbar


# Main Application Class for Task Management GUI
class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        # Load tasks from file using task_manager
        tm.load_tasks(fm)

        # Create Input Field
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)

        # Add Task Button
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        # Complete Task Button
        self.complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(pady=5)

        # Delete Task Button
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Task Listbox to display tasks
        self.task_list = Listbox(self.root, width=50, height=10)
        self.task_list.pack(pady=10)

        # Scrollbar for Listbox
        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_list.yview)

        # Initially load tasks into the list
        self.update_task_list()

        # Save tasks when closing the window
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        """Add a new task."""
        task_description = self.entry.get()
        try:
            tm.add_task(task_description)
            self.update_task_list()
            self.entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showwarning("Warning", str(e))

    def delete_task(self):
        """Delete the selected task."""
        try:
            selected_task_index = self.task_list.curselection()[0]
            tm.delete_task(selected_task_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")
        except ValueError as e:
            messagebox.showwarning("Warning", str(e))

    def complete_task(self):
    
        try:
            # Get the selected task index from the listbox
            selected_task_index = self.task_list.curselection()[0]

            # Get the selected task from task_manager
            task = tm.get_tasks()[selected_task_index]

            # Check if the task is already completed
            if task["completed"]:
                messagebox.showwarning("Warning", "This task is already marked as completed.")
            else:
                # Mark the task as completed
                tm.complete_task(selected_task_index)
                self.update_task_list()

        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def update_task_list(self):
        """Update the Listbox with current tasks."""
        self.task_list.delete(0, tk.END)  # Clear the current list
        for task in tm.get_tasks():
            status = "✓" if task["completed"] else "✗"
            self.task_list.insert(tk.END, f"{task['task']} [{status}]")

    def on_closing(self):
        """Handle window close event."""
        tm.save_tasks(fm)  # Save tasks before closing
        self.root.destroy()


# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
