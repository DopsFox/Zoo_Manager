# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)
import res_icon_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1079, 585)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(212, 15, 7, 255), stop:1 rgba(0, 97, 97, 255))")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(460, 10, 134, 271))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Add_Employee = QPushButton(self.widget)
        self.pushButton_Add_Employee.setObjectName(u"pushButton_Add_Employee")
        self.pushButton_Add_Employee.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_3.addWidget(self.pushButton_Add_Employee)

        self.pushButton_Delete_Employee = QPushButton(self.widget)
        self.pushButton_Delete_Employee.setObjectName(u"pushButton_Delete_Employee")
        self.pushButton_Delete_Employee.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_3.addWidget(self.pushButton_Delete_Employee)

        self.pushButton_Add_Animal = QPushButton(self.widget)
        self.pushButton_Add_Animal.setObjectName(u"pushButton_Add_Animal")
        self.pushButton_Add_Animal.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_3.addWidget(self.pushButton_Add_Animal)

        self.pushButton_Delete_Animal = QPushButton(self.widget)
        self.pushButton_Delete_Animal.setObjectName(u"pushButton_Delete_Animal")
        self.pushButton_Delete_Animal.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_3.addWidget(self.pushButton_Delete_Animal)

        self.pushButton_Feed_Animal = QPushButton(self.widget)
        self.pushButton_Feed_Animal.setObjectName(u"pushButton_Feed_Animal")
        self.pushButton_Feed_Animal.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_3.addWidget(self.pushButton_Feed_Animal)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(600, 10, 471, 271))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_Icon_Animals = QLabel(self.widget1)
        self.label_Icon_Animals.setObjectName(u"label_Icon_Animals")
        self.label_Icon_Animals.setPixmap(QPixmap(u":/icon/Icons/emoji_nature_40dp_E8EAED_FILL0_wght400_GRAD0_opsz40.svg"))

        self.horizontalLayout_4.addWidget(self.label_Icon_Animals)

        self.label_All_Animals_2 = QLabel(self.widget1)
        self.label_All_Animals_2.setObjectName(u"label_All_Animals_2")

        self.horizontalLayout_4.addWidget(self.label_All_Animals_2)

        self.label_All_Animals = QLabel(self.widget1)
        self.label_All_Animals.setObjectName(u"label_All_Animals")

        self.horizontalLayout_4.addWidget(self.label_All_Animals)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_Icon_Animals_2 = QLabel(self.widget1)
        self.label_Icon_Animals_2.setObjectName(u"label_Icon_Animals_2")
        self.label_Icon_Animals_2.setPixmap(QPixmap(u":/icon/Icons/raven_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_5.addWidget(self.label_Icon_Animals_2)

        self.label_Birds_2 = QLabel(self.widget1)
        self.label_Birds_2.setObjectName(u"label_Birds_2")

        self.horizontalLayout_5.addWidget(self.label_Birds_2)

        self.label_Birds = QLabel(self.widget1)
        self.label_Birds.setObjectName(u"label_Birds")

        self.horizontalLayout_5.addWidget(self.label_Birds)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_Icon_Animals_3 = QLabel(self.widget1)
        self.label_Icon_Animals_3.setObjectName(u"label_Icon_Animals_3")
        self.label_Icon_Animals_3.setPixmap(QPixmap(u":/icon/Icons/pets_40dp_E8EAED_FILL0_wght400_GRAD0_opsz40.svg"))

        self.horizontalLayout_6.addWidget(self.label_Icon_Animals_3)

        self.label_Rantors_2 = QLabel(self.widget1)
        self.label_Rantors_2.setObjectName(u"label_Rantors_2")

        self.horizontalLayout_6.addWidget(self.label_Rantors_2)

        self.label_Rantors = QLabel(self.widget1)
        self.label_Rantors.setObjectName(u"label_Rantors")

        self.horizontalLayout_6.addWidget(self.label_Rantors)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_Icon_Animals_4 = QLabel(self.widget1)
        self.label_Icon_Animals_4.setObjectName(u"label_Icon_Animals_4")
        self.label_Icon_Animals_4.setPixmap(QPixmap(u":/icon/Icons/cruelty_free_40dp_E8EAED_FILL0_wght400_GRAD0_opsz40.svg"))

        self.horizontalLayout_7.addWidget(self.label_Icon_Animals_4)

        self.label_Grazers_2 = QLabel(self.widget1)
        self.label_Grazers_2.setObjectName(u"label_Grazers_2")

        self.horizontalLayout_7.addWidget(self.label_Grazers_2)

        self.label_Grazers = QLabel(self.widget1)
        self.label_Grazers.setObjectName(u"label_Grazers")

        self.horizontalLayout_7.addWidget(self.label_Grazers)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 10, 441, 271))
        self.verticalLayout = QVBoxLayout(self.widget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_icon_enployees = QLabel(self.widget2)
        self.label_icon_enployees.setObjectName(u"label_icon_enployees")
        self.label_icon_enployees.setPixmap(QPixmap(u":/icon/Icons/person_apron_40dp_E8EAED_FILL0_wght400_GRAD0_opsz40.svg"))

        self.horizontalLayout_3.addWidget(self.label_icon_enployees)

        self.label_All_employees_2 = QLabel(self.widget2)
        self.label_All_employees_2.setObjectName(u"label_All_employees_2")

        self.horizontalLayout_3.addWidget(self.label_All_employees_2)

        self.label_All_employees = QLabel(self.widget2)
        self.label_All_employees.setObjectName(u"label_All_employees")

        self.horizontalLayout_3.addWidget(self.label_All_employees)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_icon_enployees_2 = QLabel(self.widget2)
        self.label_icon_enployees_2.setObjectName(u"label_icon_enployees_2")
        self.label_icon_enployees_2.setPixmap(QPixmap(u":/icon/Icons/household_supplies_40dp_E8EAED_FILL0_wght400_GRAD0_opsz40.svg"))

        self.horizontalLayout_2.addWidget(self.label_icon_enployees_2)

        self.label_Cleaners_2 = QLabel(self.widget2)
        self.label_Cleaners_2.setObjectName(u"label_Cleaners_2")

        self.horizontalLayout_2.addWidget(self.label_Cleaners_2)

        self.label_Cleaners = QLabel(self.widget2)
        self.label_Cleaners.setObjectName(u"label_Cleaners")

        self.horizontalLayout_2.addWidget(self.label_Cleaners)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_icon_enployees_3 = QLabel(self.widget2)
        self.label_icon_enployees_3.setObjectName(u"label_icon_enployees_3")
        self.label_icon_enployees_3.setPixmap(QPixmap(u":/icon/Icons/restaurant_40dp_E8EAED_FILL0_wght400_GRAD0_opsz40.svg"))

        self.horizontalLayout.addWidget(self.label_icon_enployees_3)

        self.label_Feeders_2 = QLabel(self.widget2)
        self.label_Feeders_2.setObjectName(u"label_Feeders_2")

        self.horizontalLayout.addWidget(self.label_Feeders_2)

        self.label_Feeders = QLabel(self.widget2)
        self.label_Feeders.setObjectName(u"label_Feeders")

        self.horizontalLayout.addWidget(self.label_Feeders)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.widget3 = QWidget(self.centralwidget)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 290, 1061, 291))
        self.horizontalLayout_8 = QHBoxLayout(self.widget3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.tableView_Employee = QTableView(self.widget3)
        self.tableView_Employee.setObjectName(u"tableView_Employee")
        self.tableView_Employee.setStyleSheet(u"QTableView:{\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radios:7px;\n"
"}\n"
"QTableView:: section{\n"
"background-color: rgba(53,53,53);\n"
"color:white;\n"
"border:none;\n"
"height:50px;\n"
"font-size:14pt;\n"
"}\n"
"QTableView::item{\n"
"border-stele:none;\n"
"border-bottom: rgba(255,255,255,50)\n"
"}\n"
"QTableView::item:selected{\n"
"border-stele:none;\n"
"color:rgba(255,255,255);\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"")
        self.tableView_Employee.setShowGrid(False)

        self.horizontalLayout_8.addWidget(self.tableView_Employee)

        self.tableView_Animal = QTableView(self.widget3)
        self.tableView_Animal.setObjectName(u"tableView_Animal")
        self.tableView_Animal.setStyleSheet(u"QTableView:{\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-left-radios:7px;\n"
"}\n"
"QTableView:: section{\n"
"background-color: rgba(53,53,53);\n"
"color:white;\n"
"border:none;\n"
"height:50px;\n"
"font-size:14pt;\n"
"}\n"
"QTableView::item{\n"
"border-stele:none;\n"
"border-bottom: rgba(255,255,255,50)\n"
"}\n"
"QTableView::item:selected{\n"
"border-stele:none;\n"
"color:rgba(255,255,255);\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.tableView_Animal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_Add_Employee.setText(QCoreApplication.translate("MainWindow", u"AddEmployee", None))
        self.pushButton_Delete_Employee.setText(QCoreApplication.translate("MainWindow", u"DeleteEmployee", None))
        self.pushButton_Add_Animal.setText(QCoreApplication.translate("MainWindow", u"Add_Animal", None))
        self.pushButton_Delete_Animal.setText(QCoreApplication.translate("MainWindow", u"DeleteAnimal", None))
        self.pushButton_Feed_Animal.setText(QCoreApplication.translate("MainWindow", u"FeedAnimal", None))
        self.label_Icon_Animals.setText("")
        self.label_All_Animals_2.setText(QCoreApplication.translate("MainWindow", u"All_Animals", None))
        self.label_All_Animals.setText("")
        self.label_Icon_Animals_2.setText("")
        self.label_Birds_2.setText(QCoreApplication.translate("MainWindow", u"Birds", None))
        self.label_Birds.setText("")
        self.label_Icon_Animals_3.setText("")
        self.label_Rantors_2.setText(QCoreApplication.translate("MainWindow", u"Raptors", None))
        self.label_Rantors.setText(QCoreApplication.translate("MainWindow", u"Raptors", None))
        self.label_Icon_Animals_4.setText("")
        self.label_Grazers_2.setText(QCoreApplication.translate("MainWindow", u"Grazers", None))
        self.label_Grazers.setText(QCoreApplication.translate("MainWindow", u"Grazers", None))
        self.label_icon_enployees.setText("")
        self.label_All_employees_2.setText(QCoreApplication.translate("MainWindow", u"All_Employees", None))
        self.label_All_employees.setText("")
        self.label_icon_enployees_2.setText("")
        self.label_Cleaners_2.setText(QCoreApplication.translate("MainWindow", u"Cleaners", None))
        self.label_Cleaners.setText("")
        self.label_icon_enployees_3.setText("")
        self.label_Feeders_2.setText(QCoreApplication.translate("MainWindow", u"Feeders", None))
        self.label_Feeders.setText("")
    # retranslateUi

