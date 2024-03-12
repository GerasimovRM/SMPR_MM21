import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from ui_main import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.push_button_for_reverse_names)

    def push_button_for_reverse_names(self):
        last_name = self.line_edit_last_name.text()[::-1]
        first_name = self.line_edit_first_name.text()[::-1]
        self.line_edit_first_name.setText(first_name)
        self.line_edit_last_name.setText(last_name)



app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
