from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_agents_run():
    response = client.post("/agents/run", json={"task": "demo task", "agents": ["planner", "executor"]})
    assert response.status_code == 200
    assert response.json() == {
        "task": "demo task",
        "agents": ["planner", "executor"],
        "result": "completed:demo task",
    }
