import strawberry
from .owner.type import Owner
from .owner.resolvers import owner_get

@strawberry.type
class Query:
    owner_data: Owner = strawberry.field(resolver = owner_get)
