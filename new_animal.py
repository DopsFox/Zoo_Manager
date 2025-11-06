# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_animal.ui'
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
        Dialog.resize(514, 527)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(212, 15, 7, 255), stop:1 rgba(0, 97, 97, 255));")
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(80, 140, 341, 61))
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(80, 210, 341, 41))
        self.pushButton_Add_Animal_Dialog = QPushButton(Dialog)
        self.pushButton_Add_Animal_Dialog.setObjectName(u"pushButton_Add_Animal_Dialog")
        self.pushButton_Add_Animal_Dialog.setGeometry(QRect(180, 413, 131, 51))
        self.pushButton_Add_Animal_Dialog.setStyleSheet(u"QPushButton{\n"
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
        self.widget.setGeometry(QRect(160, 0, 171, 131))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_Icon_Animals = QLabel(self.widget)
        self.label_Icon_Animals.setObjectName(u"label_Icon_Animals")
        self.label_Icon_Animals.setPixmap(QPixmap(u":/icon/Icons/emoji_nature_40dp_E8EAED_FILL0_wght400_GRAD0_opsz40.svg"))

        self.verticalLayout.addWidget(self.label_Icon_Animals)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.widget1 = QWidget(Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 260, 471, 141))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_Name_Animal = QLineEdit(self.widget1)
        self.lineEdit_Name_Animal.setObjectName(u"lineEdit_Name_Animal")

        self.horizontalLayout_4.addWidget(self.lineEdit_Name_Animal)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_Type_Animal = QLineEdit(self.widget1)
        self.lineEdit_Type_Animal.setObjectName(u"lineEdit_Type_Animal")

        self.horizontalLayout_3.addWidget(self.lineEdit_Type_Animal)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.dateEdit_Animal = QDateEdit(self.widget1)
        self.dateEdit_Animal.setObjectName(u"dateEdit_Animal")

        self.horizontalLayout_2.addWidget(self.dateEdit_Animal)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.lineEdit_ID_Animal = QLineEdit(self.widget1)
        self.lineEdit_ID_Animal.setObjectName(u"lineEdit_ID_Animal")

        self.horizontalLayout.addWidget(self.lineEdit_ID_Animal)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        self.comboBox.setCurrentIndex(-1)
        self.comboBox_2.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Bird", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Raptor", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Grazers", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"Hungry", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"Fed", None))

        self.pushButton_Add_Animal_Dialog.setText(QCoreApplication.translate("Dialog", u"Add_Animal", None))
        self.label_Icon_Animals.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"New_Amimal", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0434", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430\u041d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"ID", None))
    # retranslateUi

