import strawberry

@strawberry.type
class Owner:
    id: int
    name: str
    postalCode: str
    address: str
