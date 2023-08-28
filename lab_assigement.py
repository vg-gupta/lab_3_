class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id}\t{self.name}\t{self.age}\t{self.salary}"


def sort_employee_data(employees, key):
    if key == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif key == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif key == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        raise ValueError("Invalid sorting key")

if __name__ == "__main__":
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    print("Employee Table")
    print("Employee ID\tName\tAge\tSalary (PM)")
    for emp in employees:
        print(emp)

    try:
        sorting_key = int(input("Choose sorting parameter (1. Age, 2. Name, 3. Salary): "))
        sorted_employees = sort_employee_data(employees, sorting_key)

        print("\nSorted Employee Table")
        print("Employee ID\tName\tAge\tSalary (PM)")
        for emp in sorted_employees:
            print(emp)
    except ValueError:
        print("Invalid input for sorting parameter. Please choose 1, 2, or 3.")
