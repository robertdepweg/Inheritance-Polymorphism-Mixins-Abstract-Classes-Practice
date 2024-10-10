"""Tests for Employee module"""

# System imports
from unittest import TestCase

# First-Party Imports
from employee import HourlyEmployee, SalaryEmployee


class HourlyEmployeeTest(TestCase):
    """Test for HourlyEmployee"""

    def setUp(self):
        """Set up method for all tests in this class"""
        self.hourly_employee = HourlyEmployee("Test", "User", 10.00, 50.00)
        self.yearly_employee = SalaryEmployee("Test", "User", 100.00)

    def test_hourly_employee_creation(self):
        """Test hourly employee creation"""

        # Arrange
        # Set things up for the test. Get it ready to be tested.
        expected_first_name = "Test"
        expected_last_name = "User"
        expected_hourly_rate = 10.00
        expected_hours_per_week = 50.00

        # Act
        # Do the actual action that is being tested.
        # NOTE: No longer need this thanks to setUp method.
        # hourly_employee = HourlyEmployee("Test", "User", 10.00, 50.00)

        # Assert
        # Verify that the result of the Act is what is expected.
        self.assertEqual(self.hourly_employee.first_name, expected_first_name)
        self.assertEqual(self.hourly_employee.last_name, expected_last_name)
        self.assertEqual(self.hourly_employee.hourly_rate, expected_hourly_rate)
        self.assertEqual(self.hourly_employee.hours_per_week, expected_hours_per_week)

    def test_hourly_employee_str_method(self):
        """Test hourly employee str method"""
        # Arrange
        expected = f"{'Test':<10} {'User':<20} {'$500.00':>14}"

        # Act
        actual = str(self.hourly_employee)

        # Assert
        self.assertEqual(actual, expected)


# class SalaryEmployeeTest(TestCase):
#     """Test for SalaryEmployee"""

#     def setUp(self) -> None:
#         return super().setUp()

#     def test_salary_employee_formatted_yearly_salary(self):
#         """Test salary employee formatted yearly salary"""

#         # Arrange
#         expected = "$26000.00"

#         # Act
#         actual = self.salary_employee.formatted_yearly_salary

#         # Assert
#         self.assertEqual(actual, expected)

#     def test_yearly_employee_creation(self):
#         """Test Yearly employee creation"""

#         # Arrange
#         # Set things up for the test. Get it ready to be tested.
#         expected_first_name = "Test"
#         expected_last_name = "User"
#         expected_salary_rate = 1000.00

#         # Act
#         # Do the actual action that is being tested.
#         # NOTE: No longer need this thanks to setUp method.
#         # salary_employee = HourlyEmployee("Test", "User", 10.00, 50.00)

#         # Assert
#         # Verify that the result of the Act is what is expected.
#         self.assertEqual(self.salary_employee.first_name, expected_first_name)
#         self.assertEqual(self.salary_employee.last_name, expected_last_name)
#         self.assertEqual(self.salary_employee.salary_rate, expected_salary_rate)

#     def test_salary_employee_str_method(self):
#         """Test salary employee str method"""
#         # Arrange
#         expected = f"{'Test':<10} {'User':<20} {'$500.00':>14}"

#         # Act
#         actual = str(self.salary_employee)

#         # Assert
#         self.assertEqual(actual, expected)

#     def test_salary_employee_formatted_yearly_salary(self):
#         """Test salary employee formatted yearly salary"""

#         # Arrange
#         expected = "$26000.00"

#         # Act
#         actual = self.salary_employee.formatted_yearly_salary

#         # Assert
#         self.assertEqual(actual, expected)
