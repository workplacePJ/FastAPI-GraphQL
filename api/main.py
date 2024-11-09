from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from schemas.company import Company
import nest_asyncio
nest_asyncio.apply()

@strawberry.type
class Query:
    @strawberry.field
    def company(self) -> Company:
        return Company(name = '株式会社トータルメディエイト', postalCode = '1140034', address = '東京都北区上十条2-25-4')

schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix = '/graphql')





from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pyngrok import ngrok


# Add the CORSMiddleware immediately after creating the app
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)


from google.colab import userdata
auth_token = userdata.get('ngrok')
ngrok.set_auth_token(auth_token)

ngrok_tunnel = ngrok.connect(8000)
print('PUBLIC_URL:', ngrok_tunnel.public_url)
print('PUBLIC_URL_PREFIX:', f'{ngrok_tunnel.public_url}/graphql')
print('PUBLIC_DOCS_URL:', f'{ngrok_tunnel.public_url}/docs')
uvicorn.run(app, port = 8000)
