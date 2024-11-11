import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig
from query_schema import Query
#from mutation_schema import Mutation

schema = strawberry.Schema(query = Query, config = StrawberryConfig(auto_camel_case = True))
#schema = strawberry.Schema(query = Query, mutation = Mutation, config = StrawberryConfig(auto_camel_case = True))
graphql_app = GraphQLRouter(schema)
