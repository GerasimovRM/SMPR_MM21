from typing import Iterable, Callable

from PyQt5.QtWidgets import QWidget

from database import get_session, Actor
from ui import UiActorCreateForm


class ActorCreate(QWidget, UiActorCreateForm):
    def __init__(self, callbacks: Iterable[Callable]):
        super().__init__()
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.pushButton_ok.clicked.connect(self.create_actor)
        self.pushButton_cancel.clicked.connect(lambda: self.close())

    def create_actor(self):
        first_name = self.line_edit_first_name.text()
        last_name = self.line_edit_last_name.text()
        middle_name = self.line_edit_middle_name.text()
        bdate = self.dateEdit.date().toPyDate()
        new_actor = Actor(first_name=first_name,
                          last_name=last_name,
                          middle_name=middle_name,
                          bdate=bdate)
        self.session.add(new_actor)
        self.session.commit()

        self.custom_close()

    def custom_close(self):
        for callback in self.callbacks:
            callback()
        self.close()



