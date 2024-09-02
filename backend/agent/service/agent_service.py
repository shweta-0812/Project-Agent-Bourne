import yaml
from agent.models.task_detail_model import TaskDetail
from crewai import Agent, Crew
from typing import List, Union
from pydantic import BaseModel


class AgentTask(BaseModel):
    description: str
    expected_output: str


class AgentTaskList(BaseModel):
    tasks: List[AgentTask]


def create_crew(agents, tasks, process=None, manager_llm=None, embedder=None):
    crew_kwargs = {
        "agents": agents,
        "tasks": tasks,
        "verbose": 2,
        "memory": False,
    }
    if embedder is not None:
        crew_kwargs["embedder"] = embedder
    if process is not None:
        crew_kwargs["process"] = process
    if manager_llm is not None:
        crew_kwargs["manager_llm"] = manager_llm
    return Crew(**crew_kwargs)


def create_agent(agent_role: str, llm: Union[str, None] = None):
    # using config for now
    with open("agent/agents_config.yaml", "r") as file:
        agents_config = yaml.safe_load(file)

    agent_config = agents_config[agent_role]

    extra_args = {}
    if llm is not None:
        extra_args["llm"] = llm

    agent = Agent(
        role=agent_role,
        goal=agent_config["goal"],
        backstory=agent_config["backstory"],
        allow_delegation=agent_config.get("allow_delegation", False),
        verbose=agent_config.get("verbose", True),
        **extra_args
    )
    return agent


def create_task(input=input, additional_input=None):
    return TaskDetail(input=input, additional_input=additional_input, )
