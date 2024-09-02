from graphene import ObjectType, String, Boolean, Field, Mutation
from agent.run_task import run_simple_task


class RunTaskResponseType(ObjectType):
    response = String()


class RunTask(Mutation):
    ok = Boolean()
    task_response = Field(lambda: RunTaskResponseType)

    class Arguments:
        task_prompt = String()

    def mutate(self, info, task_prompt):
        run_simple_task(task_prompt=task_prompt)
        return RunTask(ack="Task received and will be processed asynchronously")


class Mutation(ObjectType):
    run_task = RunTask.Field()
