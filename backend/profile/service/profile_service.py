from jinja2 import Environment, FileSystemLoader
from typing import List
from pydantic import BaseModel

env = Environment(loader=FileSystemLoader("profile/templates/"))


class Profile(BaseModel):
    role: str
    goal: str
    backstory: str
    tools: List[str]


def select_profile(profile_name, profile_params=None):
    profile_template = env.get_template(f"{profile_name}.txt")
    profile = profile_template.render()

    return profile
