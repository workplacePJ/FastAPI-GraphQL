import strawberry
from type import Owner
from strawberry.types import Info

async def get_data__owner(info: Info, id: int) -> Owner:
    #owner_dict = await get_dict__owner(info, id)
    owner_dict = Owner(id = 1, name = '鈴木一郎', postalCode = '1140034', address = '東京都北区上十条2-25-4')
    return owner_dict
