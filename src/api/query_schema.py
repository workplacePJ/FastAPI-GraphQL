import strawberry

#@strawberry.type
#class Query:



@strawberry.type
class Owner:
    id: int
    name: str
    postalCode: str
    address: str

async def get_owner(self) -> Owner:
    return Owner(id = 1, name = '株式会社トータルメディエイト', postalCode = '1140034', address = '東京都北区上十条2-25-4')

@strawberry.type
class Query:
    owner: Owner = strawberry.field(resolver = get_owner)
