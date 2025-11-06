# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_employee.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import res_icon_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(516, 497)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(212, 15, 7, 255), stop:1 rgba(0, 97, 97, 255));")
        self.comboBox_Employee = QComboBox(Dialog)
        self.comboBox_Employee.addItem("")
        self.comboBox_Employee.addItem("")
        self.comboBox_Employee.setObjectName(u"comboBox_Employee")
        self.comboBox_Employee.setGeometry(QRect(80, 150, 361, 81))
        self.pushButton_Add_Employee_Dialoge = QPushButton(Dialog)
        self.pushButton_Add_Employee_Dialoge.setObjectName(u"pushButton_Add_Employee_Dialoge")
        self.pushButton_Add_Employee_Dialoge.setGeometry(QRect(190, 390, 151, 41))
        self.pushButton_Add_Employee_Dialoge.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:130px;\n"
"height:40px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 233, 461, 131))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color:white;\n"
"front-weight:bold;\n"
"front-size:20pt;\n"
"backdround-color:none;\n"
"border:none;")

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit_First_Name = QLineEdit(self.widget)
        self.lineEdit_First_Name.setObjectName(u"lineEdit_First_Name")

        self.horizontalLayout.addWidget(self.lineEdit_First_Name)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color:white;\n"
"front-weight:bold;\n"
"front-size:20pt;\n"
"backdround-color:none;\n"
"border:none;")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_Last_Name = QLineEdit(self.widget)
        self.lineEdit_Last_Name.setObjectName(u"lineEdit_Last_Name")

        self.horizontalLayout_2.addWidget(self.lineEdit_Last_Name)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color:white;\n"
"front-weight:bold;\n"
"front-size:20pt;\n"
"backdround-color:none;\n"
"border:none;")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.dateEdit_Edit_Employee = QDateEdit(self.widget)
        self.dateEdit_Edit_Employee.setObjectName(u"dateEdit_Edit_Employee")

        self.horizontalLayout_3.addWidget(self.dateEdit_Edit_Employee)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.lineEdit_Phone_Email = QLineEdit(self.widget)
        self.lineEdit_Phone_Email.setObjectName(u"lineEdit_Phone_Email")

        self.horizontalLayout_4.addWidget(self.lineEdit_Phone_Email)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.widget1 = QWidget(Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(160, 0, 181, 141))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_icon_enployees = QLabel(self.widget1)
        self.label_icon_enployees.setObjectName(u"label_icon_enployees")
        self.label_icon_enployees.setPixmap(QPixmap(u":/icon/Icons/person_apron_40dp_E8EAED_FILL0_wght400_GRAD0_opsz40.svg"))

        self.verticalLayout_2.addWidget(self.label_icon_enployees)

        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color:white;\n"
"front-weight:bold;\n"
"front-size:20pt;\n"
"backdround-color:none;\n"
"border:none;")

        self.verticalLayout_2.addWidget(self.label)


        self.retranslateUi(Dialog)

        self.comboBox_Employee.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.comboBox_Employee.setItemText(0, QCoreApplication.translate("Dialog", u"Cleaner", None))
        self.comboBox_Employee.setItemText(1, QCoreApplication.translate("Dialog", u"Feeder", None))

        self.pushButton_Add_Employee_Dialoge.setText(QCoreApplication.translate("Dialog", u"Add_Employee", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0406\u043c'\u044f", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0424\u0430\u043c\u0456\u043b\u0456\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430\u041d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d/\u043f\u043e\u0448\u0442\u0430", None))
        self.label_icon_enployees.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"New_Employee", None))
    # retranslateUi

