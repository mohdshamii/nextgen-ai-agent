from fastapi import FastAPI
from pydantic import BaseModel

from app.orchestrator import Orchestrator

app = FastAPI()
orchestrator = Orchestrator()


class RunAgentsRequest(BaseModel):
    task: str
    agents: list[str] | None = None


@app.get("/")
async def read_root():
    return {"message": "Hello, World"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/agents/run")
async def run_agents(payload: RunAgentsRequest):
    return orchestrator.run(task=payload.task, agents=payload.agents)
