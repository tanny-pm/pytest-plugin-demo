# Pytest Plugin Demo

This project demonstrates the usage of various pytest plugins and includes a simple task management system.

## Project Structure

```
.
├── README.md
├── src
│   └── pytest_plugin_demo
│       ├── __init__.py
│       └── todo_service.py
└── tests
    ├── __init__.py
    ├── conftest.py
    └── test_todo_service.py
```

## Installation

To set up this project, follow these steps:

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Features

- Task management system with `Task` class
- CSV file loading for tasks

## Usage

The project demonstrates the usage of various pytest plugins:

- pytest-httpserver
- pytest-factoryboy
- pytest-datadir
- pytest-icdiff

To run the tests and see the plugins in action, use:

```
pytest
```

## Testing

The `tests` directory contains test cases that demonstrate the usage of different pytest plugins:

- `test_httpserver`: Shows how to use pytest-httpserver to mock HTTP responses
- `test_task_factory`: Demonstrates pytest-factoryboy for generating test data
- `test_load_tasks_from_csv`: Uses pytest-datadir for loading test data from files
- `test_task_comparison`: Showcases pytest-icdiff for improved assertion diffs

## License

[Include license information here]