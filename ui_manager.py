from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QListWidget, QPushButton, QLineEdit, QComboBox, QCalendarWidget, QMessageBox
from PyQt5.QtCore import QDate
from task_manager import TaskManagerLogic

class TaskManager(QMainWindow):
    def __init__(self,tasks):
        super().__init__()
        self.setWindowTitle('Task Manager')
        self.setGeometry(100, 100, 600, 400)
        
        #Task Manager Logic
        self.logic = TaskManagerLogic(tasks)

        # Main widget and layout

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Task List

        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)
        self.load_tasks_to_ui()

        # Task Input

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText('Enter task description ...')
        self.layout.addWidget(self.task_input)

        # Category Dropdown Menu

        self.category_dropdown = QComboBox(self)
        self.category_dropdown.addItems(["Work", "Personal", "Urgent"])
        self.layout.addWidget(self.category_dropdown)

        # Priority Dropdown Menu

        self.priority_dropdown = QComboBox(self)
        self.priority_dropdown.addItems(["Low", "Medium", "High"])
        self.layout.addWidget(self.priority_dropdown)

        # Due Date Picker (Calendar)

        self.calendar_widget = QCalendarWidget(self)
        self.layout.addWidget(self.calendar_widget)

        # Add Task Button

        self.add_task_button = QPushButton('Add Task', self)
        self.add_task_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_task_button)

        # Complete and Delete Buttons

        self.complete_button = QPushButton('Complete Task', self)
        self.complete_button.clicked.connect(self.complete_task)
        self.layout.addWidget(self.complete_button)

        self.delete_button = QPushButton('Delete Task', self)
        self.delete_button.clicked.connect(self.delete_task)
        self.layout.addWidget(self.delete_button)

    def load_tasks_to_ui(self):
        self.task_list.clear()
        tasks = self.logic.get_tasks()
        for task in tasks:
            task_item = f"{task['description']} | {task['category']} | {task['priority']} | Due: {task['due_date']} | {'✓' if task ['completed'] else '✗' }"
            self.task_list.addItem(task_item)

    def add_task(self):
        description = self.task_input.text()
        category = self.category_dropdown.currentText()
        priority = self.priority_dropdown.currentText()
        due_date = self.calendar_widget.selectedDate().toString()

        if description:
            if self.logic.add_task(description, category, priority, due_date):
                self.load_tasks_to_ui()
            else:
                QMessageBox.warning(self, "Warning", "This task already exists !")

    def complete_task(self):
        selected_task_index = self.task_list.currentRow()
        if selected_task_index >= 0:
            if self.logic.complete_task(selected_task_index):
                self.load_tasks_to_ui()
            else:
                QMessageBox.warning(self, "Warning", "Task is already completed !")

    def delete_task(self):
        selected_task_index = self.task_list.currentRow()
        if selected_task_index >= 0:
            self.logic.delete_task(selected_task_index)
            self.load_tasks_to_ui()


    def get_tasks(self):
        print("Ok")
        return self.logic.get_tasks()            
    
    