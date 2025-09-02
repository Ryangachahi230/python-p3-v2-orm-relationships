import pytest
from employee import Employee
from department import Department

@pytest.fixture(autouse=True)
def setup_and_teardown():
    Department.drop_table()
    Employee.drop_table()
    Department.create_table()
    Employee.create_table()
    yield
    Department.drop_table()
    Employee.drop_table()

def test_create_employee():
    d = Department.create("Engineering", "HQ")
    e = Employee.create("Charlie", "Developer", d.id)
    assert e.id is not None
    assert e.department_id == d.id

def test_find_by_name():
    d = Department.create("IT", "HQ")
    e = Employee.create("Dana", "Support", d.id)
    found = Employee.find_by_name("Dana")
    assert found.id == e.id
    assert found.job_title == "Support"

def test_update_employee():
    d = Department.create("Legal", "HQ")
    e = Employee.create("Eve", "Paralegal", d.id)
    e.job_title = "Lawyer"
    e.update()
    updated = Employee.find_by_id(e.id)
    assert updated.job_title == "Lawyer"
