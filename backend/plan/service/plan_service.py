from agent.service.task_service import create_plan_task, create_review_task, create_team_task
from agent.service.agent_service import create_agent, create_crew
# from tool.service.tool_service import get_tools
from agent.models.pydantic_schema import AgentTaskList


def create_plan(goal, llm=None, embedder=None):
    strategy_maker = create_agent(agent_role="Strategy Maker", llm=llm)
    critic = create_agent(agent_role="Strategy Reviewer", llm=llm)

    plan_task = create_plan_task(strategy_maker)

    review_task = create_review_task(
        critic, output_file="outputs/tasks.json"
    )
    planning_crew = create_crew(
        agents=[strategy_maker, critic],
        tasks=[plan_task, review_task],
        embedder=embedder,
    )
    print(planning_crew)
    print("kickoff my crew")

    tasks_json = planning_crew.kickoff(inputs={"goal": goal})
    print(f"{tasks_json}")

    tasks_list = AgentTaskList.parse_raw(tasks_json)

    agent_creator = create_agent(agent_role="Leader", llm=llm)

    team_creation_tasks = []
    # Iterate over tasks in tasks_list to create new tasks
    # tools = get_tools()
    tools = []

    tools_list = "\n".join(
        f"{i + 1}. Name: {tool.name}\n   Description: {tool.description}"
        for i, tool in enumerate(tools)
    )
    for index, task in enumerate(tasks_list.tasks):
        # Generate output file name
        output_file = f"outputs/role-{index}.json"

        # Create a new task using the updated function signature
        new_task = create_team_task(
            agent=agent_creator,  # Assuming the same agent for simplicity
            output_file=output_file,
            description=task.description,
            expected_output=task.expected_output,
            goal=goal,
            tools_list=tools_list,
        )
        team_creation_tasks.append(new_task)

        team_setup_crew = create_crew(
            agents=[agent_creator], tasks=[new_task], embedder=embedder
        )

        team_setup_crew.kickoff()
    return tasks_json
