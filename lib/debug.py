from department import Department
from employee import Employee

# Reset tables
Department.drop_table()
Employee.drop_table()
Department.create_table()
Employee.create_table()

# Create departments
payroll = Department.create("Payroll", "Building A")
hr = Department.create("Human Resources", "Building C")

# Create employees
e1 = Employee.create("Amir", "Accountant", payroll.id)
e2 = Employee.create("Bola", "Manager", payroll.id)
e3 = Employee.create("Charlie", "Manager", hr.id)
e4 = Employee.create("Dani", "Benefits Coordinator", hr.id)

import ipdb; ipdb.set_trace()
