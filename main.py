import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from main_dialog import Ui_MainWindow
from connection import Data
from sqlalchemy import create_engine
from datetime import datetime
from new_animal import Ui_Dialog as Ui_AnimalDialog
from new_employee import Ui_Dialog as Ui_EmployeeDialog

class Zoo(QMainWindow):
    def __init__(self):
        super(Zoo, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()

        self.db = QSqlDatabase.addDatabase("QPSQL")

        self.db.setHostName("localhost")
        self.db.setDatabaseName("postgres")
        self.db.setUserName("postgres")
        self.db.setPassword("2005")
        self.db.setPort(5433)
        print("Available drivers:", QSqlDatabase.drivers())


        if not self.db.open():
            error_msg = self.db.lastError().text()
            print(f"Помилка підключення: {error_msg}")
            QMessageBox.critical(self, "Database Error", f"Помилка підключення до бази даних:\n{error_msg}")
            sys.exit(1)

        DATABASE_URL = "postgresql+psycopg2://postgres:2005@localhost:5433/postgres"
        engine = create_engine(DATABASE_URL)


        self.update_stat()
        self.view_data_Employee()
        self.view_data_Animal()

        self.ui.pushButton_Add_Animal.clicked.connect(self.open_new_animal)
        self.ui.pushButton_Delete_Animal.clicked.connect(self.delete_animal)
        self.ui.pushButton_Feed_Animal.clicked.connect(self.feed_animal)
        self.ui.pushButton_Add_Employee.clicked.connect(self.open_new_employee)
        self.ui.pushButton_Delete_Employee.clicked.connect(self.delete_employee)

    def update_stat(self):
        total_employees = self.conn.get_employee_count()
        total_animals = self.conn.get_animal_count()
        self.ui.label_All_Animals.setText(f"{total_animals}")
        self.ui.label_All_employees.setText(f"{total_employees}")

        animals_by_type = self.conn.get_animal_count_by_type()
        birds_count = animals_by_type.get("Bird", 0)
        raptors_count = animals_by_type.get("Raptor", 0)
        grazers_count = animals_by_type.get("Grazer", 0)

        employees_by_type = self.conn.get_employee_count_by_type()
        cleaners_count = employees_by_type.get("Cleaner", 0)
        feeders_count = employees_by_type.get("Feeder", 0)

        self.ui.label_Birds.setText(f"{birds_count}")
        self.ui.label_Rantors.setText(f"{raptors_count}")
        self.ui.label_Grazers.setText(f"{grazers_count}")

        self.ui.label_Cleaners.setText(f"{cleaners_count}")
        self.ui.label_Feeders.setText(f"{feeders_count}")
    def open_new_employee(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_EmployeeDialog()
        self.ui_window.setupUi(self.new_window)
        self.ui_window.pushButton_Add_Employee_Dialoge.clicked.connect(self.add_new_employee)
        self.new_window.exec()  

    def open_new_animal(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_AnimalDialog()
        self.ui_window.setupUi(self.new_window)
        self.ui_window.pushButton_Add_Animal_Dialog.clicked.connect(self.add_new_animal)
        self.new_window.exec()

    def add_new_employee(self):
        type_employee = self.ui_window.comboBox_Employee.currentText()
        first_name = self.ui_window.lineEdit_First_Name.text()
        last_name = self.ui_window.lineEdit_Last_Name.text()
        birthday = self.ui_window.dateEdit_Edit_Employee.date().toString("yyyy-MM-dd")
        phone_email = self.ui_window.lineEdit_Phone_Email.text()

        if not (first_name and last_name and phone_email):
            QMessageBox.warning(self, "Помилка", "Всі поля мають бути заповнені!")
            return

        self.conn.add_new_employee(type_employee, first_name, last_name, birthday, phone_email)
        self.view_data_Employee()
        self.update_stat()
        self.new_window.close()

    def add_new_animal(self):
        name = self.ui_window.lineEdit_Name_Animal.text()
        animal_type = self.ui_window.comboBox.currentText() 
        birthday = self.ui_window.dateEdit_Animal.date().toString("yyyy-MM-dd")
        type_of_animal = self.ui_window.lineEdit_Type_Animal.text()
        feed = self.ui_window.comboBox_2.currentText()

        if not name or not type_of_animal:
            QMessageBox.warning(self, "Помилка", "Всі поля мають бути заповнені!")
            return

        self.conn.add_new_animal(name, animal_type, birthday, type_of_animal, feed)
        self.view_data_Animal()
        self.update_stat()
        self.new_window.close()

    def view_data_Employee(self):
        self.model_employee = QSqlTableModel(self, self.db)
        self.model_employee.setTable("employee")
        self.model_employee.select()
        self.ui.tableView_Employee.setModel(self.model_employee)


    def view_data_Animal(self):
        self.model_animal = QSqlTableModel(self, self.db)
        self.model_animal.setTable("animal")
        self.model_animal.select()
        self.ui.tableView_Animal.setModel(self.model_animal)

    def delete_employee(self):
        index = self.ui.tableView_Employee.selectionModel().currentIndex()
        if not index.isValid():
            QMessageBox.warning(self, "Видалення", "Виберіть співробітника для видалення!")
            return

        id = self.model_employee.data(self.model_employee.index(index.row(), 0))
        self.conn.delete_employee(id)
        self.update_stat()
        self.view_data_Employee()

    def delete_animal(self):
        index = self.ui.tableView_Animal.selectionModel().currentIndex()
        if not index.isValid():
            QMessageBox.warning(self, "Видалення", "Виберіть тварину для видалення!")
            return

        id = self.model_animal.data(self.model_animal.index(index.row(), 0))
        self.conn.delete_animal(id)
        self.update_stat()
        self.view_data_Animal()

    def feed_animal(self):
        index = self.ui.tableView_Animal.selectionModel().currentIndex()
        if not index.isValid():
            QMessageBox.warning(self, "Годування", "Виберіть тварину для годування!")
            return

        id = self.model_animal.data(self.model_animal.index(index.row(), 0))
        self.conn.feed_animal(id)
        self.view_data_Animal()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Zoo()
    window.show()
    sys.exit(app.exec())
