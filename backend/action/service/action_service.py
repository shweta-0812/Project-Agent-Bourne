from crewai import Agent, Task

from agent.models.pydantic_schema import AgentTaskList
from agent.service.agent_service import create_crew
from profile.service.profile_service import Profile
# from tool.service.tool_service import get_tools


def execute_plan(tasks_json, llm=None, embedder=None):
    # tools = get_tools()
    tools = []

    tasks_list = AgentTaskList.parse_raw(tasks_json)
    llm_args = {}
    if llm is not None:
        llm_args["llm"] = llm

    tasks = []
    agents = []

    context = None
    for i, task in enumerate(tasks_list.tasks):
        with open(f"outputs/role-{i}.json", "r") as f:
            character = Profile.parse_raw(f.read())
        agent = Agent(
            role=character.role,
            goal=character.goal,
            backstory=character.backstory,
            tools=tools,
            allow_delegation=False,
            verbose=True,
            **llm_args,
        )
        agents.append(agent)
        task_args = {
            "description": task.description,
            "expected_output": task.expected_output,
            "agent": agent,
            "context": context
        }
        if context is not None:
            task_args["context"] = [context]
        task = Task(**task_args)

        tasks.append(task)
        context = task  # Update the context for the next iteration

    master_crew = create_crew(
        agents=agents,
        tasks=tasks,
        embedder=embedder,
        # , process=Process.hierarchical, manager_llm=llm,
    )

    resp = master_crew.kickoff()
    return resp
