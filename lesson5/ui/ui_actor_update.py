# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'from_designer/actor_update.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(632, 349)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.line_edit_last_name = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_last_name.setObjectName("line_edit_last_name")
        self.gridLayout.addWidget(self.line_edit_last_name, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_id = QtWidgets.QLabel(self.groupBox)
        self.label_id.setText("")
        self.label_id.setObjectName("label_id")
        self.gridLayout.addWidget(self.label_id, 0, 1, 1, 1)
        self.pushButton_cancel = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.line_edit_middle_name = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_middle_name.setObjectName("line_edit_middle_name")
        self.gridLayout.addWidget(self.line_edit_middle_name, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.line_edit_first_name = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_first_name.setObjectName("line_edit_first_name")
        self.gridLayout.addWidget(self.line_edit_first_name, 1, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 4, 1, 1, 1)
        self.pushButton_ok = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.gridLayout.addWidget(self.pushButton_ok, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Создать актера"))
        self.label_3.setText(_translate("Form", "Отчество"))
        self.label_4.setText(_translate("Form", "Дата рождения"))
        self.pushButton_cancel.setText(_translate("Form", "Отмена"))
        self.label_5.setText(_translate("Form", "id"))
        self.label.setText(_translate("Form", "Фамилия"))
        self.label_2.setText(_translate("Form", "Имя"))
        self.pushButton_ok.setText(_translate("Form", "Обновить"))
