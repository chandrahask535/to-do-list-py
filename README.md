# motioncut-task1
To-do-List Application using Python programming Language

# README: To Do List (TASK 1)

## Author: CHANDRAHAS K

## Batch:(5th NOVEMBER- 5th DECEMBER)

## Domain: PYTHON Programming

## Aim

The aim of this project is to build a To-Do List Application

## Description

This application allows users to add tasks, mark tasks as completed, update task descriptions, and remove tasks from the list. This has been implemented in a graphical user interface (GUI).

## Libraries Used

The following important libraries were used for this project:

- tkinter
- messagebox from tkinter

  ## Working of the Code 

1. **Overview:**
   - This script is a simple To-Do List application implemented using the Tkinter library in Python.
   - The application provides a graphical user interface (GUI) for users to manage their tasks.

2. **Class Structure:**
   - The main class is `TodoListApp`, which is responsible for setting up the Tkinter GUI and managing the To-Do list operations.
   - It initializes the main window (`root`) and sets up various widgets such as labels, entry fields, buttons, and a listbox.

3. **To-Do List Management:**
   - The To-Do list is stored in the `self.tasks` list, where each task is represented as a formatted string containing task details, priority, due date, and status.
   - Tasks are displayed in a Tkinter Listbox widget for easy viewing and selection.

4. **Adding a Task:**
   - Users can add a new task by entering task details, priority, and due date in the corresponding entry fields and clicking the "Add Task" button.
   - If the task description is empty, an error message is displayed using `messagebox`.

5. **Marking a Task as Complete:**
   - Users can select a task from the list and mark it as complete by clicking the "Mark Complete" button.
   - The status of the selected task is updated from "Pending" to "Completed" in both the list and the underlying data structure.

6. **Updating a Task:**
   - Users can update the details of a selected task by modifying the task description, priority, and due date in the entry fields and clicking the "Update Task" button.
   - An error message is displayed if the task description is empty or if no task is selected.

7. **Removing a Task:**
   - Users can remove a selected task by clicking the "Remove Task" button.
   - An error message is displayed if no task is selected.

8. **Clearing Entry Fields:**
   - The `clear_entries` method is used to clear the entry fields after adding or updating a task.

9. **Main Execution:**
   - The script creates an instance of the `TodoListApp` class and starts the Tkinter main loop using `root.mainloop()`.

10. **Usage:**
   - Users can run the script to launch the To-Do List application, interact with the GUI, and manage their tasks.
