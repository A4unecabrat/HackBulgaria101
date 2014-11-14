import sqlite3

db = sqlite3.connect('positions_hack')


def is_viable(command):
    if (command == "list_employees" or command == "monthly_spending"
            or command == "yearly_spending" or command == "add_employee"
            or command == "delete_employee" or command == "update_employee"
            or command == "exit"):
        return True
    else:
        return False


def list_employees():
    list_of_employes = db.execute('''SELECT name, position FROM employees''')
    for row in list_of_employes:
        print("{}-{}".format(row[0], row[1]))
    db.commit()


def monthly_spending():
    result = 0
    list_of_monthly_salaries = db.execute('''SELECT monthly_salary FROM
     employees''')
    for row in list_of_monthly_salaries:
        result += row[0]
    db.commit()
    print(result)


def yearly_spending():
    result = 0
    list_of_monthly_salaries = db.execute('''SELECT monthly_salary,
        yearly_bonus FROM employees''')
    for row in list_of_monthly_salaries:
        result += row[0] * 12
        result += row[1]
    db.commit()
    print(result)


def add_employee(name, monthly_salary, yearly_bonus, position):
    db.execute(''' INSERT INTO employees(name, monthly_salary, yearly_bonus,
     position) VALUES(?,?,?,?)''',
               (name, monthly_salary, yearly_bonus, position))
    db.commit()


def delete_employee(employee_id):
    db.execute(''' DELETE FROM employees WHERE id = ?''', (employee_id,))
    db.commit()


def update_employee(employee_id):
    newname = input("name: ")
    newmonthly_salary = input("monthly_salary: ")
    newyearly_bonus = input("yearly_bonus: ")
    newposition = input("position: ")
    db.execute(''' UPDATE employees SET name = ?, monthly_salary = ?,
     yearly_bonus = ?, position = ? WHERE id = ?''',
               (newname, newmonthly_salary, newyearly_bonus, newposition,
                employee_id))
    db.commit()


def do_this(command):
    if command == "list_employees":
        list_employees()
    elif command == "monthly_spending":
        monthly_spending()
    elif command == "yearly_spending":
        yearly_spending()
    elif command == "add_employee":
        name = input("name :")
        monthly_salary = input("monthly_salary:")
        yearly_bonus = input("yearly_bonus:")
        position = input("position: ")
        add_employee(name, monthly_salary, yearly_bonus, position)
    elif command == "delete_employee":
        employee_id = input("employee id: ")
        delete_employee(employee_id)
    elif command == "update_employee":
        employee_id = input("employee id: ")
        update_employee(employee_id)


def main():
    command = ""
    while command != "exit":
        command = input("enter a viable command: ")
        while is_viable(command) is False:
            print("Go in the kitchen and make me a sandwitch!!!")
            command = input("Try again: ")
        do_this(command)
    db.close()

if __name__ == '__main__':
    main()
