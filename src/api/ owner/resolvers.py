import strawberry
from type import Owner
from strawberry.types import Info

async def get_owner(info: Info) -> Owner:
    return Owner(id = 1, name = '株式会社トータルメディエイト', postalCode = '1140034', address = '東京都北区上十条2-25-4')
