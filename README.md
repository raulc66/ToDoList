ToDoList

A simple desktop To-Do List application built with Python and PyQt5. This app allows you to manage tasks with categories, priorities, and due dates, with data stored locally in a JSON file.
Features

    Add tasks with description, category, priority, and due date.
    Mark tasks as completed.
    Delete tasks.
    Categories: Work, Personal, Urgent.
    Priority levels: Low, Medium, High.
    Calendar widget for due date selection.
    All tasks are saved in tasks.json.

Requirements

    Python 3.x
    PyQt5

Install dependencies with:
bash

pip install PyQt5

Usage

    Clone the repository:
    bash

git clone https://github.com/raulc66/ToDoList.git
cd ToDoList

Run the application:
bash

    python main.pyToDoList

A simple desktop To-Do List application built with Python and PyQt5. This app allows you to manage tasks with categories, priorities, and due dates, with data stored locally in a JSON file.
Features

    Add tasks with description, category, priority, and due date.
    Mark tasks as completed.
    Delete tasks.
    Categories: Work, Personal, Urgent.
    Priority levels: Low, Medium, High.
    Calendar widget for due date selection.
    All tasks are saved in tasks.json.

Requirements

    Python 3.x
    PyQt5

Install dependencies with:
bash

pip install PyQt5

Usage

    Clone the repository:
    bash

git clone https://github.com/raulc66/ToDoList.git
cd ToDoList

Run the application:
bash

    python main.py

    Use the GUI to add, complete, or delete tasks. All changes are saved to tasks.json automatically.

File Structure

    main.py – Main entry point; sets up and launches the application.
    ui_manager.py – Contains the PyQt5 UI and interaction logic.
    task_manager.py – Handles task logic (add, delete, complete, retrieve tasks).
    file_manager.py – Loads and saves tasks from/to tasks.json.

Notes

    Tasks are stored locally. Deleting or moving tasks.json will remove your tasks.
    Duplicate tasks (same description, category, priority, and due date) are not allowed.


    Use the GUI to add, complete, or delete tasks. All changes are saved to tasks.json automatically.

File Structure

    main.py – Main entry point; sets up and launches the application.
    ui_manager.py – Contains the PyQt5 UI and interaction logic.
    task_manager.py – Handles task logic (add, delete, complete, retrieve tasks).
    file_manager.py – Loads and saves tasks from/to tasks.json.

Notes

    Tasks are stored locally. Deleting or moving tasks.json will remove your tasks.
    Duplicate tasks (same description, category, priority, and due date) are not allowed.
