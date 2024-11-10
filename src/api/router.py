import strawberry
from strawberry.fastapi import GraphQLRouter
from query_schema import Query
from mutation_schema import Mutation

schema = strawberry.Schema(query = Query, mutation = Mutation)
graphql_app = GraphQLRouter(schema)
