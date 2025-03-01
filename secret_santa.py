import csv
import random
import sys
import os

def read_csv(file_path):

    try:
        print(f"Reading CSV from {file_path}")
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            print(f"Successfully read {len(data)} rows from the CSV.")
            return data
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        raise ValueError(f"Error reading CSV file: {e}")


def write_csv(file_path, data):

    try:
        print(f"Writing to CSV file at {file_path}")
        with open(file_path, mode='w', newline='') as file:
            fieldnames = ['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            print(f"CSV file {file_path} written successfully.")
    except Exception as e:
        print(f"Error writing CSV file: {e}")
        raise ValueError(f"Error writing CSV file: {e}")


class SecretSanta:
    def __init__(self, employees, previous_assignments=None):
        self.employees = employees
        self.previous_assignments = previous_assignments or []
        self.assignments = {}

    def get_previous_assignments_dict(self):
        return {(assignment['Employee_Name'], assignment['Employee_EmailID']): 
                (assignment['Secret_Child_Name'], assignment['Secret_Child_EmailID'])
                for assignment in self.previous_assignments}

    def assign_secret_santa(self):
        
        available_employees = {employee['Employee_Name']: employee['Employee_EmailID'] for employee in self.employees}
        assignments_dict = self.get_previous_assignments_dict()

        secret_children = available_employees.copy()

        assigned = []

        for employee in self.employees:
            employee_name = employee['Employee_Name']
            employee_email = employee['Employee_EmailID']

            excluded = {employee_name}
            if (employee_name, employee_email) in assignments_dict:
                excluded.add(assignments_dict[(employee_name, employee_email)][0])

            possible_children = [name for name in secret_children if name not in excluded]

            
            if not possible_children:
                print(f"Warning: No possible secret children for {employee_name}. Assigning a new child.")
                possible_children = list(secret_children.keys())

            secret_child = random.choice(possible_children)
            secret_child_email = secret_children.pop(secret_child)
            
            self.assignments[employee_name] = {
                'Employee_Name': employee_name,
                'Employee_EmailID': employee_email,
                'Secret_Child_Name': secret_child,
                'Secret_Child_EmailID': secret_child_email
            }

            assigned.append(secret_child)

        return self.assignments


def main():
    try:
        print("Starting Secret Santa Assignment...")

        employees = read_csv('employee_data.csv')

        previous_assignments = []

        secret_santa = SecretSanta(employees, previous_assignments)
        assignments = secret_santa.assign_secret_santa()

        print("\nSecret Santa Assignments:")
        for assignment in assignments.values():
            print(f"{assignment['Employee_Name']} ({assignment['Employee_EmailID']}) -> "
                  f"{assignment['Secret_Child_Name']} ({assignment['Secret_Child_EmailID']})")

        # Set the path for the output CSV file
        output_file_path = 'secret_santa_assignments.csv'  # Relative path
        print(f"Saving the assignments to {output_file_path}")

        # Write the results to a new CSV file
        write_csv(output_file_path, list(assignments.values()))

        print(f"Secret Santa assignments have been successfully created and saved to {output_file_path}!")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()



