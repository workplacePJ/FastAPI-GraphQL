import strawberry
from owner.type import Owner
from owner.resolvers import owner

@strawberry.type
class Query:
    owner: Owner = strawberry.field(resolver = owner)
