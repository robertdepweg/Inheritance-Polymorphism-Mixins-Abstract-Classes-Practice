"""Employee Module"""

from abc import ABC, abstractmethod

# from typing import override


class Employee(ABC):
    """Class to represent a single base employee"""

    WEEKS_PER_YEAR = 52

    def __init__(self, first_name, last_name):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        """String Method"""
        return f"{self.first_name:<10} {self.last_name:<20}"

    def first_and_last_name(self):
        """Return first and last name concatenated together"""
        return f"{self.first_name:<10} {self.last_name:<20}"

        # NOTE: Can't do the following if planning to call this
        # first_and_last name method from outside classes.
        # Comment out the above and uncomment the below, then
        # also call this method from somewhere else to see it fail.
        # return self.__str__()

    # Made this property abstract because we want all sub-classes
    # to implement it. But, we don't know how. So, we can leave the
    # details to the sub-class.
    @property
    @abstractmethod
    def formatted_weekly_salary(self):
        """Property for weekly salary formatted as currency"""
        raise NotImplementedError()

    # Made this property abstract because we want all sub-classes
    # to implement it. But, we don't know how. So, we can leave the
    # details to the sub-class.
    @property
    @abstractmethod
    def yearly_salary(self):
        """Property for yearly salary"""
        raise NotImplementedError()

    # Made this property abstract because we want all sub-classes
    # to implement it. But, we don't know how. So, we can leave the
    # details to the sub-class.
    @property
    @abstractmethod
    def formatted_yearly_salary(self):
        """Property for yearly salary formatted as currency"""
        raise NotImplementedError()

    # Made this method abstract because we want all sub-classes
    # to implement it. But, we don't know how. So, we can leave the
    # details to the sub-class.
    @abstractmethod
    def apply_percentage_raise(self, percentage):
        """Accept a percentage raise and apply it to the pay rate"""
        raise NotImplementedError()


class SalaryEmployee(Employee):
    """Class to represent a single salary employee"""

    def __init__(self, first_name, last_name, weekly_salary):
        """Constructor"""
        super().__init__(first_name, last_name)
        self.weekly_salary = weekly_salary

    def __str__(self):
        """String method"""
        return f"{super().__str__()} {self.formatted_weekly_salary:>14}"

    @property
    def formatted_weekly_salary(self):
        """Property for weekly salary formatted as currency"""
        return f"${self.weekly_salary:.2f}"

    @property
    def yearly_salary(self):
        """Property for yearly salary"""
        return self.weekly_salary * self.WEEKS_PER_YEAR

    @property
    def formatted_yearly_salary(self):
        """Property for yearly salary formatted as currency"""
        return f"${self.yearly_salary:.2f}"

    def apply_percentage_raise(self, percentage):
        """Accept a percentage raise and apply it to the weekly salary"""
        self.weekly_salary = self.weekly_salary * (1 + (percentage / 100))


class HourlyEmployee(Employee):
    """Class to represent a single hourly employee"""

    def __init__(self, first_name, last_name, hourly_rate, hours_per_week):
        """Constructor"""
        super().__init__(first_name, last_name)
        self.hourly_rate = hourly_rate
        self.hours_per_week = hours_per_week

    def __str__(self):
        """String method"""
        return f"{super().__str__()} {self.formatted_weekly_salary:>14}"

    def first_and_last_name(self):
        """Return first and last name concatenated together"""
        return f"{self.first_name:<10} {self.last_name:<20}"

    @property
    def weekly_salary(self):
        """Return first and last name concatenated together"""
        return self.hourly_rate * self.hours_per_week

    @property
    def formatted_weekly_salary(self):
        """Property for weekly salary formatted as currency"""
        return f"${self.weekly_salary:.2f}"

    @property
    def yearly_salary(self):
        """Property for yearly salary"""
        return self.weekly_salary * self.WEEKS_PER_YEAR

    @property
    def formatted_yearly_salary(self):
        """Property for yearly salary formatted as currency"""
        return f"${self.yearly_salary:.2f}"

    def apply_percentage_raise(self, percentage):
        """Accept a percentage raise and apply it to the hourly rate"""
        self.hourly_rate = self.hourly_rate * (1 + (percentage / 100))
