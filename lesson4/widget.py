import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from ui_widget import Ui_Form


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.push_ok)

    def push_ok(self):
        answer = []
        if self.radioButton_1_red.isChecked():
            answer.append("Красный")
        elif self.radioButton_1_blue.isChecked():
            answer.append("Синий")
        elif self.radioButton_1_green.isChecked():
            answer.append("Зеленый")

        if self.radioButton_2_red.isChecked():
            answer.append("Красный")
        elif self.radioButton_2_blue.isChecked():
            answer.append("Синий")
        elif self.radioButton_2_green.isChecked():
            answer.append("Зеленый")

        if self.radioButton_3_red.isChecked():
            answer.append("Красный")
        elif self.radioButton_3_blue.isChecked():
            answer.append("Синий")
        elif self.radioButton_3_green.isChecked():
            answer.append("Зеленый")

        self.label_answer.setText(", ".join(answer))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
