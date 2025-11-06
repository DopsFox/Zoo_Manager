from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

DATABASE_URL = "postgresql://postgres:2005@localhost:5433/postgres"

engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
Session = scoped_session(sessionmaker(bind=engine))

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type_employee = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birthday = Column(Date, nullable=False)
    phone_email = Column(String, nullable=False)

class Animal(Base):
    __tablename__ = "animal"
    id_animal = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    animal_type = Column(String, nullable=False)
    birthday = Column(Date, nullable=False)
    type_of_animal = Column(String, nullable=False)
    feed = Column(String, nullable=False)

Base.metadata.create_all(engine)

class Data:
    def __init__(self):
        self.session = Session()
        self.Employee = Employee
        self.Animal = Animal
        self.connection = engine.raw_connection()

    def execute_query(self, query, params=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params or ())
                result = cursor.fetchall()
            self.connection.commit()
            return result
        except Exception as e:
            logging.error(f"Помилка при виконанні запиту: {e}")
            return []

    def get_employee_count(self):
        query = "SELECT COUNT(*) FROM employee"
        result = self.execute_query(query)
        return result[0][0] if result else 0

    def get_employee_count_by_type(self):
        query = "SELECT type_employee, COUNT(*) FROM employee GROUP BY type_employee"
        result = self.execute_query(query)
        return {row[0]: row[1] for row in result}

    def get_animal_count(self):
        query = "SELECT COUNT(*) FROM animal"
        result = self.execute_query(query)
        return result[0][0] if result else 0

    def get_animal_count_by_type(self):
        query = "SELECT animal_type, COUNT(*) FROM animal GROUP BY animal_type"  # 🔹 Оновлено
        result = self.execute_query(query)
        return {row[0]: row[1] for row in result}

    def execute_query(self, query, params=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params or ())
                result = cursor.fetchall()
            self.connection.commit()
            return result
        except Exception as e:
            logging.error(f"Помилка при виконанні запиту: {e}")
            return []

    def add_new_employee(self, type_employee, first_name, last_name, birthday, phone_email):
        try:
            new_employee = Employee(
                type_employee=type_employee,
                first_name=first_name,
                last_name=last_name,
                birthday=birthday,
                phone_email=phone_email
            )
            self.session.add(new_employee)
            self.session.commit()
            logging.info(f"Додано співробітника: {first_name} {last_name}")
        except Exception as e:
            logging.error(f"Помилка при додаванні співробітника: {e}")

    def delete_employee(self, id):
        try:
            employee = self.session.query(self.Employee).filter(self.Employee.id == id).first()
            if employee:
                self.session.delete(employee)
                self.session.commit()
                logging.info(f"Видалено співробітника ID {id}")
            else:
                logging.warning(f"Не знайдено співробітника з ID {id}")
        except Exception as e:
            logging.error(f"Помилка при видаленні співробітника: {e}")

    def add_new_animal(self, name, animal_type, birthday, type_of_animal, feed):
        try:
            new_animal = self.Animal(
                name=name,
                animal_type=animal_type,
                birthday=birthday,
                type_of_animal=type_of_animal,
                feed=feed
            )
            self.session.add(new_animal)
            self.session.commit()
            logging.info(f"Додано тварину: {name}")
        except Exception as e:
            logging.error(f"Помилка при додаванні тварини: {e}")

    def delete_animal(self, id):
        try:
            self.session.query(self.Animal).filter(self.Animal.id_animal == id).delete()
            self.session.commit()
            logging.info(f"Видалено тварину ID {id}")
        except Exception as e:
            logging.error(f"Помилка при видаленні тварини: {e}")

    def feed_animal(self, id):
        try:
            id = int(id)
            animal = self.session.query(self.Animal).filter(self.Animal.id_animal == id).first()
            if animal:
                if animal.feed != "Fed":
                    animal.feed = "Fed"
                    self.session.commit()
                    logging.info(f"Тварину {animal.name} нагодовано")
                    return True
                else:
                    logging.info(f"Тварина {animal.name} вже нагодована")
                    return True
            else:
                logging.warning(f"Не знайдено тварину з ID {id}")
                return False
        except Exception as e:
            logging.error(f"Помилка при годуванні тварини: {e}")
            return False

    def close(self):
        self.session.close()
        self.connection.close()