from pydantic import BaseModel
from typing import List


class AgentTask(BaseModel):
    description: str
    expected_output: str


class AgentTaskList(BaseModel):
    tasks: List[AgentTask]
