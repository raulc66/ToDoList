import sys
from PyQt5.QtWidgets import QApplication

from ui_manager import TaskManager
import file_manager as fm

if __name__ == "__main__":
    app = QApplication(sys.argv)

    tasks = fm.load_tasks()

    window = TaskManager(tasks)
    window.show()

    app.exec()
    fm.save_tasks(window.get_tasks())