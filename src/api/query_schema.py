import strawberry
from owner.types import Owner

@strawberry.type
class Query:
    owner: Owner = strawberry.field(resolver = get_owner)
