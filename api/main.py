from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
import nest_asyncio
nest_asyncio.apply()


@strawberry.type
class Company:
    name: str
    postalCode: str
    address: str

@strawberry.type
class Query:
    @strawberry.field
    def company(self) -> Company:
        return Company(name = '株式会社トータルメディエイト', postalCode = '1140034', address = '東京都北区上十条2-25-4')

schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix = '/graphql')
