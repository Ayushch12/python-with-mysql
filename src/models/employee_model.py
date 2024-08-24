
def create_table(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employes3 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT,
        department VARCHAR(100)
    ) ENGINE = InnoDB;
    """
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()
    print("Table 'employees' created successfully")

def insert_employee(connection, name, age, department):
    insert_query = """
    INSERT INTO employees (name, age, department)
    VALUES (%s, %s, %s)
    """
    cursor = connection.cursor()
    cursor.execute(insert_query, (name, age, department))
    connection.commit()
    print("Employee inserted successfully")

def select_employees(connection):
    select_query = "SELECT * FROM employees"
    cursor = connection.cursor()
    cursor.execute(select_query)
    result = cursor.fetchall()

    for row in result:
        print(row)
