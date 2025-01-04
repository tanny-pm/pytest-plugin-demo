from pathlib import Path

from src.pytest_plugin_demo.todo_service import Task, load_tasks_from_csv
from tests.conftest import TaskFactory


# pytest-httpserver 用のテスト
def test_httpserver(httpserver):
    test_response = [{"task": "API Task", "completed": False}]
    httpserver.expect_request("/tasks").respond_with_json(test_response)

    import requests

    response = requests.get(httpserver.url_for("/tasks")).json()
    assert response[0]["task"] == "API Task"


# pytest-factoryboy 用のテスト
def test_task_factory():
    for _ in range(100000):  # 時間のかかるテスト
        task = TaskFactory()
        assert isinstance(task, Task)
        assert isinstance(task.completed, bool)


def test_task_factory_2():
    for _ in range(100000):  # 時間のかかるテストの例
        task = TaskFactory()
        assert isinstance(task, Task)
        assert isinstance(task.completed, bool)


# pytest-datadir データファイルの使用
def test_load_tasks_from_csv(datadir):
    csv_file = Path("tests/data/test_tasks.csv")  # 直接パスを指定
    tasks = load_tasks_from_csv(str(csv_file))
    assert len(tasks) == 2


# pytest-icdiff 差分比較
def test_task_comparison():
    task1 = Task("Task A")
    task2 = Task("Task B")
    assert task1.__dict__ == task2.__dict__  # 故意に失敗させる
