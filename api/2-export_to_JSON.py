#!/usr/bin/python3

"""
Python script to retrieve and export TODO list progress for a given employee ID in JSON format.
"""

import requests
import sys
import json


def get_employee_todo_list(employee_id):
    """
    Retrieves and exports the TODO list progress for a given employee ID in JSON format.
    """

    # Make a GET request to the API endpoint
    response = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params={'userId': employee_id}
    )

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: Failed to retrieve TODO list for employee {employee_id}")
        return

    todos = response.json()

    # Prepare the JSON filename
    filename = f"{employee_id}.json"

    # Create a dictionary to store the tasks
    tasks_dict = {"USER_ID": []}

    # Populate the dictionary with task information
    for todo in todos:
        task_info = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": todo['username']
        }
        tasks_dict["USER_ID"].append(task_info)

    # Write the dictionary to a JSON file
    with open(filename, 'w') as file:
        json.dump(tasks_dict, file)

    print(f"TODO list progress exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:

