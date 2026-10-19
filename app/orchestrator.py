class Orchestrator:
    def run(self, task: str, agents: list[str] | None = None) -> dict:
        selected_agents = agents or ["planner", "executor"]
        return {
            "task": task,
            "agents": selected_agents,
            "result": f"completed:{task}",
        }
