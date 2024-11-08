import strawberry

@strawberry.type
class Company:
    id: int
    name: str
    postalCode: str
    address: str
