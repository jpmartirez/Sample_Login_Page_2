
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from logindesign import Ui_Login

class MainApp(QWidget, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())