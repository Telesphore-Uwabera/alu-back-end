## API


# Employee Task Tracker

This Python script retrieves and processes task information for a specific employee from the JSONPlaceholder API and performs the following tasks:

1. Displays the employee's name.
2. Lists the completed tasks along with their titles.
3. Creates a CSV file containing task details.
4. Creates a JSON file containing task details.

## Usage

To use this script, you need to provide an employee ID as a command-line argument. Here's how to run the script:

```bash
python employee_task_tracker.py <employee_id>
```

Replace `<employee_id>` with the ID of the employee you want to track.

## Dependencies

This project relies on the following Python libraries:

- `requests` for making HTTP requests to the JSONPlaceholder API.

## Files

- `employee_task_tracker.py`: The main Python script that retrieves and processes employee task information.
- `README.md`: This file, providing an overview of the project.
- `<employee_id>.csv`: CSV file containing task details for the employee.
- `<employee_id>.json`: JSON file containing task details for the employee.

## Example

Here's an example of how to run the script and what to expect:

```bash
python employee_task_tracker.py 1
```

Output:

```
Employee Leanne Graham is done with tasks(6/20):
     sunt aut facere repellat provident occaecati excepturi optio reprehenderit

# CSV and JSON Files
- [1.csv](1.csv) - CSV file containing task details.
- [1.json](1.json) - JSON file containing task details.

## Author

- Telesphore Uwabera

Feel free to contribute or report issues in this project.

```
