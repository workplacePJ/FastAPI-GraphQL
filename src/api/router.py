import strawberry
from strawberry.fastapi import GraphQLRouter
#from resolvers import 
#from owner. 


@strawberry.type
class Query:
    task: TaskType = strawberry.field(resolver=get_task)
    tasks: list[TaskType] = strawberry.field(resolver=get_tasks)


@strawberry.type
class Mutation:
    task_add: TaskType = strawberry.field(resolver=add_task)
    task_update: TaskType = strawberry.field(resolver=update_task)
    task_delete: TaskType = strawberry.field(resolver=delete_task)


schema = strawberry.Schema(query=Query, mutation=Mutation)
task_app = GraphQLRouter(schema, context_getter=get_context)








schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix = '/graphql')
