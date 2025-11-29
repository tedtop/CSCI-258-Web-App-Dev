"""
Unit tests for my_module.py
"""

import unittest
from my_module import max3, odd, majority, Employee, Manager


class TestFunctions(unittest.TestCase):
    """Test case for the three functions: max3, odd, and majority."""

    def test_max3_first_largest(self):
        """Test max3 when first argument is largest."""
        self.assertEqual(max3(10, 5, 3), 10)

    def test_max3_second_largest(self):
        """Test max3 when second argument is largest."""
        self.assertEqual(max3(3, 15, 7), 15)

    def test_max3_third_largest(self):
        """Test max3 when third argument is largest."""
        self.assertEqual(max3(4, 8, 20), 20)

    def test_odd_zero_true(self):
        """Test odd when no arguments are True."""
        self.assertFalse(odd(False, False, False))

    def test_odd_one_true(self):
        """Test odd when one argument is True."""
        self.assertTrue(odd(True, False, False))

    def test_odd_two_true(self):
        """Test odd when two arguments are True."""
        self.assertFalse(odd(True, True, False))

    def test_majority_zero_true(self):
        """Test majority when no arguments are True."""
        self.assertFalse(majority(False, False, False))

    def test_majority_one_true(self):
        """Test majority when one argument is True."""
        self.assertFalse(majority(True, False, False))

    def test_majority_two_true(self):
        """Test majority when two arguments are True."""
        self.assertTrue(majority(True, True, False))


class TestEmployee(unittest.TestCase):
    """Test case for the Employee parent class."""

    def test_employee_name(self):
        """Test Employee name instance variable."""
        emp = Employee("John", 50000)
        self.assertEqual(emp.name, "John")

    def test_employee_salary(self):
        """Test Employee salary instance variable."""
        emp = Employee("John", 50000)
        self.assertEqual(emp.salary, 50000)

    def test_employee_get_details(self):
        """Test Employee get_details method."""
        emp = Employee("Trish", 100000)
        self.assertEqual(emp.get_details(), "Name: Trish, Salary: $100000")


class TestManager(unittest.TestCase):
    """Test case for the Manager child class."""

    def test_manager_name(self):
        """Test Manager name instance variable (inherited)."""
        mgr = Manager("Alice", 80000, "Engineering")
        self.assertEqual(mgr.name, "Alice")

    def test_manager_salary(self):
        """Test Manager salary instance variable (inherited)."""
        mgr = Manager("Alice", 80000, "Engineering")
        self.assertEqual(mgr.salary, 80000)

    def test_manager_department(self):
        """Test Manager department instance variable."""
        mgr = Manager("Alice", 80000, "Engineering")
        self.assertEqual(mgr.department, "Engineering")

    def test_manager_get_details(self):
        """Test Manager get_details method (overridden)."""
        mgr = Manager("Trish", 100000, "Computer Science")
        self.assertEqual(mgr.get_details(), "Name: Trish, Salary: $100000, Department: Computer Science")


if __name__ == '__main__':
    unittest.main()
