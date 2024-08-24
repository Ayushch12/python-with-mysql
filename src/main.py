
from database import create_connection, close_connection
from models.employee_model import create_table, insert_employee, select_employees


def main():
    connection = create_connection()
    if connection:
        create_table(connection)
        insert_employee(connection, "John Doe", 30, "HR")
        insert_employee(connection, "Jane Smith", 25, "Finance")
        insert_employee(connection, "Mike Johnson", 40, "IT")
        print("Employees in the database:")
        select_employees(connection)
        close_connection(connection)

if __name__ == "__main__":
    main()
