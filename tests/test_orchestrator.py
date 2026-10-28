from app.orchestrator import Orchestrator


def test_orchestrator_run():
    orchestrator = Orchestrator()
    result = orchestrator.run("deterministic task")
    assert result == {
        "task": "deterministic task",
        "agents": ["planner", "executor"],
        "result": "completed:deterministic task",
    }
