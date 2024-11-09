from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from schemas.query import Query
import nest_asyncio
nest_asyncio.apply()

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix = '/graphql')
