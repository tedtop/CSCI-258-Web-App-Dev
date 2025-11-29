"""
Module containing utility functions and Employee classes.
"""


def max3(a, b, c):
    """
    Returns the largest of three int or float arguments.

    Args:
        a: First number (int or float)
        b: Second number (int or float)
        c: Third number (int or float)

    Returns:
        The largest of the three numbers
    """
    return max(a, b, c)


def odd(a, b, c):
    """
    Returns True if an odd number of arguments are True, False otherwise.

    Args:
        a: First boolean value
        b: Second boolean value
        c: Third boolean value

    Returns:
        True if odd number of arguments are True, False otherwise
    """
    count = sum([a, b, c])
    return count % 2 == 1


def majority(a, b, c):
    """
    Returns True if at least two of the arguments are True, False otherwise.

    Args:
        a: First boolean value
        b: Second boolean value
        c: Third boolean value

    Returns:
        True if at least two arguments are True, False otherwise
    """
    count = sum([a, b, c])
    return count >= 2


class Employee:
    """
    Parent class representing an employee.
    """

    def __init__(self, name, salary):
        """
        Initialize an Employee.

        Args:
            name: Employee's name (str)
            salary: Employee's salary (int or float)
        """
        self.name = name
        self.salary = salary

    def get_details(self):
        """
        Returns a string with employee details.

        Returns:
            String in format "Name: {name}, Salary: ${salary}"
        """
        return f"Name: {self.name}, Salary: ${self.salary}"


class Manager(Employee):
    """
    Child class representing a manager, inheriting from Employee.
    """

    def __init__(self, name, salary, department):
        """
        Initialize a Manager.

        Args:
            name: Manager's name (str)
            salary: Manager's salary (int or float)
            department: Manager's department (str)
        """
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        """
        Returns a string with manager details including department.

        Returns:
            String in format "Name: {name}, Salary: ${salary}, Department: {department}"
        """
        return f"Name: {self.name}, Salary: ${self.salary}, Department: {self.department}"
