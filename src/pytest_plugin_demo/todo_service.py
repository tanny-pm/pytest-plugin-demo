import csv
from typing import List


class Task:
    """タスクを表すクラス。

    Attributes:
        task (str): タスクの名前
        completed (bool): タスクの完了状態

    Example:
        >>> task = Task("Example Task")
        >>> task.completed
        False
        >>> task.complete()
        >>> task.completed
        True
    """

    def __init__(self, task: str, completed: bool = False):
        self.task = task
        self.completed = completed

    def complete(self):
        self.completed = True


def load_tasks_from_csv(filepath: str) -> List[Task]:
    """CSVファイルからタスクを読み込む。

    Example:
        >>> tasks = load_tasks_from_csv("tests/data/test_tasks.csv")
        >>> len(tasks)
        2
    """
    with open(filepath, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return [Task(row["task"], row["completed"] == "True") for row in reader]
