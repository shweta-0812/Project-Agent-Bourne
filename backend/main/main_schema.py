import graphene
import agent.agent_schema as agent_schema
# import client.client_schema as client_schema
import user.user_schema as user_schema
# import workspace.workspace_schema as workspace_schema


class Query(
        # agent_schema.Query,
        # client_schema.Query,
        user_schema.Query,
        # workspace_schema.Query,
        graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(
        agent_schema.Mutation,
        # client_schema.Mutation,
        user_schema.Mutation,
        graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
