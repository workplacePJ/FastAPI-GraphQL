import strawberry
#from owner.type import Owner
#from .owner.resolvers import owner_get

@strawberry.type
class Owner:
    id: int
    name: str
    postalCode: str
    address: str

from strawberry.types import Info
async def owner_get(info: Info, id: int) -> Owner:
    #owner_dict = await get_owner(info, id)
    owner_dict = Owner(id = 1, name = '鈴木一郎', postalCode = '1140034', address = '東京都北区上十条2-25-4')
    return owner_dict

@strawberry.type
class Query:
    owner_data: Owner = strawberry.field(resolver = owner_get)
