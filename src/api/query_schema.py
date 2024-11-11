import strawberry
from owner.type import Owner
from owner.resolvers import get_data__owner, get_data__owners

@strawberry.type
class Query:
    owner: Owner = strawberry.field(resolver = get_data__owner)
    owner: Owners = strawberry.field(resolver = get_data__owners)
