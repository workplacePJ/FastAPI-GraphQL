import strawberry
from strawberry.fastapi import GraphQLRouter
from query import Query
#from mutation import Mutation

#schema = strawberry.Schema(query = Query, mutation = Mutation)
schema = strawberry.Schema(query = Query)
graphql_app = GraphQLRouter(schema)
