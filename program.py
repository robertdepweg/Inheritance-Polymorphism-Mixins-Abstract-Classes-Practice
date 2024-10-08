"""Program code"""

# System Imports
import os

# Third-party imports
from filters.person_filter import PersonFilter

# First-Party imports
from employee import Employee, SalaryEmployee, HourlyEmployee
from user_interface import UserInterface


def main(*args):
    """Method to run program"""

    # NOTE: Use the next line to show how it is not possible
    # to make instances of an abstract class
    # If there are no abstract methods in the abstract
    # class, you can technically still make instances.
    # my_employee = Employee("D", "B")
    # print(my_employee)

    # Make a new instance of the UserInterface class
    ui = UserInterface()

    # List to hold employees
    employees: list[Employee] = []
    employees.append(SalaryEmployee("David", "Barnes", 835.00))
    employees.append(SalaryEmployee("James", "Kirk", 453.00))
    employees.append(HourlyEmployee("Jean-Luc", "Picard", 290.00, 40))
    employees.append(HourlyEmployee("Benjamin", "Sisko", 587.00, 30))
    employees.append(SalaryEmployee("Kathryn", "Janeway", 184.00))
    employees.append(HourlyEmployee("Jonathan", "Archer", 135.00, 35))

    # Get some input from the user
    selection = ui.display_menu_and_get_response()

    # While the choice they selected is not 2, continue to do work.
    while selection != ui.MAX_MENU_CHOICES:
        # See if the input they sent is equal to 1.
        if selection == 1:
            # Create string for concatenation
            output_string = ""

            # Convert each employee to a string and add it to the outputstring
            for employee in employees:
                # Concatenate to the output_string
                output_string += f"{employee}{os.linesep}"

            # Use the UI class to print out the string
            ui.print_list(output_string)

        # See if the input they sent is equal to 2.
        if selection == 2:
            # Create Person Filter
            person_filter = PersonFilter()
            filtered_employees = person_filter.filter_by_first_name(
                employees,
                "David",
            )

            # Create string for concatenation
            output_string = ""

            # Convert each employee to a string and add it to output_string
            for employee in filtered_employees:
                # Concatenate to the output_string
                output_string += f"{employee}{os.linesep}"

            # Use the UI class to print out the string
            ui.print_list(output_string)

        # Check for different choice here if there was one to check.

        # Lastly, re-prompt user for input on what to do.
        selection = ui.display_menu_and_get_response()
