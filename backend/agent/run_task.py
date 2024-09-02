from common_utils import get_env_key
from langchain_openai import ChatOpenAI
from plan.service.plan_service import create_plan
from action.service.action_service import execute_plan

JINA_MODEL = get_env_key('JINA_MODEL')
JINA_API_KEY = get_env_key('JINA_API_KEY')
JINA_API_BASE = get_env_key('JINA_API_BASE')

OPENAI_API_KEY = get_env_key('OPENAI_API_KEY')
OPENAI_API_BASE = get_env_key('OPENAI_API_BASE')


PROVIDER = "openai"


def run_simple_task(task_prompt: str):
    embedder = {
        "provider": PROVIDER,
        "config": {
            "model": JINA_MODEL,
            "api_key": JINA_API_KEY,
            "api_base": JINA_API_BASE,
        },
    }
    llm = ChatOpenAI(
        base_url=OPENAI_API_BASE,
        api_key=OPENAI_API_KEY
    )
    tasks_json = create_plan(
        task_prompt,
        llm=llm,
        embedder=embedder,
    )
    plan_resp = execute_plan(tasks_json, llm=llm, embedder=embedder)
    return plan_resp
