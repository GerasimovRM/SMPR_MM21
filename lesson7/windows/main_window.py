from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog

from database import get_session, Actor
from ui import UiMainWindow
from .actor_create_window import ActorCreate
from .actor_update_window import ActorUpdate
from .dialog import Dialog


class MainWindow(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.create_window = None
        self.session = get_session()
        self.current_row = None

        self.push_button_create.clicked.connect(self.open_actor_create)
        self.tableWidget.cellDoubleClicked.connect(self.open_actor_update)
        self.push_button_delete.clicked.connect(self.open_dialog_delete_actor)
        self.tableWidget.cellClicked.connect(self.table_widget_cell_clicked)

        self.update_table()

    def update_table(self):
        actors = self.session.query(Actor).order_by(Actor.id).all()
        self.tableWidget.setRowCount(0)
        for actor in actors:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(actor.id)))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(actor.first_name))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(actor.last_name))
            self.tableWidget.setItem(row_position, 3, QTableWidgetItem(actor.middle_name if actor.middle_name else ""))
            self.tableWidget.setItem(row_position, 4, QTableWidgetItem(str(actor.bdate)))

    def table_widget_cell_clicked(self, row, column):
        self.current_row = row

    def open_actor_create(self):
        self.create_window = ActorCreate([self.updateTable])
        self.create_window.show()

    def open_actor_update(self, row, column):
        actor_id = int(self.tableWidget.item(row, 0).text())
        actor = self.session.query(Actor).get(actor_id)
        self.create_window = ActorUpdate(actor, [self.updateTable])
        self.create_window.show()

    def open_dialog_delete_actor(self):
        if self.current_row is None:
            return
        dialog_delete = Dialog("Точно хотите удалить??")
        ret_value = dialog_delete.exec_()
        if ret_value == QDialog.Accepted:
            actor_id = int(self.tableWidget.item(self.current_row, 0).text())
            actor = self.session.query(Actor).get(actor_id)
            self.session.delete(actor)
            self.session.commit()
            self.update_table()
