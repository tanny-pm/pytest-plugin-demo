import factory

from src.pytest_plugin_demo.todo_service import Task


class TaskFactory(factory.Factory):
    class Meta:
        model = Task

    task = factory.Faker("sentence", nb_words=3)
    completed = factory.Faker("boolean")
