from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from database import get_session, Actor
from ui import UiMainWindow
from .actor_create_window import ActorCreate
from .actor_update_window import ActorUpdate


class MainWindow(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.push_button_create.clicked.connect(self.open_actor_create)
        self.tableWidget.cellDoubleClicked.connect(self.open_actor_update)
        self.session = get_session()
        self.updateTable()


    def updateTable(self):
        actors = self.session.query(Actor).order_by(Actor.id).all()
        self.tableWidget.setRowCount(0)
        for actor in actors:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(actor.id)))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(actor.first_name))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(actor.last_name))
            self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(actor.middle_name if actor.middle_name else ""))
            self.tableWidget.setItem(rowPosition, 4, QTableWidgetItem(str(actor.bdate)))

    def open_actor_create(self):
        self.create_window = ActorCreate([self.updateTable])
        self.create_window.show()

    def open_actor_update(self, row, column):
        actor_id = int(self.tableWidget.item(row, 0).text())
        actor = self.session.query(Actor).get(actor_id)
        self.create_window = ActorUpdate(actor, [self.updateTable])
        self.create_window.show()

