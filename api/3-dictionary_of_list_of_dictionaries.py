#!/usr/bin/python3

"""
Python script to retrieve and export TODO list progress for all employees in JSON format.
"""

import requests
import json


def get_todo_all_employees():
    """
    Retrieves and exports the TODO list progress for all employees in JSON format.
    """

    # Make a GET request to the API endpoint
    response_users = requests.get('https://jsonplaceholder.typicode.com/users')

    # Check if the request was successful
    if response_users.status_code != 200:
        print("Error: Failed to retrieve employee data")
        return

    users = response_users.json()

    # Prepare the dictionary to store the tasks for all employees
    tasks_dict = {}

    # Iterate over each user/employee
    for user in users:
        user_id = user['id']
        username = user['username']

        # Make a GET request to retrieve the TODO list for the current user
        response_todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos',
            params={'userId': user_id}
        )

        # Check if the request was successful
        if response_todos.status_code == 200:
            todos = response_todos.json()

            # Prepare the list to store the tasks for the current user
            user_tasks = []

            # Populate the list with task information
            for todo in todos:
                task_info = {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                user_tasks.append(task_info)

            # Add the list of tasks to the dictionary using the user ID as the key
            tasks_dict[user_id] = user_tasks

    # Prepare the JSON filename
    filename = "todo_all_employees.json"

    # Write the dictionary to a JSON file
    with open(filename, 'w') as file:
        json.dump(tasks_dict, file)

    print(f"TODO list progress for all employees exported to {filename}")


if __name__ == "__main__":
    get_todo_all_employees()

