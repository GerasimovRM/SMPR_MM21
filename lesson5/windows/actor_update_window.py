from typing import Iterable, Callable

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget

from database import get_session, Actor
from ui import UiActorUpdateForm


class ActorUpdate(QWidget, UiActorUpdateForm):
    def __init__(self, actor: Actor, callbacks: Iterable[Callable]):
        super().__init__()
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.pushButton_ok.clicked.connect(self.update_actor)
        self.pushButton_cancel.clicked.connect(lambda: self.close())

        self.label_id.setText(str(actor.id))
        self.line_edit_first_name.setText(actor.first_name)
        self.line_edit_last_name.setText(actor.last_name)
        self.line_edit_middle_name.setText(actor.middle_name)
        self.dateEdit.setDate(QDate.fromString(str(actor.bdate)))

    def update_actor(self):
        # TODO: красиво?
        first_name = self.line_edit_first_name.text()
        last_name = self.line_edit_last_name.text()
        middle_name = self.line_edit_middle_name.text()
        bdate = self.dateEdit.date().toPyDate()
        actor_id = int(self.label_id.text())
        exist_actor: Actor = self.session.query(Actor).get(actor_id)
        exist_actor.first_name = first_name
        exist_actor.last_name = last_name
        exist_actor.middle_name = middle_name
        exist_actor.bdate = bdate
        self.session.commit()

        self.custom_close()

    def custom_close(self):
        for callback in self.callbacks:
            callback()
        self.close()



