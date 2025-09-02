import pytest
from department import Department
from employee import Employee

@pytest.fixture(autouse=True)
def setup_and_teardown():
    Department.drop_table()
    Employee.drop_table()
    Department.create_table()
    Employee.create_table()
    yield
    Department.drop_table()
    Employee.drop_table()

def test_create_department():
    d = Department.create("HR", "Building A")
    assert d.id is not None
    assert d.name == "HR"

def test_find_by_name():
    d = Department.create("Finance", "Building B")
    found = Department.find_by_name("Finance")
    assert found.id == d.id
    assert found.location == "Building B"

def test_department_employees():
    d = Department.create("Payroll", "Building C")
    e1 = Employee.create("Alice", "Analyst", d.id)
    e2 = Employee.create("Bob", "Manager", d.id)
    employees = d.employees()
    assert len(employees) == 2
    assert employees[0].name in ["Alice", "Bob"]
