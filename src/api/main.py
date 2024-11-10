from fastapi import FastAPI
from router.router import graphql_app

api = FastAPI()

if __name__ == '__main__':
    api.include_router(graphql_app, prefix = '/graphql')
