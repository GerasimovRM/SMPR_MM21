# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'from_designer/actor_create.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 293)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.line_edit_first_name = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_first_name.setObjectName("line_edit_first_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_edit_first_name)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.line_edit_last_name = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_last_name.setObjectName("line_edit_last_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_edit_last_name)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.line_edit_middle_name = QtWidgets.QLineEdit(self.groupBox)
        self.line_edit_middle_name.setObjectName("line_edit_middle_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_edit_middle_name)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.pushButton_ok = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.pushButton_ok)
        self.pushButton_cancel = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_cancel)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Создать актера"))
        self.label.setText(_translate("Form", "Фамилия"))
        self.label_2.setText(_translate("Form", "Имя"))
        self.label_3.setText(_translate("Form", "Отчество"))
        self.label_4.setText(_translate("Form", "Дата рождения"))
        self.pushButton_ok.setText(_translate("Form", "Сохранить"))
        self.pushButton_cancel.setText(_translate("Form", "Отмена"))
