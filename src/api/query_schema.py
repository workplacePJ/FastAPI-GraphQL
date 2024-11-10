import strawberry
from api.owner.type import Owner

@strawberry.type
class Query:
    owner: Owner = strawberry.field(resolver = get_owner)
