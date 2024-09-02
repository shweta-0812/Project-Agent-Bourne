# flake8: noqa
# helps to identify agent.models.* files as valid model class if called with agent.* from other
# files

# the order matters - always put the models which have foreign keys later in the list to avoid import errors

from agent.models.task_detail_model import *
from agent.models.step_detail_model import *
from agent.models.artifact_detail_model import *
