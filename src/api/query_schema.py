import strawberry
from owner.type import Owner
from owner.resolvers import get_data__owner

@strawberry.type
class Query:
    owner: Owner = strawberry.field(resolver = get_data__owner)
