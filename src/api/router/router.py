import strawberry
from strawberry.fastapi import GraphQLRouter

schema = strawberry.Schema(query = Query, mutation = Mutation)
graphql_app = GraphQLRouter(schema)
