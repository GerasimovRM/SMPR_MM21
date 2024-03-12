import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem

from ui_actor_table import Ui_MainWindow
from ui_actor_create import Ui_Form

from database import get_session, Actor


class ActorTable(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.push_button_create.clicked.connect(self.open_actor_create)

        session = get_session()
        actors = session.query(Actor).all()
        for actor in actors:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(actor.id)))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(actor.first_name))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(actor.last_name))
            self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(actor.middle_name if actor.middle_name else ""))
            self.tableWidget.setItem(rowPosition, 4, QTableWidgetItem(actor.bdate))

    def open_actor_create(self):
        self.create_window = ActorCreate()
        self.create_window.show()


class ActorCreate(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook



app = QApplication(sys.argv)
ex = ActorTable()
ex.show()
sys.exit(app.exec_())
