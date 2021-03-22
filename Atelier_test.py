from atelier import TaskManager, Action


def test_can_create_an_action():
    action = Action("add", "first task")
    assert action.name == "add"
    assert action.description == "first task"

def test_task_manager_starts_with_no_tasks():
    task_manager = TaskManager()

    assert task_manager.tasks == []


def test_parse_add():
    command = "+ first task"
    task_manager = TaskManager()

    action = task_manager.parse(command)

    assert action.name == "add"
    

    
def test_parse_remove():
    command = "- 1"
    task_manager = TaskManager()
    
    action = task_manager.parse(command)
    
    assert action.name == "remove"


def test_parse_done():
    command = "x 1"
    task_manager = TaskManager()

    action = task_manager.parse(command)

    assert action.name == "done"
